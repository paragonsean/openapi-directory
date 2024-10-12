# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.calendar import Calendar


pytestmark = pytest.mark.asyncio

async def test_calendars_get(client):
    """Test case for calendars_get

    Fetch a list of Calendars
    """
    params = [('all', True),
                    ('userId', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/calendars',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendars_id_delete(client):
    """Test case for calendars_id_delete

    Delete a Calendar
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/calendars/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendars_id_put(client):
    """Test case for calendars_id_put

    Update a Calendar
    """
    body = {"data":"data","name":"name","attributes":"{}","id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/calendars/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendars_post(client):
    """Test case for calendars_post

    Create a Calendar
    """
    body = {"data":"data","name":"name","attributes":"{}","id":0}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/calendars',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

