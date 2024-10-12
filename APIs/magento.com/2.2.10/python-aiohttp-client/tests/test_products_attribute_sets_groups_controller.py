# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_product_attribute_group_repository_v1_save_post_request import CatalogProductAttributeGroupRepositoryV1SavePostRequest
from openapi_server.models.eav_data_attribute_group_interface import EavDataAttributeGroupInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_catalog_product_attribute_group_repository_v1_save_post(client):
    """Test case for catalog_product_attribute_group_repository_v1_save_post

    products/attribute-sets/groups
    """
    body = openapi_server.CatalogProductAttributeGroupRepositoryV1SavePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/products/attribute-sets/groups',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

