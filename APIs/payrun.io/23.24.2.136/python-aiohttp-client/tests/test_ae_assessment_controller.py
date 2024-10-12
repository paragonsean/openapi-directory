# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.ae_assessment import AEAssessment
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection


pytestmark = pytest.mark.asyncio

async def test_delete_ae_assessment(client):
    """Test case for delete_ae_assessment

    Delete auto enrolment assessment
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/Employee/{employee_id}/AEAssessment/{ae_assessment_id}'.format(employer_id='employer_id_example', employee_id='employee_id_example', ae_assessment_id='ae_assessment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ae_assessment_from_employee(client):
    """Test case for get_ae_assessment_from_employee

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

async def test_get_ae_assessments_from_employee(client):
    """Test case for get_ae_assessments_from_employee

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

async def test_get_ae_assessments_from_pay_run(client):
    """Test case for get_ae_assessments_from_pay_run

    Get the auto enrolment assessments
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/PaySchedule/{pay_schedule_id}/PayRun/{pay_run_id}/AEAssessments'.format(employer_id='employer_id_example', pay_schedule_id='pay_schedule_id_example', pay_run_id='pay_run_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_new_ae_assessment(client):
    """Test case for post_new_ae_assessment

    Insert new auto enrolment assessment
    """
    body = {"AEAssessment":{"AssessmentOverride":"None","IsMemberOfAlternativePensionScheme":True,"QualifyingEarnings":6.027456183070403,"OptOutWindowEndDate":"2000-01-23","AssessmentDate":"2000-01-23","AssessmentCode":"Excluded","ReenrolmentDate":"2000-01-23","TaxPeriod":5,"StatePensionDate":"2000-01-23","AssessmentEvent":"NonEnrolmentEvent","StatePensionAge":1,"AssessmentResult":"Inconclusive","Age":0,"TaxYear":5}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/Employer/{employer_id}/Employee/{employee_id}/AEAssessments'.format(employer_id='employer_id_example', employee_id='employee_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_new_ae_assessment(client):
    """Test case for put_new_ae_assessment

    Insert new auto enrolment assessment
    """
    body = {"AEAssessment":{"AssessmentOverride":"None","IsMemberOfAlternativePensionScheme":True,"QualifyingEarnings":6.027456183070403,"OptOutWindowEndDate":"2000-01-23","AssessmentDate":"2000-01-23","AssessmentCode":"Excluded","ReenrolmentDate":"2000-01-23","TaxPeriod":5,"StatePensionDate":"2000-01-23","AssessmentEvent":"NonEnrolmentEvent","StatePensionAge":1,"AssessmentResult":"Inconclusive","Age":0,"TaxYear":5}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PUT',
        path='/Employer/{employer_id}/Employee/{employee_id}/AEAssessment/{ae_assessment_id}'.format(employer_id='employer_id_example', employee_id='employee_id_example', ae_assessment_id='ae_assessment_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

