# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.reservation_response import ReservationResponse
from openapi_server.models.split_request import SplitRequest


pytestmark = pytest.mark.asyncio

async def test_reservation_split(client):
    """Test case for reservation_split

    Split the `Reservation`.
    """
    body = {"properties":{"reservationId":"reservationId","quantities":[0,0]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/providers/Microsoft.Capacity/reservationOrders/{reservation_order_id}/split'.format(reservation_order_id='reservation_order_id_example'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

