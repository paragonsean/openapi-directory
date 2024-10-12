# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response_content import ErrorResponseContent
from openapi_server.models.inventory_script_info import InventoryScriptInfo
from openapi_server.models.script_instance_custom_user_data import ScriptInstanceCustomUserData
from openapi_server.models.script_instance_details import ScriptInstanceDetails


pytestmark = pytest.mark.asyncio

async def test_scripts_instances_get(client):
    """Test case for scripts_instances_get

    Returns all script instances of the SIGNL4 team
    """
    params = [('teamId', 'team_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/scripts/instances',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_scripts_instances_instance_id_data_put(client):
    """Test case for scripts_instances_instance_id_data_put

    Updates custom data of a given script instance which includes its display name.
    """
    body = {"scriptId":"scriptId","instanceId":"instanceId","customScriptDescription":"customScriptDescription","customScriptName":"customScriptName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/scripts/instances/{instance_id}/data'.format(instance_id='instance_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scripts_instances_instance_id_delete(client):
    """Test case for scripts_instances_instance_id_delete

    Deletes a script instance.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/scripts/instances/{instance_id}'.format(instance_id='instance_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scripts_instances_instance_id_disable_post(client):
    """Test case for scripts_instances_instance_id_disable_post

    Disables a given script instance.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/scripts/instances/{instance_id}/disable'.format(instance_id='instance_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scripts_instances_instance_id_enable_post(client):
    """Test case for scripts_instances_instance_id_enable_post

    Enables a script instance.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/scripts/instances/{instance_id}/enable'.format(instance_id='instance_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scripts_instances_instance_id_get(client):
    """Test case for scripts_instances_instance_id_get

    Returns all information about a given script instance which includes its runtime status.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/scripts/instances/{instance_id}'.format(instance_id='instance_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_scripts_instances_instance_id_put(client):
    """Test case for scripts_instances_instance_id_put

    Updates a given script instance, typically used for updating the configuration of a script.
    """
    body = {"scriptId":"scriptId","instanceId":"instanceId","teamId":"teamId","scriptName":"scriptName","lastModified":"2000-01-23T04:56:07.000+00:00","subscriptionId":"subscriptionId","config":"","eventPattern":"","enabled":True,"runtimeInformation":{"statusMessage":"statusMessage","status":0},"customScriptDescription":"customScriptDescription","customScriptName":"customScriptName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/scripts/instances/{instance_id}'.format(instance_id='instance_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_scripts_instances_post(client):
    """Test case for scripts_instances_post

    Creates a new script instance in the in the SIGNL4 team.
    """
    body = {"scriptId":"scriptId","instanceId":"instanceId","teamId":"teamId","scriptName":"scriptName","lastModified":"2000-01-23T04:56:07.000+00:00","subscriptionId":"subscriptionId","config":"","eventPattern":"","enabled":True,"runtimeInformation":{"statusMessage":"statusMessage","status":0},"customScriptDescription":"customScriptDescription","customScriptName":"customScriptName"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/scripts/instances',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scripts_inventory_get(client):
    """Test case for scripts_inventory_get

    Returns all available inventory scripts which can be added to a SIGNL4 subscription.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/scripts/inventory',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scripts_inventory_parsed_get(client):
    """Test case for scripts_inventory_parsed_get

    Returns all inventory scripts.
    """
    params = [('language', 'language_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/scripts/inventory/parsed',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scripts_inventory_parsed_script_id_get(client):
    """Test case for scripts_inventory_parsed_script_id_get

    Returns an inventory script by its id.
    """
    params = [('language', 'language_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/scripts/inventory/parsed/{script_id}'.format(script_id='script_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

