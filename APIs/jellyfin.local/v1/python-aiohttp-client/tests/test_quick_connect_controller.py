# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.quick_connect_result import QuickConnectResult
from openapi_server.models.quick_connect_state import QuickConnectState


pytestmark = pytest.mark.asyncio

async def test_activate(client):
    """Test case for activate

    Temporarily activates quick connect for five minutes.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/QuickConnect/Activate',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_authorize(client):
    """Test case for authorize

    Authorizes a pending quick connect request.
    """
    params = [('code', 'code_example')]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/QuickConnect/Authorize',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_available(client):
    """Test case for available

    Enables or disables quick connect.
    """
    params = [('status', openapi_server.QuickConnectState())]
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/QuickConnect/Available',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connect(client):
    """Test case for connect

    Attempts to retrieve authentication information.
    """
    params = [('secret', 'secret_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/QuickConnect/Connect',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deauthorize(client):
    """Test case for deauthorize

    Deauthorize all quick connect devices for the current user.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/QuickConnect/Deauthorize',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_status(client):
    """Test case for get_status

    Gets the current quick connect state.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/QuickConnect/Status',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_initiate(client):
    """Test case for initiate

    Initiate a new quick connect request.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/QuickConnect/Initiate',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

