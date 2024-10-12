# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_company_webhook_request import CreateCompanyWebhookRequest
from openapi_server.models.generate_hmac_key_response import GenerateHmacKeyResponse
from openapi_server.models.list_webhooks_response import ListWebhooksResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.test_company_webhook_request import TestCompanyWebhookRequest
from openapi_server.models.test_webhook_response import TestWebhookResponse
from openapi_server.models.update_company_webhook_request import UpdateCompanyWebhookRequest
from openapi_server.models.webhook import Webhook


pytestmark = pytest.mark.asyncio

async def test_delete_companies_company_id_webhooks_webhook_id(client):
    """Test case for delete_companies_company_id_webhooks_webhook_id

    Remove a webhook
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v3/companies/{company_id}/webhooks/{webhook_id}'.format(company_id='company_id_example', webhook_id='webhook_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_companies_company_id_webhooks(client):
    """Test case for get_companies_company_id_webhooks

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
        path='/v3/companies/{company_id}/webhooks'.format(company_id='company_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_companies_company_id_webhooks_webhook_id(client):
    """Test case for get_companies_company_id_webhooks_webhook_id

    Get a webhook
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/companies/{company_id}/webhooks/{webhook_id}'.format(company_id='company_id_example', webhook_id='webhook_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_companies_company_id_webhooks_webhook_id(client):
    """Test case for patch_companies_company_id_webhooks_webhook_id

    Update a webhook
    """
    body = {"communicationFormat":"http","acceptsUntrustedRootCertificate":True,"filterMerchantAccountType":"allAccounts","filterMerchantAccounts":["filterMerchantAccounts","filterMerchantAccounts"],"active":True,"description":"description","acceptsSelfSignedCertificate":True,"url":"url","password":"password","additionalSettings":{"includeEventCodes":["includeEventCodes","includeEventCodes"],"properties":{"key":True}},"acceptsExpiredCertificate":True,"encryptionProtocol":"HTTP","networkType":"local","populateSoapActionHeader":True,"username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v3/companies/{company_id}/webhooks/{webhook_id}'.format(company_id='company_id_example', webhook_id='webhook_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_companies_company_id_webhooks(client):
    """Test case for post_companies_company_id_webhooks

    Set up a webhook
    """
    body = {"communicationFormat":"http","acceptsUntrustedRootCertificate":True,"filterMerchantAccountType":"allAccounts","filterMerchantAccounts":["filterMerchantAccounts","filterMerchantAccounts"],"active":True,"description":"description","acceptsSelfSignedCertificate":True,"type":"type","url":"url","password":"password","additionalSettings":{"includeEventCodes":["includeEventCodes","includeEventCodes"],"properties":{"key":True}},"acceptsExpiredCertificate":True,"encryptionProtocol":"HTTP","networkType":"local","populateSoapActionHeader":True,"username":"username"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/companies/{company_id}/webhooks'.format(company_id='company_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_companies_company_id_webhooks_webhook_id_generate_hmac(client):
    """Test case for post_companies_company_id_webhooks_webhook_id_generate_hmac

    Generate an HMAC key
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/companies/{company_id}/webhooks/{webhook_id}/generateHmac'.format(company_id='company_id_example', webhook_id='webhook_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_companies_company_id_webhooks_webhook_id_test(client):
    """Test case for post_companies_company_id_webhooks_webhook_id_test

    Test a webhook
    """
    body = {"notification":{"eventCode":"eventCode","reason":"reason","amount":{"currency":"currency","value":0},"success":True,"paymentMethod":"paymentMethod","merchantReference":"merchantReference","eventDate":"2000-01-23T04:56:07.000+00:00"},"types":["types","types"],"merchantIds":["merchantIds","merchantIds"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/companies/{company_id}/webhooks/{webhook_id}/test'.format(company_id='company_id_example', webhook_id='webhook_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

