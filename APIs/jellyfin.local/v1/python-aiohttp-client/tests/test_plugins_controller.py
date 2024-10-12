# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.plugin_info import PluginInfo
from openapi_server.models.plugin_security_info import PluginSecurityInfo
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.version import Version


pytestmark = pytest.mark.asyncio

async def test_disable_plugin(client):
    """Test case for disable_plugin

    Disable a plugin.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Plugins/{plugin_id}/{version}/Disable'.format(plugin_id='plugin_id_example', version=openapi_server.Version()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_enable_plugin(client):
    """Test case for enable_plugin

    Enables a disabled plugin.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Plugins/{plugin_id}/{version}/Enable'.format(plugin_id='plugin_id_example', version=openapi_server.Version()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_plugin_configuration(client):
    """Test case for get_plugin_configuration

    Gets plugin configuration.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Plugins/{plugin_id}/Configuration'.format(plugin_id='plugin_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_plugin_image(client):
    """Test case for get_plugin_image

    Gets a plugin's image.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Plugins/{plugin_id}/{version}/Image'.format(plugin_id='plugin_id_example', version=openapi_server.Version()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_plugin_manifest(client):
    """Test case for get_plugin_manifest

    Gets a plugin's manifest.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Plugins/{plugin_id}/Manifest'.format(plugin_id='plugin_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_plugins(client):
    """Test case for get_plugins

    Gets a list of currently installed plugins.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/Plugins',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_uninstall_plugin(client):
    """Test case for uninstall_plugin

    Uninstalls a plugin.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Plugins/{plugin_id}'.format(plugin_id='plugin_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_uninstall_plugin_by_version(client):
    """Test case for uninstall_plugin_by_version

    Uninstalls a plugin by version.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Plugins/{plugin_id}/{version}'.format(plugin_id='plugin_id_example', version=openapi_server.Version()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_plugin_configuration(client):
    """Test case for update_plugin_configuration

    Updates plugin configuration.
    """
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Plugins/{plugin_id}/Configuration'.format(plugin_id='plugin_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_plugin_security_info(client):
    """Test case for update_plugin_security_info

    Updates plugin security info.
    """
    body = {"IsMbSupporter":True,"SupporterKey":"SupporterKey"}
    headers = { 
        'Content-Type': 'application/*+json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Plugins/SecurityInfo',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

