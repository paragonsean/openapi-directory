# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.patch import Patch
from openapi_server.models.reservation_response import ReservationResponse


pytestmark = pytest.mark.asyncio

async def test_reservation_update_0(client):
    """Test case for reservation_update_0

    Updates a `Reservation`.
    """
    parameters = {"properties":{"appliedScopes":["appliedScopes","appliedScopes"],"appliedScopeType":"Single"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/providers/Microsoft.Capacity/reservationOrders/{reservation_order_id}/reservations/{reservation_id}'.format(reservation_order_id='reservation_order_id_example', reservation_id='reservation_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

