# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.temando_shipping_collection_point_cart_collection_point_management_v1_select_collection_point_post_request import TemandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_temando_shipping_collection_point_guest_cart_collection_point_management_v1_select_collection_point_post(client):
    """Test case for temando_shipping_collection_point_guest_cart_collection_point_management_v1_select_collection_point_post

    guest-carts/{cartId}/collection-point/select
    """
    body = openapi_server.TemandoShippingCollectionPointCartCollectionPointManagementV1SelectCollectionPointPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/default/V1/guest-carts/{cart_id}/collection-point/select'.format(cart_id='cart_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

