# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.startup_configuration_dto import StartupConfigurationDto
from openapi_server.models.startup_remote_access_dto import StartupRemoteAccessDto
from openapi_server.models.startup_user_dto import StartupUserDto


pytestmark = pytest.mark.asyncio

async def test_complete_wizard(client):
    """Test case for complete_wizard

    Completes the startup wizard.
    """
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Startup/Complete',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_first_user(client):
    """Test case for get_first_user

    Gets the first user.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Startup/User',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_first_user2(client):
    """Test case for get_first_user2

    Gets the first user.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Startup/FirstUser',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_startup_configuration(client):
    """Test case for get_startup_configuration

    Gets the initial startup wizard configuration.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Startup/Configuration',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_set_remote_access(client):
    """Test case for set_remote_access

    Sets remote access and UPnP.
    """
    body = {"EnableAutomaticPortMapping":True,"EnableRemoteAccess":True}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Startup/RemoteAccess',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_initial_configuration(client):
    """Test case for update_initial_configuration

    Sets the initial startup wizard configuration.
    """
    body = {"PreferredMetadataLanguage":"PreferredMetadataLanguage","UICulture":"UICulture","MetadataCountryCode":"MetadataCountryCode"}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Startup/Configuration',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_startup_user(client):
    """Test case for update_startup_user

    Sets the user name and password.
    """
    body = {"Name":"Name","Password":"Password"}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Startup/User',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

