# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_webhook_request_body import AddWebhookRequestBody
from openapi_server.models.empty_response import EmptyResponse
from openapi_server.models.update_webhook_request_body import UpdateWebhookRequestBody
from openapi_server.models.webhook_collection_response import WebhookCollectionResponse
from openapi_server.models.webhook_response import WebhookResponse


pytestmark = pytest.mark.asyncio

async def test_add_webhook(client):
    """Test case for add_webhook

    Add A New Webhook
    """
    body = {"responseVersion":"v2","resource":"/uploads-folder","endpointUrl":"https://example.com/webhook","triggers":{"shares":{"formSubmit":True},"resources":{"download":True,"move":True,"extract":True,"compress":True,"rename":True,"upload":True,"copy":True,"createFolder":True,"delete":True}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/webhooks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_webhook(client):
    """Test case for delete_webhook

    Delete a webhook
    """
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/webhooks/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_webhook_by_id(client):
    """Test case for get_webhook_by_id

    Get info for a webhook
    """
    params = [('include', 'include_example')]
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/webhooks/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_wehooks_list(client):
    """Test case for get_wehooks_list

    Get Webhooks List
    """
    params = [('include', 'include_example'),
                    ('offset', 100),
                    ('limit', 10)]
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/webhooks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_regenerate_webhook_token(client):
    """Test case for regenerate_webhook_token

    Regenerate security token
    """
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/webhooks/regenerate-token/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_resend_webhook_activity_entry(client):
    """Test case for resend_webhook_activity_entry

    Resend a webhook message
    """
    headers = { 
        'Accept': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/webhooks/resend/{activity_id}'.format(activity_id='activity_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_webhook(client):
    """Test case for update_webhook

    Update a webhook
    """
    body = {"responseVersion":"v1","resource":"/newfolder","endpointUrl":"https://example.com/new-endpoint","triggers":{"shares":{"formSubmit":True},"resources":{"download":True,"move":True,"extract":True,"compress":True,"rename":True,"upload":True,"copy":True,"createFolder":True,"delete":True}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ev_api_key': 'ev_api_key_example',
        'ev_access_token': '5dc97cc607985eb8da033220e7447647e7915fbf73808',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/webhooks/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

