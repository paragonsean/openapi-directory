# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.shared_catalog_product_management_v1_assign_products_post_request import SharedCatalogProductManagementV1AssignProductsPostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_shared_catalog_product_management_v1_unassign_products_post(client):
    """Test case for shared_catalog_product_management_v1_unassign_products_post

    sharedCatalog/{id}/unassignProducts
    """
    body = openapi_server.SharedCatalogProductManagementV1AssignProductsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/sharedCatalog/{id}/unassignProducts'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

