# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.action_response import ActionResponse
from openapi_server.models.actions_response import ActionsResponse
from openapi_server.models.add_to_placement_group_request import AddToPlacementGroupRequest
from openapi_server.models.attach_to_network_request import AttachToNetworkRequest
from openapi_server.models.create_image_request import CreateImageRequest
from openapi_server.models.detach_from_network_request import DetachFromNetworkRequest
from openapi_server.models.rebuild_server_request import RebuildServerRequest
from openapi_server.models.servers_id_actions_attach_iso_post_request import ServersIdActionsAttachIsoPostRequest
from openapi_server.models.servers_id_actions_change_alias_ips_post_request import ServersIdActionsChangeAliasIpsPostRequest
from openapi_server.models.servers_id_actions_change_dns_ptr_post_request import ServersIdActionsChangeDnsPtrPostRequest
from openapi_server.models.servers_id_actions_change_protection_post_request import ServersIdActionsChangeProtectionPostRequest
from openapi_server.models.servers_id_actions_change_type_post_request import ServersIdActionsChangeTypePostRequest
from openapi_server.models.servers_id_actions_create_image_post201_response import ServersIdActionsCreateImagePost201Response
from openapi_server.models.servers_id_actions_enable_rescue_post201_response import ServersIdActionsEnableRescuePost201Response
from openapi_server.models.servers_id_actions_enable_rescue_post_request import ServersIdActionsEnableRescuePostRequest
from openapi_server.models.servers_id_actions_rebuild_post201_response import ServersIdActionsRebuildPost201Response
from openapi_server.models.servers_id_actions_request_console_post201_response import ServersIdActionsRequestConsolePost201Response


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_action_id_get(client):
    """Test case for servers_id_actions_action_id_get

    Get an Action for a Server
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/servers/{id}/actions/{action_id}'.format(id=56, action_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_add_to_placement_group_post(client):
    """Test case for servers_id_actions_add_to_placement_group_post

    Add a Server to a Placement Group
    """
    body = {"placement_group":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers/{id}/actions/add_to_placement_group'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_attach_iso_post(client):
    """Test case for servers_id_actions_attach_iso_post

    Attach an ISO to a Server
    """
    body = openapi_server.ServersIdActionsAttachIsoPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers/{id}/actions/attach_iso'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_attach_to_network_post(client):
    """Test case for servers_id_actions_attach_to_network_post

    Attach a Server to a Network
    """
    body = {"ip":"10.0.1.1","alias_ips":["10.0.1.2"],"network":4711}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers/{id}/actions/attach_to_network'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_change_alias_ips_post(client):
    """Test case for servers_id_actions_change_alias_ips_post

    Change alias IPs of a Network
    """
    body = openapi_server.ServersIdActionsChangeAliasIpsPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers/{id}/actions/change_alias_ips'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_change_dns_ptr_post(client):
    """Test case for servers_id_actions_change_dns_ptr_post

    Change reverse DNS entry for this Server
    """
    body = openapi_server.ServersIdActionsChangeDnsPtrPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers/{id}/actions/change_dns_ptr'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_change_protection_post(client):
    """Test case for servers_id_actions_change_protection_post

    Change Server Protection
    """
    body = openapi_server.ServersIdActionsChangeProtectionPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers/{id}/actions/change_protection'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_change_type_post(client):
    """Test case for servers_id_actions_change_type_post

    Change the Type of a Server
    """
    body = openapi_server.ServersIdActionsChangeTypePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers/{id}/actions/change_type'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_create_image_post(client):
    """Test case for servers_id_actions_create_image_post

    Create Image from a Server
    """
    body = {"description":"my image","type":"snapshot","labels":{"labelkey":"value"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers/{id}/actions/create_image'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_detach_from_network_post(client):
    """Test case for servers_id_actions_detach_from_network_post

    Detach a Server from a Network
    """
    body = {"network":4711}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers/{id}/actions/detach_from_network'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_detach_iso_post(client):
    """Test case for servers_id_actions_detach_iso_post

    Detach an ISO from a Server
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers/{id}/actions/detach_iso'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_disable_backup_post(client):
    """Test case for servers_id_actions_disable_backup_post

    Disable Backups for a Server
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers/{id}/actions/disable_backup'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_disable_rescue_post(client):
    """Test case for servers_id_actions_disable_rescue_post

    Disable Rescue Mode for a Server
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers/{id}/actions/disable_rescue'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_enable_backup_post(client):
    """Test case for servers_id_actions_enable_backup_post

    Enable and Configure Backups for a Server
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers/{id}/actions/enable_backup'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_enable_rescue_post(client):
    """Test case for servers_id_actions_enable_rescue_post

    Enable Rescue Mode for a Server
    """
    body = openapi_server.ServersIdActionsEnableRescuePostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers/{id}/actions/enable_rescue'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_get(client):
    """Test case for servers_id_actions_get

    Get all Actions for a Server
    """
    params = [('sort', 'sort_example'),
                    ('status', 'status_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/servers/{id}/actions'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_poweroff_post(client):
    """Test case for servers_id_actions_poweroff_post

    Power off a Server
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers/{id}/actions/poweroff'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_poweron_post(client):
    """Test case for servers_id_actions_poweron_post

    Power on a Server
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers/{id}/actions/poweron'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_reboot_post(client):
    """Test case for servers_id_actions_reboot_post

    Soft-reboot a Server
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers/{id}/actions/reboot'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_rebuild_post(client):
    """Test case for servers_id_actions_rebuild_post

    Rebuild a Server from an Image
    """
    body = {"image":"ubuntu-20.04"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers/{id}/actions/rebuild'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_remove_from_placement_group_post(client):
    """Test case for servers_id_actions_remove_from_placement_group_post

    Remove from Placement Group
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers/{id}/actions/remove_from_placement_group'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_request_console_post(client):
    """Test case for servers_id_actions_request_console_post

    Request Console for a Server
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers/{id}/actions/request_console'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_reset_password_post(client):
    """Test case for servers_id_actions_reset_password_post

    Reset root Password of a Server
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers/{id}/actions/reset_password'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_reset_post(client):
    """Test case for servers_id_actions_reset_post

    Reset a Server
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers/{id}/actions/reset'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_servers_id_actions_shutdown_post(client):
    """Test case for servers_id_actions_shutdown_post

    Shutdown a Server
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/servers/{id}/actions/shutdown'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

