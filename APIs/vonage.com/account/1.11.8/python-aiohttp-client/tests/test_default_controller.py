# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.account_hal_response import AccountHalResponse
from openapi_server.models.location_hal_response import LocationHalResponse
from openapi_server.models.locations_hal_response import LocationsHalResponse


pytestmark = pytest.mark.asyncio

async def test_account_ctrl_get_account_services_by_account_id(client):
    """Test case for account_ctrl_get_account_services_by_account_id

    Get account data by ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/t/vbc.prod/provisioning/api/accounts/{account_id}'.format(account_id=571700),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_ctrl_get_location_by_id(client):
    """Test case for account_ctrl_get_location_by_id

    Get location data by account ID and location ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/t/vbc.prod/provisioning/api/accounts/{account_id}/locations/{location_id}'.format(account_id=571700, location_id=327910),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_account_ctrl_get_locations_by_account_id(client):
    """Test case for account_ctrl_get_locations_by_account_id

    Get account locations data by account ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/t/vbc.prod/provisioning/api/accounts/{account_id}/locations'.format(account_id=571700),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

