# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.temando_shipping_data_collection_point_quote_collection_point_interface import TemandoShippingDataCollectionPointQuoteCollectionPointInterface


pytestmark = pytest.mark.asyncio

async def test_temando_shipping_collection_point_guest_cart_collection_point_management_v1_get_collection_points_get(client):
    """Test case for temando_shipping_collection_point_guest_cart_collection_point_management_v1_get_collection_points_get

    guest-carts/{cartId}/collection-point/search-result
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/guest-carts/{cart_id}/collection-point/search-result'.format(cart_id='cart_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

