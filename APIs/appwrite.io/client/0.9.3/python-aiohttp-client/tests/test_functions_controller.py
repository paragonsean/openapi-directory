# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.execution import Execution
from openapi_server.models.execution_list import ExecutionList
from openapi_server.models.functions_create_execution_request import FunctionsCreateExecutionRequest


pytestmark = pytest.mark.asyncio

async def test_functions_create_execution(client):
    """Test case for functions_create_execution

    Create Execution
    """
    body = openapi_server.FunctionsCreateExecutionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/functions/{function_id}/executions'.format(function_id='function_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functions_get_execution(client):
    """Test case for functions_get_execution

    Get Execution
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/functions/{function_id}/executions/{execution_id}'.format(function_id='function_id_example', execution_id='execution_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_functions_list_executions(client):
    """Test case for functions_list_executions

    List Executions
    """
    params = [('search', ''),
                    ('limit', 25),
                    ('offset', 0),
                    ('orderType', 'ASC')]
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/functions/{function_id}/executions'.format(function_id='function_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

