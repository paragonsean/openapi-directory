# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_attribute_set_management_v1_create_post_request import CatalogAttributeSetManagementV1CreatePostRequest
from openapi_server.models.eav_data_attribute_set_interface import EavDataAttributeSetInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_catalog_attribute_set_management_v1_create_post(client):
    """Test case for catalog_attribute_set_management_v1_create_post

    products/attribute-sets
    """
    body = openapi_server.CatalogAttributeSetManagementV1CreatePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/products/attribute-sets',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

