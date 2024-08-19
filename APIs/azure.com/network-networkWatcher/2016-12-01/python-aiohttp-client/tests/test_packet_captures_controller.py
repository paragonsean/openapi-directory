# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.packet_capture import PacketCapture
from openapi_server.models.packet_capture_list_result import PacketCaptureListResult
from openapi_server.models.packet_capture_query_status_result import PacketCaptureQueryStatusResult
from openapi_server.models.packet_capture_result import PacketCaptureResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_packet_captures_create(client):
    """Test case for packet_captures_create

    
    """
    parameters = {"properties":{"totalBytesPerSession":1,"timeLimitInSeconds":6,"bytesToCapturePerPacket":0,"storageLocation":{"filePath":"filePath","storagePath":"storagePath","storageId":"storageId"},"filters":[{"protocol":"Any","localPort":"localPort","remoteIPAddress":"remoteIPAddress","remotePort":"remotePort","localIPAddress":"localIPAddress"},{"protocol":"Any","localPort":"localPort","remoteIPAddress":"remoteIPAddress","remotePort":"remotePort","localIPAddress":"localIPAddress"}],"target":"target"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/packetCaptures/{packet_capture_name}'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', packet_capture_name='packet_capture_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_packet_captures_delete(client):
    """Test case for packet_captures_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/packetCaptures/{packet_capture_name}'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', packet_capture_name='packet_capture_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_packet_captures_get(client):
    """Test case for packet_captures_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/packetCaptures/{packet_capture_name}'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', packet_capture_name='packet_capture_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_packet_captures_get_status(client):
    """Test case for packet_captures_get_status

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/packetCaptures/{packet_capture_name}/queryStatus'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', packet_capture_name='packet_capture_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_packet_captures_list(client):
    """Test case for packet_captures_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/packetCaptures'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_packet_captures_stop(client):
    """Test case for packet_captures_stop

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/packetCaptures/{packet_capture_name}/stop'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', packet_capture_name='packet_capture_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

