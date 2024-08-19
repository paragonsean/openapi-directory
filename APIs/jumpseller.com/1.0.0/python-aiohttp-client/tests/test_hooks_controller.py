# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.hook import Hook
from openapi_server.models.hook_edit import HookEdit
from openapi_server.models.not_found import NotFound


pytestmark = pytest.mark.asyncio

async def test_hooks_id_json_delete(client):
    """Test case for hooks_id_json_delete

    Delete an existing Hook.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/hooks/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hooks_id_json_get(client):
    """Test case for hooks_id_json_get

    Retrieve a single Hook.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/hooks/{id_jso}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hooks_id_json_put(client):
    """Test case for hooks_id_json_put

    Update a Hook.
    """
    body = {"hook":{"event":"order_updated","url":"url"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/v1/hooks/{id_jso}'.format(id=56),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hooks_json_get(client):
    """Test case for hooks_json_get

    Retrieve all Hooks.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example'),
                    ('limit', 50),
                    ('page', 1)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/hooks.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hooks_json_post(client):
    """Test case for hooks_json_post

    Create a new Hook.
    """
    body = {"hook":{"event":"order_updated","url":"url"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/hooks.json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

