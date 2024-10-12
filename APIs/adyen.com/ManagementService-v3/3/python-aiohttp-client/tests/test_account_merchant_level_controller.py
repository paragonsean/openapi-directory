# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_merchant_request import CreateMerchantRequest
from openapi_server.models.create_merchant_response import CreateMerchantResponse
from openapi_server.models.list_merchant_response import ListMerchantResponse
from openapi_server.models.merchant import Merchant
from openapi_server.models.request_activation_response import RequestActivationResponse
from openapi_server.models.rest_service_error import RestServiceError


pytestmark = pytest.mark.asyncio

async def test_get_merchants(client):
    """Test case for get_merchants

    Get a list of merchant accounts
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
        path='/v3/merchants',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_merchants_merchant_id(client):
    """Test case for get_merchants_merchant_id

    Get a merchant account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/merchants/{merchant_id}'.format(merchant_id='merchant_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_merchants(client):
    """Test case for post_merchants

    Create a merchant account
    """
    body = {"reference":"reference","salesChannels":["salesChannels","salesChannels"],"companyId":"companyId","pricingPlan":"pricingPlan","legalEntityId":"legalEntityId","description":"description","businessLineId":"businessLineId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/merchants',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_merchants_merchant_id_activate(client):
    """Test case for post_merchants_merchant_id_activate

    Request to activate a merchant account
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/merchants/{merchant_id}/activate'.format(merchant_id='merchant_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

