# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.report_line import ReportLine


pytestmark = pytest.mark.asyncio

async def test_get_report_line_from_employer(client):
    """Test case for get_report_line_from_employer

    Gets the specified report line from the employer
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/ReportLine/{report_line_id}'.format(employer_id='employer_id_example', report_line_id='report_line_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_report_lines_from_employer(client):
    """Test case for get_report_lines_from_employer

    Gets the report lines from the specified employer
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/ReportLines'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_report_lines_from_pay_run(client):
    """Test case for get_report_lines_from_pay_run

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

