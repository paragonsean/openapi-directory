# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.app import App
from openapi_server.models.js_app import JSApp
from openapi_server.models.js_app_edit import JSAppEdit
from openapi_server.models.not_found import NotFound


pytestmark = pytest.mark.asyncio

async def test_jsapps_code_json_delete(client):
    """Test case for jsapps_code_json_delete

    Delete an existing JSApp.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/jsapps/{code_jso}'.format(code='code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jsapps_code_json_get(client):
    """Test case for jsapps_code_json_get

    Retrieve a JSApp.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/jsapps/{code_jso}'.format(code='code_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jsapps_json_get(client):
    """Test case for jsapps_json_get

    Retrieve all the Store's JSApps.
    """
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/jsapps.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_jsapps_json_post(client):
    """Test case for jsapps_json_post

    Create a Store JSApp.
    """
    body = {"app":{"template":"template","url":"url","element":"element"}}
    params = [('login', 'login_example'),
                    ('authtoken', 'authtoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/jsapps.json',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

