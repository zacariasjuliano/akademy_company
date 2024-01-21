from trytond.model import ModelSQL, ModelView, fields, Unique
from trytond.transaction import Transaction
from trytond.pyson import Eval, If
from trytond.pool import PoolMeta
from datetime import date


class Company(metaclass=PoolMeta):
    'Company'
    __name__ = 'company.company'
    
    party = fields.Many2One(
        'party.party', 'Party', 
        domain=[
            ('is_institution', '=', True)
            ], required=True,
        ondelete='CASCADE')
    student = fields.One2Many('company.student', 'company', 'Discentes',
        help="Adicionar discentes a instituição.")


class Employee(metaclass=PoolMeta):
    'Employee'
    __name__ = 'company.employee'
       
    teacher = fields.Boolean(
        'Docente', 
        help="A entidade será tratada como docente.")
    party = fields.Many2One(
        'party.party', 'Party', 
        domain=[
            ('is_person', '=', True)
            ], required=True, 
        context={
            'company': If(
                Eval('company', -1) >= 0, Eval('company', None), None),
            },
        depends={'company'}, ondelete="RESTRICT",
        help="The party which represents the employee.")

    @classmethod
    def default_start_date(cls):
        return date.today()  
    

class Student(ModelSQL, ModelView):
    'Student'
    __name__ = 'company.student'

    code = fields.Char('Nº de matrícula', size=20,
        help="Número de matrícula do discente.")
    start_date = fields.Date('Início',
        domain=[
                If(
                    (Eval('start_date')) & (Eval('end_date')),
                    ('start_date', '<=', Eval('end_date')),
                    (),
                )
            ], depends={'end_date'},
        required=True, help="Início da formação.")
    end_date = fields.Date('Fim',
        domain=[
                If(
                    (Eval('start_date')) & (Eval('end_date')),
                    ('end_date', '>=', Eval('start_date')),
                    (),
                )
            ], depends=['start_date'],
        help="Fim da formação.")    
    party = fields.Many2One(
        'party.party', 'Nome', 
        required=True, domain=[
            ('is_person', '=', True)
            ], ondelete="RESTRICT",
        help="Nome do discente.")
    company = fields.Many2One(
        'company.company', 'Instituição',
        readonly=True, ondelete="RESTRICT",
        help="Nome da instituição.")       
    
    @classmethod
    def __setup__(cls):
        super(Student, cls).__setup__()
        table = cls.__table__()
        cls._sql_constraints = [
            ('key', Unique(table, table.party),
            u'Não foi possível cadastrar o nova discente, por favor verifica se o discente já existe.')
        ]
        cls._order = [('party', 'ASC')]
        
    @classmethod
    def default_start_date(cls):
        return date.today()

    @staticmethod
    def default_company():
        return Transaction().context.get('company')

    def get_rec_name(self, name):
        return self.party.rec_name

    @classmethod
    def search_rec_name(cls, name, clause):
        return [('party.rec_name',) + tuple(clause[1:])]

