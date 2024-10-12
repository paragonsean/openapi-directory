# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.properties import Properties


pytestmark = pytest.mark.asyncio

async def test_reservation_available_scopes(client):
    """Test case for reservation_available_scopes

    Get Available Scopes for `Reservation`.
    """
    body = ['body_example']
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Capacity/reservationOrders/{reservation_order_id}/reservations/{reservation_id}/availableScopes'.format(reservation_order_id='reservation_order_id_example', reservation_id='reservation_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

