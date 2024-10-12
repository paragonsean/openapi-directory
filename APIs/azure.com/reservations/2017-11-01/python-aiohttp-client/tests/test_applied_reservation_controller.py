# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.applied_reservations import AppliedReservations
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_get_applied_reservation_list(client):
    """Test case for get_applied_reservation_list

    Get list of applicable `Reservation`s.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Capacity/appliedReservations'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

