# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.done import Done
from openapi_server.models.group import Group
from openapi_server.models.outage import Outage
from openapi_server.models.snow_monkey_config import SnowMonkeyConfig


pytestmark = pytest.mark.asyncio

async def test_get_snow_monkey_config(client):
    """Test case for get_snow_monkey_config

    Get current Snow Monkey config
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/snowmonkey/config',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_snow_monkey_outages(client):
    """Test case for get_snow_monkey_outages

    Get all current Snow Monkey ourages
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/snowmonkey/outages',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_snow_monkey(client):
    """Test case for patch_snow_monkey

    Update current Snow Monkey config
    """
    body = {"name":"a string value","description":"a string value","id":"a string value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PATCH',
        path='/api/snowmonkey/config',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_reset_snow_monkey(client):
    """Test case for reset_snow_monkey

    Reset Snow Monkey Outages for the day
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/snowmonkey/outages',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_start_snow_monkey(client):
    """Test case for start_snow_monkey

    Start the Snow Monkey
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/snowmonkey/_start',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stop_snow_monkey(client):
    """Test case for stop_snow_monkey

    Stop the Snow Monkey
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/snowmonkey/_stop',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_snow_monkey(client):
    """Test case for update_snow_monkey

    Update current Snow Monkey config
    """
    body = {"name":"a string value","description":"a string value","id":"a string value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/snowmonkey/config',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

