# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.pay_instruction import PayInstruction


pytestmark = pytest.mark.asyncio

async def test_delete_pay_instruction(client):
    """Test case for delete_pay_instruction

    Deletes a pay instruction
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='DELETE',
        path='/Employer/{employer_id}/Employee/{employee_id}/PayInstruction/{pay_instruction_id}'.format(employer_id='employer_id_example', employee_id='employee_id_example', pay_instruction_id='pay_instruction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_pay_instruction_tags_0(client):
    """Test case for get_all_pay_instruction_tags_0

    Get all pay instruction tags
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employee/{employee_id}/PayInstructions/Tags'.format(employer_id='employer_id_example', employee_id='employee_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_instruction_from_employee(client):
    """Test case for get_pay_instruction_from_employee

    Gets the specified pay instruction from the employee
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employee/{employee_id}/PayInstruction/{pay_instruction_id}'.format(employer_id='employer_id_example', employee_id='employee_id_example', pay_instruction_id='pay_instruction_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_instructions_from_employee(client):
    """Test case for get_pay_instructions_from_employee

    Gets the pay instructions from the specified employee
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employee/{employee_id}/PayInstructions'.format(employer_id='employer_id_example', employee_id='employee_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_pay_instructions_with_tag_0(client):
    """Test case for get_pay_instructions_with_tag_0

    Get pay instructions with tag
    """
    headers = { 
        'Accept': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='GET',
        path='/Employer/{employer_id}/Employee/{employee_id}/PayInstructions/Tag/{tag_id}'.format(employer_id='employer_id_example', employee_id='employee_id_example', tag_id='tag_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_pay_instruction(client):
    """Test case for patch_pay_instruction

    Sparse Update of a Pay Instruction
    """
    body = {"PayInstruction":{"StartDate":"2000-01-23","Description":"Description","EndDate":"2000-01-23","PayLineTag":"PayLineTag"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PATCH',
        path='/Employer/{employer_id}/Employee/{employee_id}/PayInstruction/{pay_instruction_id}'.format(employer_id='employer_id_example', employee_id='employee_id_example', pay_instruction_id='pay_instruction_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_pay_instruction(client):
    """Test case for post_pay_instruction

    Creates a new Pay Instruction
    """
    body = {"PayInstruction":{"StartDate":"2000-01-23","Description":"Description","EndDate":"2000-01-23","PayLineTag":"PayLineTag"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='POST',
        path='/Employer/{employer_id}/Employee/{employee_id}/PayInstructions'.format(employer_id='employer_id_example', employee_id='employee_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_pay_instruction(client):
    """Test case for put_pay_instruction

    Update a Pay Instruction
    """
    body = {"PayInstruction":{"StartDate":"2000-01-23","Description":"Description","EndDate":"2000-01-23","PayLineTag":"PayLineTag"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'authorization': 'Auto',
        'api_version': 'default',
    }
    response = await client.request(
        method='PUT',
        path='/Employer/{employer_id}/Employee/{employee_id}/PayInstruction/{pay_instruction_id}'.format(employer_id='employer_id_example', employee_id='employee_id_example', pay_instruction_id='pay_instruction_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

