from trytond.pool import Pool
from . import company
from . import party

def register():
	Pool.register(
		company.Employee,
        company.Student,
		party.Party,
		
		module='akademy_company', type_='model'
	)

