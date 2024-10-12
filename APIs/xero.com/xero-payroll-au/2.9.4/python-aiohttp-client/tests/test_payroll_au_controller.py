# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_exception import APIException
from openapi_server.models.employee import Employee
from openapi_server.models.employees import Employees
from openapi_server.models.leave_application import LeaveApplication
from openapi_server.models.leave_applications import LeaveApplications
from openapi_server.models.pay_item import PayItem
from openapi_server.models.pay_items import PayItems
from openapi_server.models.pay_run import PayRun
from openapi_server.models.pay_runs import PayRuns
from openapi_server.models.payroll_calendar import PayrollCalendar
from openapi_server.models.payroll_calendars import PayrollCalendars
from openapi_server.models.payslip_lines import PayslipLines
from openapi_server.models.payslip_object import PayslipObject
from openapi_server.models.payslips import Payslips
from openapi_server.models.settings_object import SettingsObject
from openapi_server.models.super_fund import SuperFund
from openapi_server.models.super_fund_products import SuperFundProducts
from openapi_server.models.super_funds import SuperFunds
from openapi_server.models.timesheet import Timesheet
from openapi_server.models.timesheet_object import TimesheetObject
from openapi_server.models.timesheets import Timesheets


pytestmark = pytest.mark.asyncio

async def test_create_employee(client):
    """Test case for create_employee

    Creates a payroll employee
    """
    body = {"HomeAddress":{"AddressLine2":"Apt 4","AddressLine1":"123 Main St","Country":"AUSTRALIA","PostalCode":"3182","Region":"VIC","City":"St. Kilda"},"Email":"developer@me.com","UpdatedDateUTC":"/Date(1583967733054+0000)/","EmployeeGroupName":"marketing","ValidationErrors":[{"Message":"Message"},{"Message":"Message"}],"Gender":"F","JobTitle":"Manager","LeaveLines":[{"EntitlementFinalPayPayoutType":"NOTPAIDOUT","NumberOfUnits":2.5,"CalculationType":"NOCALCULATIONREQUIRED","EmploymentTerminationPaymentType":"O","IncludeSuperannuationGuaranteeContribution":True,"AnnualNumberOfUnits":2.5,"FullTimeNumberOfUnitsPerPeriod":2.5,"LeaveTypeID":"742998cb-7584-4ecf-aa88-d694f59c50f9"},{"EntitlementFinalPayPayoutType":"NOTPAIDOUT","NumberOfUnits":2.5,"CalculationType":"NOCALCULATIONREQUIRED","EmploymentTerminationPaymentType":"O","IncludeSuperannuationGuaranteeContribution":True,"AnnualNumberOfUnits":2.5,"FullTimeNumberOfUnitsPerPeriod":2.5,"LeaveTypeID":"742998cb-7584-4ecf-aa88-d694f59c50f9"}],"StartDate":"/Date(320284900000+0000)/","PayrollCalendarID":"2ee8e5cc-9835-40d5-bb18-09fdb118db9c","LeaveBalances":[{"NumberOfUnits":81.2602,"LeaveName":"Annual Leave","TypeOfUnits":"Hours","LeaveTypeID":"544d9292-4329-4512-bfff-a9f15236d776"},{"NumberOfUnits":81.2602,"LeaveName":"Annual Leave","TypeOfUnits":"Hours","LeaveTypeID":"544d9292-4329-4512-bfff-a9f15236d776"}],"Phone":"415-555-1212","Classification":"99383","PayTemplate":{"LeaveLines":[{"EntitlementFinalPayPayoutType":"NOTPAIDOUT","NumberOfUnits":2.5,"CalculationType":"NOCALCULATIONREQUIRED","EmploymentTerminationPaymentType":"O","IncludeSuperannuationGuaranteeContribution":True,"AnnualNumberOfUnits":2.5,"FullTimeNumberOfUnitsPerPeriod":2.5,"LeaveTypeID":"742998cb-7584-4ecf-aa88-d694f59c50f9"},{"EntitlementFinalPayPayoutType":"NOTPAIDOUT","NumberOfUnits":2.5,"CalculationType":"NOCALCULATIONREQUIRED","EmploymentTerminationPaymentType":"O","IncludeSuperannuationGuaranteeContribution":True,"AnnualNumberOfUnits":2.5,"FullTimeNumberOfUnitsPerPeriod":2.5,"LeaveTypeID":"742998cb-7584-4ecf-aa88-d694f59c50f9"}],"ReimbursementLines":[{"ExpenseAccount":"420","Description":"For the taxi","Amount":10,"ReimbursementTypeID":"bd246b96-c637-4767-81cf-851ba8fa93c2"},{"ExpenseAccount":"420","Description":"For the taxi","Amount":10,"ReimbursementTypeID":"bd246b96-c637-4767-81cf-851ba8fa93c2"}],"DeductionLines":[{"NumberOfUnits":10,"CalculationType":"FIXEDAMOUNT","Percentage":10,"Amount":10,"DeductionTypeID":"59cd9d04-4521-4cc3-93ac-7841651ff407"},{"NumberOfUnits":10,"CalculationType":"FIXEDAMOUNT","Percentage":10,"Amount":10,"DeductionTypeID":"59cd9d04-4521-4cc3-93ac-7841651ff407"}],"SuperLines":[{"CalculationType":"FIXEDAMOUNT","ContributionType":"SGC","Percentage":9,"Amount":10,"ExpenseAccountCode":"478","SuperMembershipID":"4333d5cd-53a5-4c31-98e5-a8b4e5676b0b","MinimumMonthlyEarnings":450,"LiabilityAccountCode":"826"},{"CalculationType":"FIXEDAMOUNT","ContributionType":"SGC","Percentage":9,"Amount":10,"ExpenseAccountCode":"478","SuperMembershipID":"4333d5cd-53a5-4c31-98e5-a8b4e5676b0b","MinimumMonthlyEarnings":450,"LiabilityAccountCode":"826"}],"EarningsLines":[{"EarningsRateID":"72e962d1-fcac-4083-8a71-742bb3e7ae14","NormalNumberOfUnits":38,"NumberOfUnits":2.5,"CalculationType":"USEEARNINGSRATE","Amount":38,"RatePerUnit":38,"AnnualSalary":40000,"FixedAmount":2.5,"NumberOfUnitsPerWeek":38},{"EarningsRateID":"72e962d1-fcac-4083-8a71-742bb3e7ae14","NormalNumberOfUnits":38,"NumberOfUnits":2.5,"CalculationType":"USEEARNINGSRATE","Amount":38,"RatePerUnit":38,"AnnualSalary":40000,"FixedAmount":2.5,"NumberOfUnitsPerWeek":38}]},"TaxDeclaration":{"HasTradeSupportLoanDebt":False,"TaxFreeThresholdClaimed":False,"UpdatedDateUTC":"/Date(1583967733054+0000)/","TaxOffsetEstimatedAmount":100,"UpwardVariationTaxWithholdingAmount":50,"EligibleToReceiveLeaveLoading":False,"TaxFileNumber":"123123123","TFNExemptionType":"NOTQUOTED","HasSFSSDebt":False,"AustralianResidentForTaxPurposes":True,"ApprovedWithholdingVariationPercentage":75,"HasHELPDebt":False,"EmploymentBasis":"FULLTIME","HasStudentStartupLoan":True,"EmployeeID":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","ResidencyStatus":"AUSTRALIANRESIDENT"},"IsAuthorisedToApproveLeave":False,"MiddleNames":"Adena","DateOfBirth":"/Date(322560000000+0000)/","OrdinaryEarningsRateID":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Status":"ACTIVE","FirstName":"Karen","OpeningBalances":{"LeaveLines":[{"EntitlementFinalPayPayoutType":"NOTPAIDOUT","NumberOfUnits":2.5,"CalculationType":"NOCALCULATIONREQUIRED","EmploymentTerminationPaymentType":"O","IncludeSuperannuationGuaranteeContribution":True,"AnnualNumberOfUnits":2.5,"FullTimeNumberOfUnitsPerPeriod":2.5,"LeaveTypeID":"742998cb-7584-4ecf-aa88-d694f59c50f9"},{"EntitlementFinalPayPayoutType":"NOTPAIDOUT","NumberOfUnits":2.5,"CalculationType":"NOCALCULATIONREQUIRED","EmploymentTerminationPaymentType":"O","IncludeSuperannuationGuaranteeContribution":True,"AnnualNumberOfUnits":2.5,"FullTimeNumberOfUnitsPerPeriod":2.5,"LeaveTypeID":"742998cb-7584-4ecf-aa88-d694f59c50f9"}],"ReimbursementLines":[{"ExpenseAccount":"420","Description":"For the taxi","Amount":10,"ReimbursementTypeID":"bd246b96-c637-4767-81cf-851ba8fa93c2"},{"ExpenseAccount":"420","Description":"For the taxi","Amount":10,"ReimbursementTypeID":"bd246b96-c637-4767-81cf-851ba8fa93c2"}],"DeductionLines":[{"NumberOfUnits":10,"CalculationType":"FIXEDAMOUNT","Percentage":10,"Amount":10,"DeductionTypeID":"59cd9d04-4521-4cc3-93ac-7841651ff407"},{"NumberOfUnits":10,"CalculationType":"FIXEDAMOUNT","Percentage":10,"Amount":10,"DeductionTypeID":"59cd9d04-4521-4cc3-93ac-7841651ff407"}],"Tax":"4333d5cd-53a5-4c31-98e5-a8b4e5676b0b","SuperLines":[{"CalculationType":"FIXEDAMOUNT","ContributionType":"SGC","Percentage":9,"Amount":10,"ExpenseAccountCode":"478","SuperMembershipID":"4333d5cd-53a5-4c31-98e5-a8b4e5676b0b","MinimumMonthlyEarnings":450,"LiabilityAccountCode":"826"},{"CalculationType":"FIXEDAMOUNT","ContributionType":"SGC","Percentage":9,"Amount":10,"ExpenseAccountCode":"478","SuperMembershipID":"4333d5cd-53a5-4c31-98e5-a8b4e5676b0b","MinimumMonthlyEarnings":450,"LiabilityAccountCode":"826"}],"OpeningBalanceDate":"/Date(322560000000+0000)/","EarningsLines":[{"EarningsRateID":"72e962d1-fcac-4083-8a71-742bb3e7ae14","NormalNumberOfUnits":38,"NumberOfUnits":2.5,"CalculationType":"USEEARNINGSRATE","Amount":38,"RatePerUnit":38,"AnnualSalary":40000,"FixedAmount":2.5,"NumberOfUnitsPerWeek":38},{"EarningsRateID":"72e962d1-fcac-4083-8a71-742bb3e7ae14","NormalNumberOfUnits":38,"NumberOfUnits":2.5,"CalculationType":"USEEARNINGSRATE","Amount":38,"RatePerUnit":38,"AnnualSalary":40000,"FixedAmount":2.5,"NumberOfUnitsPerWeek":38}]},"TerminationDate":"/Date(1584662400000+0000)/","SuperMemberships":[{"SuperFundID":"2187a42b-639a-45cb-9eed-cd4ae488306a","SuperMembershipID":"4333d5cd-53a5-4c31-98e5-a8b4e5676b0b","EmployeeNumber":"1234"},{"SuperFundID":"2187a42b-639a-45cb-9eed-cd4ae488306a","SuperMembershipID":"4333d5cd-53a5-4c31-98e5-a8b4e5676b0b","EmployeeNumber":"1234"}],"Title":"Mrs","IsAuthorisedToApproveTimesheets":True,"Mobile":"415-234-5678","TwitterUserName":"xeroapi","BankAccounts":[{"BSB":"122344","StatementText":"Salary","Amount":200,"AccountName":"James Lebron Savings","AccountNumber":"345678","Remainder":False},{"BSB":"122344","StatementText":"Salary","Amount":200,"AccountName":"James Lebron Savings","AccountNumber":"345678","Remainder":False}],"LastName":"Jones","EmployeeID":"4ff1e5cc-9835-40d5-bb18-09fdb118db9c"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/payroll.xro/1.0/Employees',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_leave_application(client):
    """Test case for create_leave_application

    Creates a leave application
    """
    body = {"StartDate":"/Date(322560000000+0000)/","Description":"My leave","UpdatedDateUTC":"/Date(1583967733054+0000)/","ValidationErrors":[{"Message":"Message"},{"Message":"Message"}],"LeaveApplicationID":"e0eb6747-7c17-4075-b804-989f8d4e5d39","Title":"Annual Leave","LeavePeriods":[{"PayPeriodStartDate":"/Date(322560000000+0000)/","PayPeriodEndDate":"/Date(322560000000+0000)/","NumberOfUnits":22.8,"LeavePeriodStatus":"SCHEDULED"},{"PayPeriodStartDate":"/Date(322560000000+0000)/","PayPeriodEndDate":"/Date(322560000000+0000)/","NumberOfUnits":22.8,"LeavePeriodStatus":"SCHEDULED"}],"EmployeeID":"fb4ebd68-6568-41eb-96ab-628a0f54b4b8","EndDate":"/Date(322560000000+0000)/","LeaveTypeID":"742998cb-7584-4ecf-aa88-d694f59c50f9"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/payroll.xro/1.0/LeaveApplications',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_pay_item(client):
    """Test case for create_pay_item

    Creates a pay item
    """
    body = {"LeaveTypes":[{"UpdatedDateUTC":"/Date(1583967733054+0000)/","ShowOnPayslip":True,"TypeOfUnits":"Hours","IsPaidLeave":True,"NormalEntitlement":152,"CurrentRecord":True,"LeaveLoadingRate":2,"LeaveTypeID":"e0eb6747-7c17-4075-b804-989f8d4e5d39","Name":"PTO"},{"UpdatedDateUTC":"/Date(1583967733054+0000)/","ShowOnPayslip":True,"TypeOfUnits":"Hours","IsPaidLeave":True,"NormalEntitlement":152,"CurrentRecord":True,"LeaveLoadingRate":2,"LeaveTypeID":"e0eb6747-7c17-4075-b804-989f8d4e5d39","Name":"PTO"}],"EarningsRates":[{"UpdatedDateUTC":"/Date(1583967733054+0000)/","Amount":50.3,"IsReportableAsW1":False,"RatePerUnit":"10","CurrentRecord":True,"AllowanceType":"CAR","EarningsType":"FIXED","Name":"PTO","EarningsRateID":"e0eb6747-7c17-4075-b804-989f8d4e5d39","AccrueLeave":False,"IsExemptFromTax":False,"EmploymentTerminationPaymentType":"O","AccountCode":"720","Multiplier":1.5,"TypeOfUnits":"Fixed","IsExemptFromSuper":False,"RateType":"FIXEDAMOUNT"},{"UpdatedDateUTC":"/Date(1583967733054+0000)/","Amount":50.3,"IsReportableAsW1":False,"RatePerUnit":"10","CurrentRecord":True,"AllowanceType":"CAR","EarningsType":"FIXED","Name":"PTO","EarningsRateID":"e0eb6747-7c17-4075-b804-989f8d4e5d39","AccrueLeave":False,"IsExemptFromTax":False,"EmploymentTerminationPaymentType":"O","AccountCode":"720","Multiplier":1.5,"TypeOfUnits":"Fixed","IsExemptFromSuper":False,"RateType":"FIXEDAMOUNT"}],"ReimbursementTypes":[{"UpdatedDateUTC":"/Date(1583967733054+0000)/","AccountCode":"720","CurrentRecord":True,"ReimbursementTypeID":"e0eb6747-7c17-4075-b804-989f8d4e5d39","Name":"PTO"},{"UpdatedDateUTC":"/Date(1583967733054+0000)/","AccountCode":"720","CurrentRecord":True,"ReimbursementTypeID":"e0eb6747-7c17-4075-b804-989f8d4e5d39","Name":"PTO"}],"DeductionTypes":[{"DeductionCategory":"NONE","UpdatedDateUTC":"/Date(1583967733054+0000)/","ReducesTax":False,"AccountCode":"720","ReducesSuper":False,"CurrentRecord":True,"DeductionTypeID":"e0eb6747-7c17-4075-b804-989f8d4e5d39","IsExemptFromW1":False,"Name":"PTO"},{"DeductionCategory":"NONE","UpdatedDateUTC":"/Date(1583967733054+0000)/","ReducesTax":False,"AccountCode":"720","ReducesSuper":False,"CurrentRecord":True,"DeductionTypeID":"e0eb6747-7c17-4075-b804-989f8d4e5d39","IsExemptFromW1":False,"Name":"PTO"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/payroll.xro/1.0/PayItems',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_pay_run(client):
    """Test case for create_pay_run

    Creates a pay run
    """
    body = {"PayRunStatus":"DRAFT","PayslipMessage":"Thanks for being awesome","PayRunPeriodEndDate":"/Date(322560000000+0000)/","UpdatedDateUTC":"/Date(1583967733054+0000)/","PaymentDate":"/Date(322560000000+0000)/","ValidationErrors":[{"Message":"Message"},{"Message":"Message"}],"Tax":198,"PayRunID":"bba1d10f-63b1-4692-b5c5-a99f869523a4","PayrollCalendarID":"bfac31bd-ea62-4fc8-a5e7-7965d9504b15","Super":75.6,"NetPay":862.5,"Payslips":[{"Reimbursements":0,"Super":75.6,"EmployeeGroup":"Marketing","NetPay":862.5,"PayslipID":"f3c0874d-7cdd-459a-a95c-d90d51decc42","UpdatedDateUTC":"/Date(1583967733054+0000)/","FirstName":"Karen","Deductions":0,"Tax":198,"LastName":"Jones","EmployeeID":"4729f087-8eec-49c1-8294-4d11a5a0a37c","Wages":1060.5},{"Reimbursements":0,"Super":75.6,"EmployeeGroup":"Marketing","NetPay":862.5,"PayslipID":"f3c0874d-7cdd-459a-a95c-d90d51decc42","UpdatedDateUTC":"/Date(1583967733054+0000)/","FirstName":"Karen","Deductions":0,"Tax":198,"LastName":"Jones","EmployeeID":"4729f087-8eec-49c1-8294-4d11a5a0a37c","Wages":1060.5}],"Deductions":0,"Reimbursement":0,"Wages":1060.5,"PayRunPeriodStartDate":"/Date(322560000000+0000)/"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/payroll.xro/1.0/PayRuns',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_payroll_calendar(client):
    """Test case for create_payroll_calendar

    Creates a Payroll Calendar
    """
    body = {"StartDate":"/Date(322560000000+0000)/","PayrollCalendarID":"e0eb6747-7c17-4075-b804-989f8d4e5d39","UpdatedDateUTC":"/Date(1583967733054+0000)/","PaymentDate":"/Date(322560000000+0000)/","ValidationErrors":[{"Message":"Message"},{"Message":"Message"}],"CalendarType":"WEEKLY","Name":"Fortnightly Calendar"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/payroll.xro/1.0/PayrollCalendars',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_superfund(client):
    """Test case for create_superfund

    Creates a superfund
    """
    body = {"SuperFundID":"bfac31bd-ea62-4fc8-a5e7-7965d9504b15","SPIN":"4545445454","UpdatedDateUTC":"/Date(1583967733054+0000)/","ValidationErrors":[{"Message":"Message"},{"Message":"Message"}],"USI":"40022701955001","ABN":"40022701955","AccountNumber":"234234234","Name":"MLC Navigator Retirement Plan - Superannuation Service (including Series 2) (MLC Superannuation Fund)","BSB":"234324","Type":"REGULATED","EmployerNumber":"324324","ElectronicServiceAddress":"12345678","AccountName":"Money account"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/payroll.xro/1.0/Superfunds',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_timesheet(client):
    """Test case for create_timesheet

    Creates a timesheet
    """
    body = {"StartDate":"/Date(322560000000+0000)/","Status":"DRAFT","UpdatedDateUTC":"/Date(1583967733054+0000)/","Hours":31,"ValidationErrors":[{"Message":"Message"},{"Message":"Message"}],"TimesheetLines":[{"EarningsRateID":"966c5c77-2ef0-4320-b6a9-6c27b080ecc5","NumberOfUnits":[3,3],"UpdatedDateUTC":"/Date(1583967733054+0000)/","TrackingItemID":"ae777a87-5ef3-4fa0-a4f0-d10e1f13073a"},{"EarningsRateID":"966c5c77-2ef0-4320-b6a9-6c27b080ecc5","NumberOfUnits":[3,3],"UpdatedDateUTC":"/Date(1583967733054+0000)/","TrackingItemID":"ae777a87-5ef3-4fa0-a4f0-d10e1f13073a"}],"TimesheetID":"049765fc-4506-48fb-bf88-3578dec0ec47","EmployeeID":"72a0d0c2-0cf8-4f0b-ade1-33231f47b41b","EndDate":"/Date(322560000000+0000)/"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/payroll.xro/1.0/Timesheets',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employee(client):
    """Test case for get_employee

    Retrieves an employee's detail by unique employee id
    """
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/payroll.xro/1.0/Employees/{employee_id}'.format(employee_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employees(client):
    """Test case for get_employees

    Searches payroll employees
    """
    params = [('where', 'Status==\"ACTIVE\"'),
                    ('order', 'EmailAddress%20DESC'),
                    ('page', 56)]
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'if_modified_since': 'if_modified_since_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/payroll.xro/1.0/Employees',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_leave_application(client):
    """Test case for get_leave_application

    Retrieves a leave application by a unique leave application id
    """
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/payroll.xro/1.0/LeaveApplications/{leave_application_id}'.format(leave_application_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_leave_applications(client):
    """Test case for get_leave_applications

    Retrieves leave applications
    """
    params = [('where', 'Status==\"ACTIVE\"'),
                    ('order', 'EmailAddress%20DESC'),
                    ('page', 56)]
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'if_modified_since': 'if_modified_since_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/payroll.xro/1.0/LeaveApplications',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_items(client):
    """Test case for get_pay_items

    Retrieves pay items
    """
    params = [('where', 'Status==\"ACTIVE\"'),
                    ('order', 'EmailAddress%20DESC'),
                    ('page', 56)]
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'if_modified_since': 'if_modified_since_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/payroll.xro/1.0/PayItems',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_run(client):
    """Test case for get_pay_run

    Retrieves a pay run by using a unique pay run id
    """
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/payroll.xro/1.0/PayRuns/{pay_run_id}'.format(pay_run_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_runs(client):
    """Test case for get_pay_runs

    Retrieves pay runs
    """
    params = [('where', 'Status==\"ACTIVE\"'),
                    ('order', 'EmailAddress%20DESC'),
                    ('page', 56)]
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'if_modified_since': 'if_modified_since_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/payroll.xro/1.0/PayRuns',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payroll_calendar(client):
    """Test case for get_payroll_calendar

    Retrieves payroll calendar by using a unique payroll calendar ID
    """
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/payroll.xro/1.0/PayrollCalendars/{payroll_calendar_id}'.format(payroll_calendar_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payroll_calendars(client):
    """Test case for get_payroll_calendars

    Retrieves payroll calendars
    """
    params = [('where', 'Status==\"ACTIVE\"'),
                    ('order', 'EmailAddress%20DESC'),
                    ('page', 56)]
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'if_modified_since': 'if_modified_since_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/payroll.xro/1.0/PayrollCalendars',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_payslip(client):
    """Test case for get_payslip

    Retrieves for a payslip by a unique payslip id
    """
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/payroll.xro/1.0/Payslip/{payslip_id}'.format(payslip_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_settings(client):
    """Test case for get_settings

    Retrieves payroll settings
    """
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/payroll.xro/1.0/Settings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_superfund(client):
    """Test case for get_superfund

    Retrieves a superfund by using a unique superfund ID
    """
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/payroll.xro/1.0/Superfunds/{super_fund_id}'.format(super_fund_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_superfund_products(client):
    """Test case for get_superfund_products

    Retrieves superfund products
    """
    params = [('ABN', '40022701955'),
                    ('USI', 'OSF0001AU')]
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/payroll.xro/1.0/SuperfundProducts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_superfunds(client):
    """Test case for get_superfunds

    Retrieves superfunds
    """
    params = [('where', 'Status==\"ACTIVE\"'),
                    ('order', 'EmailAddress%20DESC'),
                    ('page', 56)]
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'if_modified_since': 'if_modified_since_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/payroll.xro/1.0/Superfunds',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_timesheet(client):
    """Test case for get_timesheet

    Retrieves a timesheet by using a unique timesheet id
    """
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/payroll.xro/1.0/Timesheets/{timesheet_id}'.format(timesheet_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_timesheets(client):
    """Test case for get_timesheets

    Retrieves timesheets
    """
    params = [('where', 'Status==\"ACTIVE\"'),
                    ('order', 'EmailAddress%20DESC'),
                    ('page', 56)]
    headers = { 
        'Accept': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'if_modified_since': 'if_modified_since_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/payroll.xro/1.0/Timesheets',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_employee(client):
    """Test case for update_employee

    Updates an employee's detail
    """
    body = {"HomeAddress":{"AddressLine2":"Apt 4","AddressLine1":"123 Main St","Country":"AUSTRALIA","PostalCode":"3182","Region":"VIC","City":"St. Kilda"},"Email":"developer@me.com","UpdatedDateUTC":"/Date(1583967733054+0000)/","EmployeeGroupName":"marketing","ValidationErrors":[{"Message":"Message"},{"Message":"Message"}],"Gender":"F","JobTitle":"Manager","LeaveLines":[{"EntitlementFinalPayPayoutType":"NOTPAIDOUT","NumberOfUnits":2.5,"CalculationType":"NOCALCULATIONREQUIRED","EmploymentTerminationPaymentType":"O","IncludeSuperannuationGuaranteeContribution":True,"AnnualNumberOfUnits":2.5,"FullTimeNumberOfUnitsPerPeriod":2.5,"LeaveTypeID":"742998cb-7584-4ecf-aa88-d694f59c50f9"},{"EntitlementFinalPayPayoutType":"NOTPAIDOUT","NumberOfUnits":2.5,"CalculationType":"NOCALCULATIONREQUIRED","EmploymentTerminationPaymentType":"O","IncludeSuperannuationGuaranteeContribution":True,"AnnualNumberOfUnits":2.5,"FullTimeNumberOfUnitsPerPeriod":2.5,"LeaveTypeID":"742998cb-7584-4ecf-aa88-d694f59c50f9"}],"StartDate":"/Date(320284900000+0000)/","PayrollCalendarID":"2ee8e5cc-9835-40d5-bb18-09fdb118db9c","LeaveBalances":[{"NumberOfUnits":81.2602,"LeaveName":"Annual Leave","TypeOfUnits":"Hours","LeaveTypeID":"544d9292-4329-4512-bfff-a9f15236d776"},{"NumberOfUnits":81.2602,"LeaveName":"Annual Leave","TypeOfUnits":"Hours","LeaveTypeID":"544d9292-4329-4512-bfff-a9f15236d776"}],"Phone":"415-555-1212","Classification":"99383","PayTemplate":{"LeaveLines":[{"EntitlementFinalPayPayoutType":"NOTPAIDOUT","NumberOfUnits":2.5,"CalculationType":"NOCALCULATIONREQUIRED","EmploymentTerminationPaymentType":"O","IncludeSuperannuationGuaranteeContribution":True,"AnnualNumberOfUnits":2.5,"FullTimeNumberOfUnitsPerPeriod":2.5,"LeaveTypeID":"742998cb-7584-4ecf-aa88-d694f59c50f9"},{"EntitlementFinalPayPayoutType":"NOTPAIDOUT","NumberOfUnits":2.5,"CalculationType":"NOCALCULATIONREQUIRED","EmploymentTerminationPaymentType":"O","IncludeSuperannuationGuaranteeContribution":True,"AnnualNumberOfUnits":2.5,"FullTimeNumberOfUnitsPerPeriod":2.5,"LeaveTypeID":"742998cb-7584-4ecf-aa88-d694f59c50f9"}],"ReimbursementLines":[{"ExpenseAccount":"420","Description":"For the taxi","Amount":10,"ReimbursementTypeID":"bd246b96-c637-4767-81cf-851ba8fa93c2"},{"ExpenseAccount":"420","Description":"For the taxi","Amount":10,"ReimbursementTypeID":"bd246b96-c637-4767-81cf-851ba8fa93c2"}],"DeductionLines":[{"NumberOfUnits":10,"CalculationType":"FIXEDAMOUNT","Percentage":10,"Amount":10,"DeductionTypeID":"59cd9d04-4521-4cc3-93ac-7841651ff407"},{"NumberOfUnits":10,"CalculationType":"FIXEDAMOUNT","Percentage":10,"Amount":10,"DeductionTypeID":"59cd9d04-4521-4cc3-93ac-7841651ff407"}],"SuperLines":[{"CalculationType":"FIXEDAMOUNT","ContributionType":"SGC","Percentage":9,"Amount":10,"ExpenseAccountCode":"478","SuperMembershipID":"4333d5cd-53a5-4c31-98e5-a8b4e5676b0b","MinimumMonthlyEarnings":450,"LiabilityAccountCode":"826"},{"CalculationType":"FIXEDAMOUNT","ContributionType":"SGC","Percentage":9,"Amount":10,"ExpenseAccountCode":"478","SuperMembershipID":"4333d5cd-53a5-4c31-98e5-a8b4e5676b0b","MinimumMonthlyEarnings":450,"LiabilityAccountCode":"826"}],"EarningsLines":[{"EarningsRateID":"72e962d1-fcac-4083-8a71-742bb3e7ae14","NormalNumberOfUnits":38,"NumberOfUnits":2.5,"CalculationType":"USEEARNINGSRATE","Amount":38,"RatePerUnit":38,"AnnualSalary":40000,"FixedAmount":2.5,"NumberOfUnitsPerWeek":38},{"EarningsRateID":"72e962d1-fcac-4083-8a71-742bb3e7ae14","NormalNumberOfUnits":38,"NumberOfUnits":2.5,"CalculationType":"USEEARNINGSRATE","Amount":38,"RatePerUnit":38,"AnnualSalary":40000,"FixedAmount":2.5,"NumberOfUnitsPerWeek":38}]},"TaxDeclaration":{"HasTradeSupportLoanDebt":False,"TaxFreeThresholdClaimed":False,"UpdatedDateUTC":"/Date(1583967733054+0000)/","TaxOffsetEstimatedAmount":100,"UpwardVariationTaxWithholdingAmount":50,"EligibleToReceiveLeaveLoading":False,"TaxFileNumber":"123123123","TFNExemptionType":"NOTQUOTED","HasSFSSDebt":False,"AustralianResidentForTaxPurposes":True,"ApprovedWithholdingVariationPercentage":75,"HasHELPDebt":False,"EmploymentBasis":"FULLTIME","HasStudentStartupLoan":True,"EmployeeID":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","ResidencyStatus":"AUSTRALIANRESIDENT"},"IsAuthorisedToApproveLeave":False,"MiddleNames":"Adena","DateOfBirth":"/Date(322560000000+0000)/","OrdinaryEarningsRateID":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","Status":"ACTIVE","FirstName":"Karen","OpeningBalances":{"LeaveLines":[{"EntitlementFinalPayPayoutType":"NOTPAIDOUT","NumberOfUnits":2.5,"CalculationType":"NOCALCULATIONREQUIRED","EmploymentTerminationPaymentType":"O","IncludeSuperannuationGuaranteeContribution":True,"AnnualNumberOfUnits":2.5,"FullTimeNumberOfUnitsPerPeriod":2.5,"LeaveTypeID":"742998cb-7584-4ecf-aa88-d694f59c50f9"},{"EntitlementFinalPayPayoutType":"NOTPAIDOUT","NumberOfUnits":2.5,"CalculationType":"NOCALCULATIONREQUIRED","EmploymentTerminationPaymentType":"O","IncludeSuperannuationGuaranteeContribution":True,"AnnualNumberOfUnits":2.5,"FullTimeNumberOfUnitsPerPeriod":2.5,"LeaveTypeID":"742998cb-7584-4ecf-aa88-d694f59c50f9"}],"ReimbursementLines":[{"ExpenseAccount":"420","Description":"For the taxi","Amount":10,"ReimbursementTypeID":"bd246b96-c637-4767-81cf-851ba8fa93c2"},{"ExpenseAccount":"420","Description":"For the taxi","Amount":10,"ReimbursementTypeID":"bd246b96-c637-4767-81cf-851ba8fa93c2"}],"DeductionLines":[{"NumberOfUnits":10,"CalculationType":"FIXEDAMOUNT","Percentage":10,"Amount":10,"DeductionTypeID":"59cd9d04-4521-4cc3-93ac-7841651ff407"},{"NumberOfUnits":10,"CalculationType":"FIXEDAMOUNT","Percentage":10,"Amount":10,"DeductionTypeID":"59cd9d04-4521-4cc3-93ac-7841651ff407"}],"Tax":"4333d5cd-53a5-4c31-98e5-a8b4e5676b0b","SuperLines":[{"CalculationType":"FIXEDAMOUNT","ContributionType":"SGC","Percentage":9,"Amount":10,"ExpenseAccountCode":"478","SuperMembershipID":"4333d5cd-53a5-4c31-98e5-a8b4e5676b0b","MinimumMonthlyEarnings":450,"LiabilityAccountCode":"826"},{"CalculationType":"FIXEDAMOUNT","ContributionType":"SGC","Percentage":9,"Amount":10,"ExpenseAccountCode":"478","SuperMembershipID":"4333d5cd-53a5-4c31-98e5-a8b4e5676b0b","MinimumMonthlyEarnings":450,"LiabilityAccountCode":"826"}],"OpeningBalanceDate":"/Date(322560000000+0000)/","EarningsLines":[{"EarningsRateID":"72e962d1-fcac-4083-8a71-742bb3e7ae14","NormalNumberOfUnits":38,"NumberOfUnits":2.5,"CalculationType":"USEEARNINGSRATE","Amount":38,"RatePerUnit":38,"AnnualSalary":40000,"FixedAmount":2.5,"NumberOfUnitsPerWeek":38},{"EarningsRateID":"72e962d1-fcac-4083-8a71-742bb3e7ae14","NormalNumberOfUnits":38,"NumberOfUnits":2.5,"CalculationType":"USEEARNINGSRATE","Amount":38,"RatePerUnit":38,"AnnualSalary":40000,"FixedAmount":2.5,"NumberOfUnitsPerWeek":38}]},"TerminationDate":"/Date(1584662400000+0000)/","SuperMemberships":[{"SuperFundID":"2187a42b-639a-45cb-9eed-cd4ae488306a","SuperMembershipID":"4333d5cd-53a5-4c31-98e5-a8b4e5676b0b","EmployeeNumber":"1234"},{"SuperFundID":"2187a42b-639a-45cb-9eed-cd4ae488306a","SuperMembershipID":"4333d5cd-53a5-4c31-98e5-a8b4e5676b0b","EmployeeNumber":"1234"}],"Title":"Mrs","IsAuthorisedToApproveTimesheets":True,"Mobile":"415-234-5678","TwitterUserName":"xeroapi","BankAccounts":[{"BSB":"122344","StatementText":"Salary","Amount":200,"AccountName":"James Lebron Savings","AccountNumber":"345678","Remainder":False},{"BSB":"122344","StatementText":"Salary","Amount":200,"AccountName":"James Lebron Savings","AccountNumber":"345678","Remainder":False}],"LastName":"Jones","EmployeeID":"4ff1e5cc-9835-40d5-bb18-09fdb118db9c"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/payroll.xro/1.0/Employees/{employee_id}'.format(employee_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_leave_application(client):
    """Test case for update_leave_application

    Updates a specific leave application
    """
    body = {"StartDate":"/Date(322560000000+0000)/","Description":"My leave","UpdatedDateUTC":"/Date(1583967733054+0000)/","ValidationErrors":[{"Message":"Message"},{"Message":"Message"}],"LeaveApplicationID":"e0eb6747-7c17-4075-b804-989f8d4e5d39","Title":"Annual Leave","LeavePeriods":[{"PayPeriodStartDate":"/Date(322560000000+0000)/","PayPeriodEndDate":"/Date(322560000000+0000)/","NumberOfUnits":22.8,"LeavePeriodStatus":"SCHEDULED"},{"PayPeriodStartDate":"/Date(322560000000+0000)/","PayPeriodEndDate":"/Date(322560000000+0000)/","NumberOfUnits":22.8,"LeavePeriodStatus":"SCHEDULED"}],"EmployeeID":"fb4ebd68-6568-41eb-96ab-628a0f54b4b8","EndDate":"/Date(322560000000+0000)/","LeaveTypeID":"742998cb-7584-4ecf-aa88-d694f59c50f9"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/payroll.xro/1.0/LeaveApplications/{leave_application_id}'.format(leave_application_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_pay_run(client):
    """Test case for update_pay_run

    Updates a pay run
    """
    body = {"PayRunStatus":"DRAFT","PayslipMessage":"Thanks for being awesome","PayRunPeriodEndDate":"/Date(322560000000+0000)/","UpdatedDateUTC":"/Date(1583967733054+0000)/","PaymentDate":"/Date(322560000000+0000)/","ValidationErrors":[{"Message":"Message"},{"Message":"Message"}],"Tax":198,"PayRunID":"bba1d10f-63b1-4692-b5c5-a99f869523a4","PayrollCalendarID":"bfac31bd-ea62-4fc8-a5e7-7965d9504b15","Super":75.6,"NetPay":862.5,"Payslips":[{"Reimbursements":0,"Super":75.6,"EmployeeGroup":"Marketing","NetPay":862.5,"PayslipID":"f3c0874d-7cdd-459a-a95c-d90d51decc42","UpdatedDateUTC":"/Date(1583967733054+0000)/","FirstName":"Karen","Deductions":0,"Tax":198,"LastName":"Jones","EmployeeID":"4729f087-8eec-49c1-8294-4d11a5a0a37c","Wages":1060.5},{"Reimbursements":0,"Super":75.6,"EmployeeGroup":"Marketing","NetPay":862.5,"PayslipID":"f3c0874d-7cdd-459a-a95c-d90d51decc42","UpdatedDateUTC":"/Date(1583967733054+0000)/","FirstName":"Karen","Deductions":0,"Tax":198,"LastName":"Jones","EmployeeID":"4729f087-8eec-49c1-8294-4d11a5a0a37c","Wages":1060.5}],"Deductions":0,"Reimbursement":0,"Wages":1060.5,"PayRunPeriodStartDate":"/Date(322560000000+0000)/"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/payroll.xro/1.0/PayRuns/{pay_run_id}'.format(pay_run_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_payslip(client):
    """Test case for update_payslip

    Updates a payslip
    """
    body = {"SuperannuationLines":[{"PaymentDateForThisPeriod":"/Date(322560000000+0000)/","CalculationType":"FIXEDAMOUNT","ContributionType":"SGC","Percentage":4,"Amount":10.5,"ExpenseAccountCode":"450","SuperMembershipID":"e0eb6747-7c17-4075-b804-989f8d4e5d39","MinimumMonthlyEarnings":100.5,"LiabilityAccountCode":"650"},{"PaymentDateForThisPeriod":"/Date(322560000000+0000)/","CalculationType":"FIXEDAMOUNT","ContributionType":"SGC","Percentage":4,"Amount":10.5,"ExpenseAccountCode":"450","SuperMembershipID":"e0eb6747-7c17-4075-b804-989f8d4e5d39","MinimumMonthlyEarnings":100.5,"LiabilityAccountCode":"650"}],"TaxLines":[{"ManualTaxType":"PAYGMANUAL","LiabilityAccount":"620","Description":"Description","PayslipTaxLineID":"e0eb6747-7c17-4075-b804-989f8d4e5d39","Amount":50,"TaxTypeName":"Manual Adjustment"},{"ManualTaxType":"PAYGMANUAL","LiabilityAccount":"620","Description":"Description","PayslipTaxLineID":"e0eb6747-7c17-4075-b804-989f8d4e5d39","Amount":50,"TaxTypeName":"Manual Adjustment"}],"ReimbursementLines":[{"ExpenseAccount":"420","Description":"For the taxi","Amount":10,"ReimbursementTypeID":"bd246b96-c637-4767-81cf-851ba8fa93c2"},{"ExpenseAccount":"420","Description":"For the taxi","Amount":10,"ReimbursementTypeID":"bd246b96-c637-4767-81cf-851ba8fa93c2"}],"DeductionLines":[{"NumberOfUnits":10,"CalculationType":"FIXEDAMOUNT","Percentage":10,"Amount":10,"DeductionTypeID":"59cd9d04-4521-4cc3-93ac-7841651ff407"},{"NumberOfUnits":10,"CalculationType":"FIXEDAMOUNT","Percentage":10,"Amount":10,"DeductionTypeID":"59cd9d04-4521-4cc3-93ac-7841651ff407"}],"LeaveEarningsLines":[{"EarningsRateID":"e0eb6747-7c17-4075-b804-989f8d4e5d39","NumberOfUnits":2.5,"RatePerUnit":38},{"EarningsRateID":"e0eb6747-7c17-4075-b804-989f8d4e5d39","NumberOfUnits":2.5,"RatePerUnit":38}],"TimesheetEarningsLines":[{"EarningsRateID":"72e962d1-fcac-4083-8a71-742bb3e7ae14","NormalNumberOfUnits":38,"NumberOfUnits":2.5,"CalculationType":"USEEARNINGSRATE","Amount":38,"RatePerUnit":38,"AnnualSalary":40000,"FixedAmount":2.5,"NumberOfUnitsPerWeek":38},{"EarningsRateID":"72e962d1-fcac-4083-8a71-742bb3e7ae14","NormalNumberOfUnits":38,"NumberOfUnits":2.5,"CalculationType":"USEEARNINGSRATE","Amount":38,"RatePerUnit":38,"AnnualSalary":40000,"FixedAmount":2.5,"NumberOfUnitsPerWeek":38}],"EarningsLines":[{"EarningsRateID":"72e962d1-fcac-4083-8a71-742bb3e7ae14","NormalNumberOfUnits":38,"NumberOfUnits":2.5,"CalculationType":"USEEARNINGSRATE","Amount":38,"RatePerUnit":38,"AnnualSalary":40000,"FixedAmount":2.5,"NumberOfUnitsPerWeek":38},{"EarningsRateID":"72e962d1-fcac-4083-8a71-742bb3e7ae14","NormalNumberOfUnits":38,"NumberOfUnits":2.5,"CalculationType":"USEEARNINGSRATE","Amount":38,"RatePerUnit":38,"AnnualSalary":40000,"FixedAmount":2.5,"NumberOfUnitsPerWeek":38}],"LeaveAccrualLines":[{"NumberOfUnits":105.5,"AutoCalculate":True,"LeaveTypeID":"e0eb6747-7c17-4075-b804-989f8d4e5d39"},{"NumberOfUnits":105.5,"AutoCalculate":True,"LeaveTypeID":"e0eb6747-7c17-4075-b804-989f8d4e5d39"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/payroll.xro/1.0/Payslip/{payslip_id}'.format(payslip_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_superfund(client):
    """Test case for update_superfund

    Updates a superfund
    """
    body = {"SuperFundID":"bfac31bd-ea62-4fc8-a5e7-7965d9504b15","SPIN":"4545445454","UpdatedDateUTC":"/Date(1583967733054+0000)/","ValidationErrors":[{"Message":"Message"},{"Message":"Message"}],"USI":"40022701955001","ABN":"40022701955","AccountNumber":"234234234","Name":"MLC Navigator Retirement Plan - Superannuation Service (including Series 2) (MLC Superannuation Fund)","BSB":"234324","Type":"REGULATED","EmployerNumber":"324324","ElectronicServiceAddress":"12345678","AccountName":"Money account"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/payroll.xro/1.0/Superfunds/{super_fund_id}'.format(super_fund_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_timesheet(client):
    """Test case for update_timesheet

    Updates a timesheet
    """
    body = {"StartDate":"/Date(322560000000+0000)/","Status":"DRAFT","UpdatedDateUTC":"/Date(1583967733054+0000)/","Hours":31,"ValidationErrors":[{"Message":"Message"},{"Message":"Message"}],"TimesheetLines":[{"EarningsRateID":"966c5c77-2ef0-4320-b6a9-6c27b080ecc5","NumberOfUnits":[3,3],"UpdatedDateUTC":"/Date(1583967733054+0000)/","TrackingItemID":"ae777a87-5ef3-4fa0-a4f0-d10e1f13073a"},{"EarningsRateID":"966c5c77-2ef0-4320-b6a9-6c27b080ecc5","NumberOfUnits":[3,3],"UpdatedDateUTC":"/Date(1583967733054+0000)/","TrackingItemID":"ae777a87-5ef3-4fa0-a4f0-d10e1f13073a"}],"TimesheetID":"049765fc-4506-48fb-bf88-3578dec0ec47","EmployeeID":"72a0d0c2-0cf8-4f0b-ade1-33231f47b41b","EndDate":"/Date(322560000000+0000)/"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'xero_tenant_id': 'xero_tenant_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/payroll.xro/1.0/Timesheets/{timesheet_id}'.format(timesheet_id='4ff1e5cc-9835-40d5-bb18-09fdb118db9c'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

