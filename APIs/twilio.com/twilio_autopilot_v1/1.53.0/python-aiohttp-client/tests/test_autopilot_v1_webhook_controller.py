# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.autopilot_v1_assistant_webhook import AutopilotV1AssistantWebhook
from openapi_server.models.list_webhook_response import ListWebhookResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_webhook(client):
    """Test case for create_webhook

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'events': 'events_example',
        'unique_name': 'unique_name_example',
        'webhook_method': 'webhook_method_example',
        'webhook_url': 'webhook_url_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Assistants/{assistant_sid}/Webhooks'.format(assistant_sid='assistant_sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_webhook(client):
    """Test case for delete_webhook

    
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/Assistants/{assistant_sid}/Webhooks/{sid}'.format(assistant_sid='assistant_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_fetch_webhook(client):
    """Test case for fetch_webhook

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Assistants/{assistant_sid}/Webhooks/{sid}'.format(assistant_sid='assistant_sid_example', sid='sid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_webhook(client):
    """Test case for list_webhook

    
    """
    params = [('PageSize', 56),
                    ('Page', 56),
                    ('PageToken', 'page_token_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/Assistants/{assistant_sid}/Webhooks'.format(assistant_sid='assistant_sid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_update_webhook(client):
    """Test case for update_webhook

    
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    data = {
        'events': 'events_example',
        'unique_name': 'unique_name_example',
        'webhook_method': 'webhook_method_example',
        'webhook_url': 'webhook_url_example'
        }
    response = await client.request(
        method='POST',
        path='/v1/Assistants/{assistant_sid}/Webhooks/{sid}'.format(assistant_sid='assistant_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

