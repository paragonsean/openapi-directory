# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_data_price_update_result_interface import CatalogDataPriceUpdateResultInterface
from openapi_server.models.catalog_tier_price_storage_v1_replace_put_request import CatalogTierPriceStorageV1ReplacePutRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_catalog_tier_price_storage_v1_replace_put(client):
    """Test case for catalog_tier_price_storage_v1_replace_put

    products/tier-prices
    """
    body = openapi_server.CatalogTierPriceStorageV1ReplacePutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/products/tier-prices',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_catalog_tier_price_storage_v1_update_post(client):
    """Test case for catalog_tier_price_storage_v1_update_post

    products/tier-prices
    """
    body = openapi_server.CatalogTierPriceStorageV1ReplacePutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/products/tier-prices',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

