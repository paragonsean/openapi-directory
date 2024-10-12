# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.reporting_instruction import ReportingInstruction


pytestmark = pytest.mark.asyncio

async def test_delete_reporting_instruction(client):
    """Test case for delete_reporting_instruction

    Deletes a reporting instruction
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/ReportingInstruction/{reporting_instruction_id}'.format(employer_id='employer_id_example', reporting_instruction_id='reporting_instruction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reporting_instruction_from_employer(client):
    """Test case for get_reporting_instruction_from_employer

    Gets the specified reporting instruction from the employer
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/ReportingInstruction/{reporting_instruction_id}'.format(employer_id='employer_id_example', reporting_instruction_id='reporting_instruction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reporting_instructions_from_employer(client):
    """Test case for get_reporting_instructions_from_employer

    Gets the reporting instructions from the specified employer
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/ReportingInstructions'.format(employer_id='employer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_reporting_instruction(client):
    """Test case for post_reporting_instruction

    Creates a new Reporting Instruction
    """
    body = {"ReportingInstruction":{"StartDate":"2000-01-23","TaxMonth":0,"Value":1.4658129805029452,"EndDate":"2000-01-23","TaxYear":6}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/Employer/{employer_id}/ReportingInstructions'.format(employer_id='employer_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_reporting_instruction(client):
    """Test case for put_reporting_instruction

    Update a reporting Instruction
    """
    body = {"ReportingInstruction":{"StartDate":"2000-01-23","TaxMonth":0,"Value":1.4658129805029452,"EndDate":"2000-01-23","TaxYear":6}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PUT',
        path='/Employer/{employer_id}/ReportingInstruction/{reporting_instruction_id}'.format(employer_id='employer_id_example', reporting_instruction_id='reporting_instruction_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

