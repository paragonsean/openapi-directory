# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_cost_storage_v1_update_post_request import CatalogCostStorageV1UpdatePostRequest
from openapi_server.models.catalog_data_price_update_result_interface import CatalogDataPriceUpdateResultInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_catalog_cost_storage_v1_update_post(client):
    """Test case for catalog_cost_storage_v1_update_post

    products/cost
    """
    body = openapi_server.CatalogCostStorageV1UpdatePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/products/cost',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

