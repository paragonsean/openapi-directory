# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.execution_enum_status import ExecutionEnumStatus
from openapi_server.models.list_execution_response import ListExecutionResponse
from openapi_server.models.studio_v1_flow_execution import StudioV1FlowExecution


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_execution(client):
    """Test case for create_execution

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        '_from': '_from_example',
        'parameters': None,
        'to': 'to_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Flows/{flow_sid}/Executions'.format(flow_sid='flow_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_execution(client):
    """Test case for delete_execution

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Flows/{flow_sid}/Executions/{sid}'.format(flow_sid='flow_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_execution(client):
    """Test case for fetch_execution

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Flows/{flow_sid}/Executions/{sid}'.format(flow_sid='flow_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_execution(client):
    """Test case for list_execution

    
    """
    params = [('DateCreatedFrom', '2013-10-20T19:20:30+01:00'),
                    ('DateCreatedTo', '2013-10-20T19:20:30+01:00'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Flows/{flow_sid}/Executions'.format(flow_sid='flow_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_execution(client):
    """Test case for update_execution

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'status': openapi_server.ExecutionEnumStatus()
        }
    response = await client.request(
        method='POST',
        path='/v1/Flows/{flow_sid}/Executions/{sid}'.format(flow_sid='flow_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

