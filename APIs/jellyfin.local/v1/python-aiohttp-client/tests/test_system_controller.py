# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.end_point_info import EndPointInfo
from openapi_server.models.log_file import LogFile
from openapi_server.models.public_system_info import PublicSystemInfo
from openapi_server.models.system_info import SystemInfo
from openapi_server.models.wake_on_lan_info import WakeOnLanInfo


pytestmark = pytest.mark.asyncio

async def test_get_endpoint_info(client):
    """Test case for get_endpoint_info

    Gets information about the request endpoint.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/System/Endpoint',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_log_file(client):
    """Test case for get_log_file

    Gets a log file.
    """
    params = [('name', 'name_example')]
    headers = { 
        'Accept': 'text/plain',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/System/Logs/Log',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_ping_system(client):
    """Test case for get_ping_system

    Pings the system.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/System/Ping',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_public_system_info(client):
    """Test case for get_public_system_info

    Gets public information about the server.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/System/Info/Public',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_server_logs(client):
    """Test case for get_server_logs

    Gets a list of available server log files.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/System/Logs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_system_info(client):
    """Test case for get_system_info

    Gets information about the server.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/System/Info',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_wake_on_lan_info(client):
    """Test case for get_wake_on_lan_info

    Gets wake on lan information.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/System/WakeOnLanInfo',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_ping_system(client):
    """Test case for post_ping_system

    Pings the system.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/System/Ping',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_restart_application(client):
    """Test case for restart_application

    Restarts the application.
    """
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/System/Restart',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_shutdown_application(client):
    """Test case for shutdown_application

    Shuts down the application.
    """
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/System/Shutdown',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

