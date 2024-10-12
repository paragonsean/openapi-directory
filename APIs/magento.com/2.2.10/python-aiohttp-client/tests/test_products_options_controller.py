# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_data_product_custom_option_interface import CatalogDataProductCustomOptionInterface
from openapi_server.models.catalog_product_custom_option_repository_v1_save_post_request import CatalogProductCustomOptionRepositoryV1SavePostRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_catalog_product_custom_option_repository_v1_save_post(client):
    """Test case for catalog_product_custom_option_repository_v1_save_post

    products/options
    """
    body = openapi_server.CatalogProductCustomOptionRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/products/options',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

