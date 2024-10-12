# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.sandbox_driver_availability import SandboxDriverAvailability
from openapi_server.models.sandbox_primetime import SandboxPrimetime
from openapi_server.models.sandbox_ride_status import SandboxRideStatus
from openapi_server.models.sandbox_ride_type import SandboxRideType
from openapi_server.models.sandbox_ride_update import SandboxRideUpdate


pytestmark = pytest.mark.asyncio

async def test_set_prime_time(client):
    """Test case for set_prime_time

    Preset Prime Time percentage
    """
    request = {"lat":37.7833,"lng":-122.4167,"primetime_percentage":"25%"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/sandbox/primetime',
        headers=headers,
        json=request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_ride_status(client):
    """Test case for set_ride_status

    Propagate ride through ride status
    """
    request = {"status":"lyft"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/sandbox/rides/{id}'.format(id='id_example'),
        headers=headers,
        json=request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_ride_type_availability(client):
    """Test case for set_ride_type_availability

    Driver availability for processing ride request
    """
    request = {"driver_availability":True,"lat":37.7833,"lng":-122.4167}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/sandbox/ridetypes/{ride_type}'.format(ride_type='ride_type_example'),
        headers=headers,
        json=request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_ride_types(client):
    """Test case for set_ride_types

    Preset types of rides for sandbox
    """
    request = {"lat":37.7833,"lng":-122.4167,"ride_types":["lyft","lyft_line","lyft_plus"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/sandbox/ridetypes',
        headers=headers,
        json=request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

