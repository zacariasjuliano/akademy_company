from trytond.pool import Pool
from . import company
from . import party
from . import report

def register():
	Pool.register(
		company.Employee,
        company.Student,
		party.Party,
		
		module='akademy_company', type_='model'
	)

	Pool.register(
		report.CompanyReport,
		report.EmployeeReport,
		report.StudentReport,

		module='akademy_company', type_='report'
	)

