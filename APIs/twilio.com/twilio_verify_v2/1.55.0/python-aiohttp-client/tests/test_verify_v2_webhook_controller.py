# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_webhook_response import ListWebhookResponse
from openapi_server.models.verify_v2_service_webhook import VerifyV2ServiceWebhook
from openapi_server.models.webhook_enum_status import WebhookEnumStatus
from openapi_server.models.webhook_enum_version import WebhookEnumVersion


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
        'event_types': ['event_types_example'],
        'friendly_name': 'friendly_name_example',
        'status': openapi_server.WebhookEnumStatus(),
        'version': openapi_server.WebhookEnumVersion(),
        'webhook_url': 'webhook_url_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/Webhooks'.format(service_sid='service_sid_example'),
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
        path='/v2/Services/{service_sid}/Webhooks/{sid}'.format(service_sid='service_sid_example', sid='sid_example'),
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
        path='/v2/Services/{service_sid}/Webhooks/{sid}'.format(service_sid='service_sid_example', sid='sid_example'),
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
        path='/v2/Services/{service_sid}/Webhooks'.format(service_sid='service_sid_example'),
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
        'event_types': ['event_types_example'],
        'friendly_name': 'friendly_name_example',
        'status': openapi_server.WebhookEnumStatus(),
        'version': openapi_server.WebhookEnumVersion(),
        'webhook_url': 'webhook_url_example'
        }
    response = await client.request(
        method='POST',
        path='/v2/Services/{service_sid}/Webhooks/{sid}'.format(service_sid='service_sid_example', sid='sid_example'),
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

