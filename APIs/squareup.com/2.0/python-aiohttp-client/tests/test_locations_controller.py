# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_location_request import CreateLocationRequest
from openapi_server.models.create_location_response import CreateLocationResponse
from openapi_server.models.list_locations_response import ListLocationsResponse
from openapi_server.models.retrieve_location_response import RetrieveLocationResponse
from openapi_server.models.update_location_request import UpdateLocationRequest
from openapi_server.models.update_location_response import UpdateLocationResponse


pytestmark = pytest.mark.asyncio

async def test_create_location(client):
    """Test case for create_location

    CreateLocation
    """
    body = {"request_body":{"location":{"address":{"address_line_1":"1234 Peachtree St. NE","administrative_district_level_1":"GA","locality":"Atlanta","postal_code":"30309"},"description":"My new location.","facebook_url":null,"name":"New location name"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/locations',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_locations(client):
    """Test case for list_locations

    ListLocations
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/locations',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_location(client):
    """Test case for retrieve_location

    RetrieveLocation
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/locations/{location_id}'.format(location_id='location_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_location(client):
    """Test case for update_location

    UpdateLocation
    """
    body = {"request_body":{"location":{"address":{"address_line_1":"1234 Peachtree St. NE","administrative_district_level_1":"GA","locality":"Atlanta","postal_code":"30309"},"business_hours":{"periods":[{"day_of_week":"MON","end_local_time":1020,"start_local_time":"09:00"}]},"description":"Updated description","facebook_url":null,"instagram_username":"instagram","name":"Updated nickname","twitter_username":"twitter"}}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/locations/{location_id}'.format(location_id='location_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

