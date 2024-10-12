# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.pay_line import PayLine


pytestmark = pytest.mark.asyncio

async def test_get_all_pay_line_tags_0(client):
    """Test case for get_all_pay_line_tags_0

    Get all pay line tags
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employee/{employee_id}/PayLines/Tags'.format(employer_id='employer_id_example', employee_id='employee_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_line_from_employee(client):
    """Test case for get_pay_line_from_employee

    Gets the specified pay line from the employee
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employee/{employee_id}/PayLine/{pay_line_id}'.format(employer_id='employer_id_example', employee_id='employee_id_example', pay_line_id='pay_line_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_lines_from_employee(client):
    """Test case for get_pay_lines_from_employee

    Gets the pay lines from the specified employee
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employee/{employee_id}/PayLines'.format(employer_id='employer_id_example', employee_id='employee_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_lines_from_pay_run(client):
    """Test case for get_pay_lines_from_pay_run

    Gets the pay lines from the specified pay run
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/PaySchedule/{pay_schedule_id}/PayRun/{pay_run_id}/PayLines'.format(employer_id='employer_id_example', pay_schedule_id='pay_schedule_id_example', pay_run_id='pay_run_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_lines_with_tag_0(client):
    """Test case for get_pay_lines_with_tag_0

    Get pay lines with tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employee/{employee_id}/PayLines/Tag/{tag_id}'.format(employer_id='employer_id_example', employee_id='employee_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

