# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.patch import Patch
from openapi_server.models.reservation_list import ReservationList
from openapi_server.models.reservation_order_list import ReservationOrderList
from openapi_server.models.reservation_order_response import ReservationOrderResponse
from openapi_server.models.reservation_response import ReservationResponse


pytestmark = pytest.mark.asyncio

async def test_reservation_get(client):
    """Test case for reservation_get

    Get `Reservation` details.
    """
    params = [('api-version', 'api_version_example'),
                    ('expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Capacity/reservationOrders/{reservation_order_id}/reservations/{reservation_id}'.format(reservation_id='reservation_id_example', reservation_order_id='reservation_order_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reservation_list(client):
    """Test case for reservation_list

    Get `Reservation`s in a given reservation Order
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Capacity/reservationOrders/{reservation_order_id}/reservations'.format(reservation_order_id='reservation_order_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reservation_list_revisions(client):
    """Test case for reservation_list_revisions

    Get `Reservation` revisions.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Capacity/reservationOrders/{reservation_order_id}/reservations/{reservation_id}/revisions'.format(reservation_id='reservation_id_example', reservation_order_id='reservation_order_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reservation_order_get(client):
    """Test case for reservation_order_get

    Get a specific `ReservationOrder`.
    """
    params = [('api-version', 'api_version_example'),
                    ('$expand', 'expand_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Capacity/reservationOrders/{reservation_order_id}'.format(reservation_order_id='reservation_order_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reservation_order_list(client):
    """Test case for reservation_order_list

    Get all `ReservationOrder`s.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/providers/Microsoft.Capacity/reservationOrders',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reservation_update(client):
    """Test case for reservation_update

    Updates a `Reservation`.
    """
    parameters = {"properties":{"appliedScopes":["appliedScopes","appliedScopes"],"renewProperties":{"purchaseProperties":{"location":"location","sku":{"name":"name"},"properties":{"reservedResourceType":"VirtualMachines","reservedResourceProperties":{"instanceFlexibility":"On"},"billingScopeId":"billingScopeId","quantity":0,"appliedScopes":["appliedScopes","appliedScopes"],"displayName":"displayName","appliedScopeType":"Single","billingPlan":"Upfront","term":"P1Y","renew":False}}},"name":"name","appliedScopeType":"Single","instanceFlexibility":"On","renew":False}}
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

