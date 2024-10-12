# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.catalog_product_attribute_management_v1_assign_post_request import CatalogProductAttributeManagementV1AssignPostRequest
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_catalog_product_attribute_management_v1_assign_post(client):
    """Test case for catalog_product_attribute_management_v1_assign_post

    products/attribute-sets/attributes
    """
    body = openapi_server.CatalogProductAttributeManagementV1AssignPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/products/attribute-sets/attributes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

