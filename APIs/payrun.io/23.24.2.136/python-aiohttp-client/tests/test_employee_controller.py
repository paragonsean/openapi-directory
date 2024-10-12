# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ae_assessment import AEAssessment
from openapi_server.models.commentary import Commentary
from openapi_server.models.employee import Employee
from openapi_server.models.employee_secret import EmployeeSecret
from openapi_server.models.employee_summary import EmployeeSummary
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection


pytestmark = pytest.mark.asyncio

async def test_delete_employee(client):
    """Test case for delete_employee

    Delete an Employee
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/Employee/{employee_id}'.format(employer_id='employer_id_example', employee_id='employee_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_employee_revision(client):
    """Test case for delete_employee_revision

    Delete an Employee revision matching the specified revision date.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/Employee/{employee_id}/{effective_date}'.format(employer_id='employer_id_example', employee_id='employee_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_employee_revision_by_number(client):
    """Test case for delete_employee_revision_by_number

    Delete an Employee revision matching the specified revision number.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/Employee/{employee_id}/Revision/{revision_number}'.format(employer_id='employer_id_example', employee_id='employee_id_example', revision_number='revision_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_employee_secret(client):
    """Test case for delete_employee_secret

    Deletes employee secret
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/Employee/{employee_id}/Secret/{secret_id}'.format(employer_id='employer_id_example', employee_id='employee_id_example', secret_id='secret_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ae_assessment_from_employee_0(client):
    """Test case for get_ae_assessment_from_employee_0

    Get the auto enrolment assessment
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employee/{employee_id}/AEAssessment/{ae_assessment_id}'.format(employer_id='employer_id_example', employee_id='employee_id_example', ae_assessment_id='ae_assessment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ae_assessments_from_employee_0(client):
    """Test case for get_ae_assessments_from_employee_0

    Get the auto enrolment assessments
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employee/{employee_id}/AEAssessments'.format(employer_id='employer_id_example', employee_id='employee_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_employee_tags_0(client):
    """Test case for get_all_employee_tags_0

    Get all employee tags
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employees/Tags'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_commentaries_from_employee(client):
    """Test case for get_commentaries_from_employee

    Get links to all commentaries for the specified employee
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employee/{employee_id}/Commentaries'.format(employer_id='employer_id_example', employee_id='employee_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_commentary_from_employee(client):
    """Test case for get_commentary_from_employee

    Get commentary from employee
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employee/{employee_id}/Commentary/{commentary_id}'.format(employer_id='employer_id_example', employee_id='employee_id_example', commentary_id='commentary_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_commentary_from_pay_run_by_employee(client):
    """Test case for get_commentary_from_pay_run_by_employee

    Get commentary from payrun by specified employee.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/PaySchedule/{pay_schedule_id}/PayRun/{pay_run_id}/Employee/{employee_id}/Commentary'.format(employer_id='employer_id_example', pay_schedule_id='pay_schedule_id_example', pay_run_id='pay_run_id_example', employee_id='employee_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employee_by_effective_date(client):
    """Test case for get_employee_by_effective_date

    Get employee by effective date.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employee/{employee_id}/{effective_date}'.format(employer_id='employer_id_example', employee_id='employee_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employee_from_employer(client):
    """Test case for get_employee_from_employer

    Get employee from employer
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employee/{employee_id}'.format(employer_id='employer_id_example', employee_id='employee_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employee_revision_by_number(client):
    """Test case for get_employee_revision_by_number

    Gets the employee by revision number
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employee/{employee_id}/Revision/{revision_number}'.format(employer_id='employer_id_example', employee_id='employee_id_example', revision_number='revision_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employee_revision_summaries(client):
    """Test case for get_employee_revision_summaries

    Get all employee revision summaries
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employee/{employee_id}/Revisions/Summary'.format(employer_id='employer_id_example', employee_id='employee_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employee_revision_summary_by_number(client):
    """Test case for get_employee_revision_summary_by_number

    Gets the employee summary by revision number
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employee/{employee_id}/Revision/{revision_number}/Summary'.format(employer_id='employer_id_example', employee_id='employee_id_example', revision_number='revision_number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employee_revisions(client):
    """Test case for get_employee_revisions

    Get all employee revisions
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employee/{employee_id}/Revisions'.format(employer_id='employer_id_example', employee_id='employee_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employee_secret(client):
    """Test case for get_employee_secret

    Get employee secret
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employee/{employee_id}/Secret/{secret_id}'.format(employer_id='employer_id_example', employee_id='employee_id_example', secret_id='secret_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employee_secrets(client):
    """Test case for get_employee_secrets

    Get all employee secret links
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employee/{employee_id}/Secrets'.format(employer_id='employer_id_example', employee_id='employee_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employee_summaries_by_effective_date(client):
    """Test case for get_employee_summaries_by_effective_date

    Get employee summaries from employer at a given effective date.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employees/{effective_date}/Summary'.format(employer_id='employer_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employee_summaries_from_employer(client):
    """Test case for get_employee_summaries_from_employer

    Get employee summaries from employer.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employees/Summary'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employee_summary_by_effective_date(client):
    """Test case for get_employee_summary_by_effective_date

    Get employee summary by effective date.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employee/{employee_id}/{effective_date}/Summary'.format(employer_id='employer_id_example', employee_id='employee_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employee_summary_from_employer(client):
    """Test case for get_employee_summary_from_employer

    Get employee summary from employer
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employee/{employee_id}/Summary'.format(employer_id='employer_id_example', employee_id='employee_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employees_by_effective_date(client):
    """Test case for get_employees_by_effective_date

    Get employees from employer at a given effective date.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employees/{effective_date}'.format(employer_id='employer_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employees_from_employer(client):
    """Test case for get_employees_from_employer

    Get employees from employer.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employees'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employees_from_pay_run(client):
    """Test case for get_employees_from_pay_run

    Get employees from the pay run
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/PaySchedule/{pay_schedule_id}/PayRun/{pay_run_id}/Employees'.format(employer_id='employer_id_example', pay_schedule_id='pay_schedule_id_example', pay_run_id='pay_run_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employees_from_pay_schedule(client):
    """Test case for get_employees_from_pay_schedule

    Get all employees revisions from a pay schedule.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/PaySchedule/{pay_schedule_id}/Employees'.format(employer_id='employer_id_example', pay_schedule_id='pay_schedule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employees_from_pay_schedule_on_effective_date(client):
    """Test case for get_employees_from_pay_schedule_on_effective_date

    Get employees from a pay schedule on effective date.
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/PaySchedule/{pay_schedule_id}/Employees/{effective_date}'.format(employer_id='employer_id_example', pay_schedule_id='pay_schedule_id_example', effective_date='2013-10-20'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_employees_with_tag_0(client):
    """Test case for get_employees_with_tag_0

    Get employees with tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employees/Tag/{tag_id}'.format(employer_id='employer_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_runs_from_employee_0(client):
    """Test case for get_pay_runs_from_employee_0

    Gets the pay runs from the employee
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employee/{employee_id}/PayRuns'.format(employer_id='employer_id_example', employee_id='employee_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_employee(client):
    """Test case for patch_employee

    Patches the employee
    """
    body = {"Employee":{"AEAssessmentOverrideDate":"2000-01-23","DirectorshipAppointmentDate":"2000-01-23","LeaverReason":"Resigned","P45IssuedDate":"2000-01-23","NiNumber":"NiNumber","Address":{"Address4":"Address4","Address2":"Address2","Address3":"Address3","Country":"Country","Address1":"Address1","Postcode":"Postcode"},"IsAgencyWorker":True,"StarterDeclaration":"PreviouslyReported","Gender":"Unknown","HoursPerWeek":0.8008281904610115,"NextRevisionDate":"2000-01-23","StartDate":"2000-01-23","PaymentToANonIndividual":True,"EPM6":True,"IrregularEmployment":True,"MetaData":"{}","EmployeePartner":{"NiNumber":"NiNumber","FirstName":"FirstName","LastName":"LastName","Initials":"Initials","MiddleName":"MiddleName"},"PaySchedule":{"@title":"@title","@rel":"@rel","@href":"@href"},"OffPayrollWorker":True,"AEAssessmentOverride":"None","DateOfBirth":"2000-01-23","Territory":"UnitedKingdom","LeavingDate":"2000-01-23","Seconded":"NotSet","VeteranPeriodStartDate":"2000-01-23","FirstName":"FirstName","Title":"Title","BankAccount":{"Reference":"Reference","BranchName":"BranchName","SortCode":"SortCode","AccountName":"AccountName","AccountNumber":"AccountNumber"},"EEACitizen":True,"AEPostponementDate":"2000-01-23","Initials":"Initials","MiddleName":"MiddleName","Code":"Code","MaritalStatus":"NotSet","Revision":6,"OnStrike":True,"AEExclusionReasonCode":"OtherNotKnown","Deactivated":True,"NicLiability":"HasOtherJob","PassportNumber":"PassportNumber","PaymentMethod":"NotSet","Region":"NotSet","WorkingWeek":"None","LastName":"LastName","RuleExclusions":"None","EffectiveDate":"2000-01-23"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PATCH',
        path='/Employer/{employer_id}/Employee/{employee_id}'.format(employer_id='employer_id_example', employee_id='employee_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_employee_into_employer(client):
    """Test case for post_employee_into_employer

    Create a new Employee
    """
    body = {"Employee":{"AEAssessmentOverrideDate":"2000-01-23","DirectorshipAppointmentDate":"2000-01-23","LeaverReason":"Resigned","P45IssuedDate":"2000-01-23","NiNumber":"NiNumber","Address":{"Address4":"Address4","Address2":"Address2","Address3":"Address3","Country":"Country","Address1":"Address1","Postcode":"Postcode"},"IsAgencyWorker":True,"StarterDeclaration":"PreviouslyReported","Gender":"Unknown","HoursPerWeek":0.8008281904610115,"NextRevisionDate":"2000-01-23","StartDate":"2000-01-23","PaymentToANonIndividual":True,"EPM6":True,"IrregularEmployment":True,"MetaData":"{}","EmployeePartner":{"NiNumber":"NiNumber","FirstName":"FirstName","LastName":"LastName","Initials":"Initials","MiddleName":"MiddleName"},"PaySchedule":{"@title":"@title","@rel":"@rel","@href":"@href"},"OffPayrollWorker":True,"AEAssessmentOverride":"None","DateOfBirth":"2000-01-23","Territory":"UnitedKingdom","LeavingDate":"2000-01-23","Seconded":"NotSet","VeteranPeriodStartDate":"2000-01-23","FirstName":"FirstName","Title":"Title","BankAccount":{"Reference":"Reference","BranchName":"BranchName","SortCode":"SortCode","AccountName":"AccountName","AccountNumber":"AccountNumber"},"EEACitizen":True,"AEPostponementDate":"2000-01-23","Initials":"Initials","MiddleName":"MiddleName","Code":"Code","MaritalStatus":"NotSet","Revision":6,"OnStrike":True,"AEExclusionReasonCode":"OtherNotKnown","Deactivated":True,"NicLiability":"HasOtherJob","PassportNumber":"PassportNumber","PaymentMethod":"NotSet","Region":"NotSet","WorkingWeek":"None","LastName":"LastName","RuleExclusions":"None","EffectiveDate":"2000-01-23"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/Employer/{employer_id}/Employees'.format(employer_id='employer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_employee_secret(client):
    """Test case for post_employee_secret

    Create a new employee secret
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/Employer/{employer_id}/Employee/{employee_id}/Secrets'.format(employer_id='employer_id_example', employee_id='employee_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_employee_into_employer(client):
    """Test case for put_employee_into_employer

    Updates the Employee
    """
    body = {"Employee":{"AEAssessmentOverrideDate":"2000-01-23","DirectorshipAppointmentDate":"2000-01-23","LeaverReason":"Resigned","P45IssuedDate":"2000-01-23","NiNumber":"NiNumber","Address":{"Address4":"Address4","Address2":"Address2","Address3":"Address3","Country":"Country","Address1":"Address1","Postcode":"Postcode"},"IsAgencyWorker":True,"StarterDeclaration":"PreviouslyReported","Gender":"Unknown","HoursPerWeek":0.8008281904610115,"NextRevisionDate":"2000-01-23","StartDate":"2000-01-23","PaymentToANonIndividual":True,"EPM6":True,"IrregularEmployment":True,"MetaData":"{}","EmployeePartner":{"NiNumber":"NiNumber","FirstName":"FirstName","LastName":"LastName","Initials":"Initials","MiddleName":"MiddleName"},"PaySchedule":{"@title":"@title","@rel":"@rel","@href":"@href"},"OffPayrollWorker":True,"AEAssessmentOverride":"None","DateOfBirth":"2000-01-23","Territory":"UnitedKingdom","LeavingDate":"2000-01-23","Seconded":"NotSet","VeteranPeriodStartDate":"2000-01-23","FirstName":"FirstName","Title":"Title","BankAccount":{"Reference":"Reference","BranchName":"BranchName","SortCode":"SortCode","AccountName":"AccountName","AccountNumber":"AccountNumber"},"EEACitizen":True,"AEPostponementDate":"2000-01-23","Initials":"Initials","MiddleName":"MiddleName","Code":"Code","MaritalStatus":"NotSet","Revision":6,"OnStrike":True,"AEExclusionReasonCode":"OtherNotKnown","Deactivated":True,"NicLiability":"HasOtherJob","PassportNumber":"PassportNumber","PaymentMethod":"NotSet","Region":"NotSet","WorkingWeek":"None","LastName":"LastName","RuleExclusions":"None","EffectiveDate":"2000-01-23"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PUT',
        path='/Employer/{employer_id}/Employee/{employee_id}'.format(employer_id='employer_id_example', employee_id='employee_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_employee_secret(client):
    """Test case for put_employee_secret

    Create a new employee secret
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PUT',
        path='/Employer/{employer_id}/Employee/{employee_id}/Secret/{secret_id}'.format(employer_id='employer_id_example', employee_id='employee_id_example', secret_id='secret_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

