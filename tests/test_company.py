from trytond.tests.test_tryton import ModuleTestCase, with_transaction

class CompanyTestCase(ModuleTestCase):
    "Company Test Case"
    module = 'akademy_company'

    @with_transaction()
    def test_method(self):
        "Test method"
        self.assertTrue(True)

del ModuleTestCase
