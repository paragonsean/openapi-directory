# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.multi_zone_result import MultiZoneResult
from openapi_server.models.zone_create import ZoneCreate
from openapi_server.models.zone_result import ZoneResult


pytestmark = pytest.mark.asyncio

async def test_zone_get(client):
    """Test case for zone_get

    get a list of zones
    """
    params = [('filters', 'filters_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/zone',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_zone_post(client):
    """Test case for zone_post

    create zone
    """
    zone = {"name":"name"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1.0/zone',
        headers=headers,
        json=zone,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_zone_zone_key_delete(client):
    """Test case for zone_zone_key_delete

    delete zone
    """
    params = [('checksum', '9cd24183-f848-48f8-6f55-0f07240700b9')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1.0/zone/{zone_key}'.format(zone_key='9cd24183-f848-48f8-6f55-0f0724070000'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_zone_zone_key_get(client):
    """Test case for zone_zone_key_get

    get zone
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1.0/zone/{zone_key}'.format(zone_key='9cd24183-f848-48f8-6f55-0f0724070000'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

