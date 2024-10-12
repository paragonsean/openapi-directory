# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_reservation200_response import CreateReservation200Response
from openapi_server.models.create_reservation_request1 import CreateReservationRequest1
from openapi_server.models.reservation_by_id200_response import ReservationById200Response


pytestmark = pytest.mark.asyncio

async def test_acknowledgment_reservation(client):
    """Test case for acknowledgment_reservation

    Acknowledgment reservation
    """
    headers = { 
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/logistics/pvt/inventory/reservations/{reservation_id}/acknowledge'.format(reservation_id='reservation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancel_reservation(client):
    """Test case for cancel_reservation

    Cancel reservation
    """
    headers = { 
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/logistics/pvt/inventory/reservations/{reservation_id}/cancel'.format(reservation_id='reservation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_confirm_reservation(client):
    """Test case for confirm_reservation

    Confirm reservation
    """
    headers = { 
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/logistics/pvt/inventory/reservations/{reservation_id}/confirm'.format(reservation_id='reservation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/json; charset&#x3D;utf-8 not supported by Connexion")
async def test_create_reservation(client):
    """Test case for create_reservation

    Create reservation
    """
    body = {"autorizationExpirationTTL":"00:10:00","deliveryItemOptions":[{"aditionalTimeBlockedDays":"00:00:00","deliveryWindows":[],"dockId":"1a8bce3","dockTime":"00:00:00","item":{"additionalHandlingTime":"00:00:00","dimension":{"height":1,"length":1,"weight":150,"width":1},"groupItemId":null,"id":"2390059","kitItem":[],"price":0,"quantity":1},"listPrice":10.5,"location":{"country":"BRA","inStore":{"IsCheckedIn":false,"StoreId":null},"zipCode":"22220070"},"promotionalPrice":10.5,"slaType":"Expressa","slaTypeName":"Expressa","timeToDockPlusDockTime":"1.00:00:00","totalTime":"3.00:00:00","transitTime":"2.00:00:00","wareHouseId":null}],"lockId":null,"salesChannel":"1"}
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'content_type': 'application/json; charset=utf-8',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/logistics/pvt/inventory/reservations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reservation_by_id(client):
    """Test case for reservation_by_id

    List reservation by ID
    """
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/logistics/pvt/inventory/reservations/{reservation_id}'.format(reservation_id='reservation_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reservationby_warehouseand_sku(client):
    """Test case for reservationby_warehouseand_sku

    List reservation by warehouse and SKU
    """
    headers = { 
        'content_type': 'application/json; charset=utf-8',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/logistics/pvt/inventory/reservations/{warehouse_id}/{sku_id}'.format(warehouse_id='warehouse_id_example', sku_id='sku_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

