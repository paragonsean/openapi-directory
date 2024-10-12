# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.temando_shipping_collection_point_cart_collection_point_management_v1_save_search_request_put_request import TemandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest
from openapi_server.models.temando_shipping_data_collection_point_search_request_interface import TemandoShippingDataCollectionPointSearchRequestInterface


pytestmark = pytest.mark.asyncio

async def test_temando_shipping_collection_point_guest_cart_collection_point_management_v1_delete_search_request_delete(client):
    """Test case for temando_shipping_collection_point_guest_cart_collection_point_management_v1_delete_search_request_delete

    guest-carts/{cartId}/collection-point/search-request
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/default/V1/guest-carts/{cart_id}/collection-point/search-request'.format(cart_id='cart_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_temando_shipping_collection_point_guest_cart_collection_point_management_v1_save_search_request_put(client):
    """Test case for temando_shipping_collection_point_guest_cart_collection_point_management_v1_save_search_request_put

    guest-carts/{cartId}/collection-point/search-request
    """
    body = openapi_server.TemandoShippingCollectionPointCartCollectionPointManagementV1SaveSearchRequestPutRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/default/V1/guest-carts/{cart_id}/collection-point/search-request'.format(cart_id='cart_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

