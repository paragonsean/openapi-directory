# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.autopilot_v1_assistant_task_sample import AutopilotV1AssistantTaskSample
from openapi_server.models.list_sample_response import ListSampleResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_sample(client):
    """Test case for create_sample

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'language': 'language_example',
        'source_channel': 'source_channel_example',
        'tagged_text': 'tagged_text_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Samples'.format(assistant_sid='assistant_sid_example', task_sid='task_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_sample(client):
    """Test case for delete_sample

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Samples/{sid}'.format(assistant_sid='assistant_sid_example', task_sid='task_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_sample(client):
    """Test case for fetch_sample

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Samples/{sid}'.format(assistant_sid='assistant_sid_example', task_sid='task_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_sample(client):
    """Test case for list_sample

    
    """
    params = [('Language', 'language_example'),
                    ('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Samples'.format(assistant_sid='assistant_sid_example', task_sid='task_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_sample(client):
    """Test case for update_sample

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'language': 'language_example',
        'source_channel': 'source_channel_example',
        'tagged_text': 'tagged_text_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Assistants/{assistant_sid}/Tasks/{task_sid}/Samples/{sid}'.format(assistant_sid='assistant_sid_example', task_sid='task_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

