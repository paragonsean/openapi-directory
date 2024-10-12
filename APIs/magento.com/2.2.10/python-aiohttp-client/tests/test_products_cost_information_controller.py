# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_base_price_storage_v1_get_post_request import CatalogBasePriceStorageV1GetPostRequest
from openapi_server.models.catalog_data_cost_interface import CatalogDataCostInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_catalog_cost_storage_v1_get_post(client):
    """Test case for catalog_cost_storage_v1_get_post

    products/cost-information
    """
    body = openapi_server.CatalogBasePriceStorageV1GetPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/products/cost-information',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

