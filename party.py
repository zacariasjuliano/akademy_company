from trytond.model import fields
from trytond.pool import PoolMeta


class Party(metaclass=PoolMeta):
    'Party'
    __name__ = 'party.party'
    
    student = fields.One2Many('company.student', 'party', 'Discente')    

