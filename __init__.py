from trytond.pool import Pool
from . import company

def register():
	Pool.register(
		company.Employee,
        company.Student,
		
		module='akademy_company', type_='model'
	)

