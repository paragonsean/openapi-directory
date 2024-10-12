# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.autopilot_v1_assistant_query import AutopilotV1AssistantQuery
from openapi_server.models.list_query_response import ListQueryResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_query(client):
    """Test case for create_query

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'language': 'language_example',
        'model_build': 'model_build_example',
        'query': 'query_example',
        'tasks': 'tasks_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Assistants/{assistant_sid}/Queries'.format(assistant_sid='assistant_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_query(client):
    """Test case for delete_query

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Assistants/{assistant_sid}/Queries/{sid}'.format(assistant_sid='assistant_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_query(client):
    """Test case for fetch_query

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Assistants/{assistant_sid}/Queries/{sid}'.format(assistant_sid='assistant_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_query(client):
    """Test case for list_query

    
    """
    params = [('Language', 'language_example'),
                    ('ModelBuild', 'model_build_example'),
                    ('Status', 'status_example'),
                    ('DialogueSid', 'dialogue_sid_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Assistants/{assistant_sid}/Queries'.format(assistant_sid='assistant_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_query(client):
    """Test case for update_query

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'sample_sid': 'sample_sid_example',
        'status': 'status_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Assistants/{assistant_sid}/Queries/{sid}'.format(assistant_sid='assistant_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

