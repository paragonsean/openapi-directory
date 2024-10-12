# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_lock_thing(client):
    """Test case for lock_thing

    Reserve and lock a thing.
    """
    params = [('lock', 'lock_example'),
                    ('key', 'key_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/lock/{thing}'.format(thing='thing_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_lock(client):
    """Test case for remove_lock

    Remove a lock from thing.
    """
    params = [('key', 'key_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/remove/lock/{lock}'.format(lock='lock_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unlock_thing(client):
    """Test case for unlock_thing

    Unlock a thing.
    """
    params = [('key', 'key_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/unlock/{thing}'.format(thing='thing_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

