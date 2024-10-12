# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_dweet_for_thing_post(client):
    """Test case for dweet_for_thing_post

    Create a dweet for a thing.
    """
    content = 'content_example'
    params = [('key', 'key_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/dweet/for/{thing}'.format(thing='thing_example'),
        headers=headers,
        json=content,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_dweet_quietly_for_thing_post(client):
    """Test case for dweet_quietly_for_thing_post

    Create a dweet for a thing.  This method differs from /dweet/for/{thing} only in that successful dweets result in an HTTP 204 response rather than the typical verbose response.
    """
    content = 'content_example'
    params = [('key', 'key_example')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/dweet/quietly/for/{thing}'.format(thing='thing_example'),
        headers=headers,
        json=content,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dweets_for_thing_get(client):
    """Test case for get_dweets_for_thing_get

    Read the last 5 cached dweets for a thing.
    """
    params = [('key', 'key_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/get/dweets/for/{thing}'.format(thing='thing_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_latest_dweet(client):
    """Test case for get_latest_dweet

    Read the latest dweet for a thing.
    """
    params = [('key', 'key_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/get/latest/dweet/for/{thing}'.format(thing='thing_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_listen_for_dweets(client):
    """Test case for listen_for_dweets

    Listen for dweets from a thing.
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/listen/for/dweets/from/{thing}'.format(thing='thing_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

