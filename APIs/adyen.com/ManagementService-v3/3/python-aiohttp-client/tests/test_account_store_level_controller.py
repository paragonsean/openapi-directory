# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.list_stores_response import ListStoresResponse
from openapi_server.models.rest_service_error import RestServiceError
from openapi_server.models.store import Store
from openapi_server.models.store_creation_request import StoreCreationRequest
from openapi_server.models.store_creation_with_merchant_code_request import StoreCreationWithMerchantCodeRequest
from openapi_server.models.update_store_request import UpdateStoreRequest


pytestmark = pytest.mark.asyncio

async def test_get_merchants_merchant_id_stores(client):
    """Test case for get_merchants_merchant_id_stores

    Get a list of stores
    """
    params = [('pageNumber', 56),
                    ('pageSize', 56),
                    ('reference', 'reference_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/merchants/{merchant_id}/stores'.format(merchant_id='merchant_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_merchants_merchant_id_stores_store_id(client):
    """Test case for get_merchants_merchant_id_stores_store_id

    Get a store
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/merchants/{merchant_id}/stores/{store_id}'.format(merchant_id='merchant_id_example', store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_stores(client):
    """Test case for get_stores

    Get a list of stores
    """
    params = [('pageNumber', 56),
                    ('pageSize', 56),
                    ('reference', 'reference_example'),
                    ('merchantId', 'merchant_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/stores',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_stores_store_id(client):
    """Test case for get_stores_store_id

    Get a store
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v3/stores/{store_id}'.format(store_id='store_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_merchants_merchant_id_stores_store_id(client):
    """Test case for patch_merchants_merchant_id_stores_store_id

    Update a store
    """
    body = {"externalReferenceId":"externalReferenceId","address":{"stateOrProvince":"stateOrProvince","city":"city","postalCode":"postalCode","line3":"line3","line2":"line2","line1":"line1"},"phoneNumber":"phoneNumber","description":"description","businessLineIds":["businessLineIds","businessLineIds"],"splitConfiguration":{"balanceAccountId":"balanceAccountId","splitConfigurationId":"splitConfigurationId"},"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v3/merchants/{merchant_id}/stores/{store_id}'.format(merchant_id='merchant_id_example', store_id='store_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_stores_store_id(client):
    """Test case for patch_stores_store_id

    Update a store
    """
    body = {"externalReferenceId":"externalReferenceId","address":{"stateOrProvince":"stateOrProvince","city":"city","postalCode":"postalCode","line3":"line3","line2":"line2","line1":"line1"},"phoneNumber":"phoneNumber","description":"description","businessLineIds":["businessLineIds","businessLineIds"],"splitConfiguration":{"balanceAccountId":"balanceAccountId","splitConfigurationId":"splitConfigurationId"},"status":"active"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v3/stores/{store_id}'.format(store_id='store_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_merchants_merchant_id_stores(client):
    """Test case for post_merchants_merchant_id_stores

    Create a store
    """
    body = {"externalReferenceId":"externalReferenceId","reference":"reference","address":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","postalCode":"postalCode","line3":"line3","line2":"line2","line1":"line1"},"phoneNumber":"phoneNumber","description":"description","businessLineIds":["businessLineIds","businessLineIds"],"shopperStatement":"shopperStatement","splitConfiguration":{"balanceAccountId":"balanceAccountId","splitConfigurationId":"splitConfigurationId"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/merchants/{merchant_id}/stores'.format(merchant_id='merchant_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_stores(client):
    """Test case for post_stores

    Create a store
    """
    body = {"externalReferenceId":"externalReferenceId","reference":"reference","address":{"country":"country","stateOrProvince":"stateOrProvince","city":"city","postalCode":"postalCode","line3":"line3","line2":"line2","line1":"line1"},"phoneNumber":"phoneNumber","merchantId":"merchantId","description":"description","businessLineIds":["businessLineIds","businessLineIds"],"shopperStatement":"shopperStatement","splitConfiguration":{"balanceAccountId":"balanceAccountId","splitConfigurationId":"splitConfigurationId"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v3/stores',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

