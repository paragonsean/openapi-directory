# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.commentary import Commentary
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.pay_run import PayRun


pytestmark = pytest.mark.asyncio

async def test_delete_pay_run(client):
    """Test case for delete_pay_run

    Deletes a pay run
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/PaySchedule/{pay_schedule_id}/PayRun/{pay_run_id}'.format(employer_id='employer_id_example', pay_schedule_id='pay_schedule_id_example', pay_run_id='pay_run_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_pay_run_employee(client):
    """Test case for delete_pay_run_employee

    Deletes a pay run employee
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/PaySchedule/{pay_schedule_id}/PayRun/{pay_run_id}/Employee/{employee_id}'.format(employer_id='employer_id_example', pay_schedule_id='pay_schedule_id_example', pay_run_id='pay_run_id_example', employee_id='employee_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ae_assessments_from_pay_run_0(client):
    """Test case for get_ae_assessments_from_pay_run_0

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

async def test_get_all_pay_run_tags_0(client):
    """Test case for get_all_pay_run_tags_0

    Get all pay run tags
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/PaySchedule/{pay_schedule_id}/PayRuns/Tags'.format(employer_id='employer_id_example', pay_schedule_id='pay_schedule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_commentaries_from_pay_run(client):
    """Test case for get_commentaries_from_pay_run

    Get links to all commentaries for the specified pay run
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/PaySchedule/{pay_schedule_id}/PayRun/{pay_run_id}/Commentaries'.format(employer_id='employer_id_example', pay_schedule_id='pay_schedule_id_example', pay_run_id='pay_run_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_commentary_from_pay_run_by_employee_0(client):
    """Test case for get_commentary_from_pay_run_by_employee_0

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

async def test_get_employees_from_pay_run_0(client):
    """Test case for get_employees_from_pay_run_0

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

async def test_get_pay_run_from_pay_schedule(client):
    """Test case for get_pay_run_from_pay_schedule

    Gets the pay run from the pay schedule
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/PaySchedule/{pay_schedule_id}/PayRun/{pay_run_id}'.format(employer_id='employer_id_example', pay_schedule_id='pay_schedule_id_example', pay_run_id='pay_run_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_runs_from_employee(client):
    """Test case for get_pay_runs_from_employee

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

async def test_get_pay_runs_from_pay_schedule(client):
    """Test case for get_pay_runs_from_pay_schedule

    Gets the pay runs from the pay schedule
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/PaySchedule/{pay_schedule_id}/PayRuns'.format(employer_id='employer_id_example', pay_schedule_id='pay_schedule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_runs_with_tag_0(client):
    """Test case for get_pay_runs_with_tag_0

    Get pay runs with tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/PaySchedule/{pay_schedule_id}/PayRuns/Tag/{tag_id}'.format(employer_id='employer_id_example', pay_schedule_id='pay_schedule_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_report_lines_from_pay_run_0(client):
    """Test case for get_report_lines_from_pay_run_0

    Gets the report lines from the specified pay run
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/PaySchedule/{pay_schedule_id}/PayRun/{pay_run_id}/ReportLines'.format(employer_id='employer_id_example', pay_schedule_id='pay_schedule_id_example', pay_run_id='pay_run_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

