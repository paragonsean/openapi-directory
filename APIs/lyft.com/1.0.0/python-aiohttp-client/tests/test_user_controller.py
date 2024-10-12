# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_error import ApiError
from openapi_server.models.cancellation_cost_error import CancellationCostError
from openapi_server.models.cancellation_request import CancellationRequest
from openapi_server.models.location import Location
from openapi_server.models.profile import Profile
from openapi_server.models.rating_request import RatingRequest
from openapi_server.models.ride import Ride
from openapi_server.models.ride_detail import RideDetail
from openapi_server.models.ride_receipt import RideReceipt
from openapi_server.models.ride_request import RideRequest
from openapi_server.models.ride_request_error import RideRequestError
from openapi_server.models.rides_response import RidesResponse


pytestmark = pytest.mark.asyncio

async def test_cancel_ride(client):
    """Test case for cancel_ride

    Cancel a ongoing requested ride
    """
    request = {"cancel_confirmation_token":"656a91d"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/rides/{id}/cancel'.format(id='id_example'),
        headers=headers,
        json=request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_profile(client):
    """Test case for get_profile

    The user's general info
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/profile',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ride(client):
    """Test case for get_ride

    Get the ride detail of a given ride ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/rides/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ride_receipt(client):
    """Test case for get_ride_receipt

    Get the receipt of the rides.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/rides/{id}/receipt'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_rides(client):
    """Test case for get_rides

    List rides
    """
    params = [('start_time', '2013-10-20T19:20:30+01:00'),
                    ('end_time', '2013-10-20T19:20:30+01:00'),
                    ('limit', 10)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/rides',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_new_ride(client):
    """Test case for new_ride

    Request a Lyft
    """
    request = {"origin":"{}","cost_token":"cost_token","destination":"{}","primetime_confirmation_token":"primetime_confirmation_token","ride_type":"lyft"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/rides',
        headers=headers,
        json=request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_ride_destination(client):
    """Test case for set_ride_destination

    Update the destination of the ride
    """
    request = {"address":"address","lng":6.027456183070403,"lat":0.8008281904610115}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/rides/{id}/destination'.format(id='id_example'),
        headers=headers,
        json=request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_set_ride_rating(client):
    """Test case for set_ride_rating

    Add the passenger's rating, feedback, and tip
    """
    request = {"feedback":"Great ride!","rating":5,"tip":{"amount":100,"currency":"USD"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/rides/{id}/rating'.format(id='id_example'),
        headers=headers,
        json=request,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

