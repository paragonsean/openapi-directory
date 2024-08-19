# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_merchant_webhook_request import CreateMerchantWebhookRequest
from openapi_server.models.generate_hmac_key_response import GenerateHmacKeyResponse
from openapi_server.models.list_webhooks_response import ListWebhooksResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.test_webhook_request import TestWebhookRequest
from openapi_server.models.test_webhook_response import TestWebhookResponse
from openapi_server.models.update_merchant_webhook_request import UpdateMerchantWebhookRequest
from openapi_server.models.webhook import Webhook


pytestmark = pytest.mark.asyncio

async def test_delete_merchants_merchant_id_webhooks_webhook_id(client):
    """Test case for delete_merchants_merchant_id_webhooks_webhook_id

    Remove a webhook
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/merchants/{merchant_id}/webhooks/{webhook_id}'.format(merchant_id='merchant_id_example', webhook_id='webhook_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_merchants_merchant_id_webhooks(client):
    """Test case for get_merchants_merchant_id_webhooks

    List all webhooks
    """
    params = [('pageNumber', 56),
                    ('pageSize', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/merchants/{merchant_id}/webhooks'.format(merchant_id='merchant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_merchants_merchant_id_webhooks_webhook_id(client):
    """Test case for get_merchants_merchant_id_webhooks_webhook_id

    Get a webhook
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/merchants/{merchant_id}/webhooks/{webhook_id}'.format(merchant_id='merchant_id_example', webhook_id='webhook_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_merchants_merchant_id_webhooks_webhook_id(client):
    """Test case for patch_merchants_merchant_id_webhooks_webhook_id

    Update a webhook
    """
    body = {"communicationFormat":"http","sslVersion":"HTTP","acceptsUntrustedRootCertificate":True,"active":True,"description":"description","acceptsSelfSignedCertificate":True,"url":"url","password":"password","additionalSettings":{"includeEventCodes":["includeEventCodes","includeEventCodes"],"properties":{"key":True}},"acceptsExpiredCertificate":True,"networkType":"local","populateSoapActionHeader":True,"username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/merchants/{merchant_id}/webhooks/{webhook_id}'.format(merchant_id='merchant_id_example', webhook_id='webhook_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_merchants_merchant_id_webhooks(client):
    """Test case for post_merchants_merchant_id_webhooks

    Set up a webhook
    """
    body = {"communicationFormat":"http","sslVersion":"HTTP","acceptsUntrustedRootCertificate":True,"active":True,"description":"description","acceptsSelfSignedCertificate":True,"type":"type","url":"url","password":"password","additionalSettings":{"includeEventCodes":["includeEventCodes","includeEventCodes"],"properties":{"key":True}},"acceptsExpiredCertificate":True,"networkType":"local","populateSoapActionHeader":True,"username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/merchants/{merchant_id}/webhooks'.format(merchant_id='merchant_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_merchants_merchant_id_webhooks_webhook_id_generate_hmac(client):
    """Test case for post_merchants_merchant_id_webhooks_webhook_id_generate_hmac

    Generate an HMAC key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/merchants/{merchant_id}/webhooks/{webhook_id}/generateHmac'.format(merchant_id='merchant_id_example', webhook_id='webhook_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_merchants_merchant_id_webhooks_webhook_id_test(client):
    """Test case for post_merchants_merchant_id_webhooks_webhook_id_test

    Test a webhook
    """
    body = {"notification":{"eventCode":"eventCode","reason":"reason","amount":{"currency":"currency","value":0},"success":True,"paymentMethod":"paymentMethod","merchantReference":"merchantReference","eventDate":"2000-01-23T04:56:07.000+00:00"},"types":["types","types"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/merchants/{merchant_id}/webhooks/{webhook_id}/test'.format(merchant_id='merchant_id_example', webhook_id='webhook_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

