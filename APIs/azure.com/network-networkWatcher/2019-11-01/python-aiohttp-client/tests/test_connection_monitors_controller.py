# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connection_monitor import ConnectionMonitor
from openapi_server.models.connection_monitor_list_result import ConnectionMonitorListResult
from openapi_server.models.connection_monitor_query_result import ConnectionMonitorQueryResult
from openapi_server.models.connection_monitor_result import ConnectionMonitorResult
from openapi_server.models.connection_monitors_list_default_response import ConnectionMonitorsListDefaultResponse
from openapi_server.models.network_watchers_update_tags_request import NetworkWatchersUpdateTagsRequest


pytestmark = pytest.mark.asyncio

async def test_connection_monitors_create_or_update(client):
    """Test case for connection_monitors_create_or_update

    
    """
    parameters = {"location":"location","properties":{"outputs":[{"workspaceSettings":{"workspaceResourceId":"workspaceResourceId"},"type":"Workspace"},{"workspaceSettings":{"workspaceResourceId":"workspaceResourceId"},"type":"Workspace"}],"endpoints":[{"filter":{"type":"Include","items":[{"address":"address","type":"AgentAddress"},{"address":"address","type":"AgentAddress"}]},"resourceId":"resourceId","address":"address","name":"name"},{"filter":{"type":"Include","items":[{"address":"address","type":"AgentAddress"},{"address":"address","type":"AgentAddress"}]},"resourceId":"resourceId","address":"address","name":"name"}],"notes":"notes","testGroups":[{"sources":["sources","sources"],"disable":True,"destinations":["destinations","destinations"],"name":"name","testConfigurations":["testConfigurations","testConfigurations"]},{"sources":["sources","sources"],"disable":True,"destinations":["destinations","destinations"],"name":"name","testConfigurations":["testConfigurations","testConfigurations"]}],"destination":{"resourceId":"resourceId","address":"address","port":0},"source":{"resourceId":"resourceId","port":1},"testConfigurations":[{"icmpConfiguration":{"disableTraceRoute":True},"protocol":"Tcp","testFrequencySec":9,"name":"name","tcpConfiguration":{"disableTraceRoute":True,"port":7},"successThreshold":{"roundTripTimeMs":2,"checksFailedPercent":5},"httpConfiguration":{"path":"path","requestHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"method":"Get","port":5,"validStatusCodeRanges":["validStatusCodeRanges","validStatusCodeRanges"],"preferHTTPS":True},"preferredIPVersion":"IPv4"},{"icmpConfiguration":{"disableTraceRoute":True},"protocol":"Tcp","testFrequencySec":9,"name":"name","tcpConfiguration":{"disableTraceRoute":True,"port":7},"successThreshold":{"roundTripTimeMs":2,"checksFailedPercent":5},"httpConfiguration":{"path":"path","requestHeaders":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"method":"Get","port":5,"validStatusCodeRanges":["validStatusCodeRanges","validStatusCodeRanges"],"preferHTTPS":True},"preferredIPVersion":"IPv4"}],"monitoringIntervalInSeconds":6,"autoStart":True},"tags":{"key":"tags"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/connectionMonitors/{connection_monitor_name}'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', connection_monitor_name='connection_monitor_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connection_monitors_delete(client):
    """Test case for connection_monitors_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/connectionMonitors/{connection_monitor_name}'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', connection_monitor_name='connection_monitor_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connection_monitors_get(client):
    """Test case for connection_monitors_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/connectionMonitors/{connection_monitor_name}'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', connection_monitor_name='connection_monitor_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connection_monitors_list(client):
    """Test case for connection_monitors_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/connectionMonitors'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connection_monitors_query(client):
    """Test case for connection_monitors_query

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/connectionMonitors/{connection_monitor_name}/query'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', connection_monitor_name='connection_monitor_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connection_monitors_start(client):
    """Test case for connection_monitors_start

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/connectionMonitors/{connection_monitor_name}/start'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', connection_monitor_name='connection_monitor_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connection_monitors_stop(client):
    """Test case for connection_monitors_stop

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/connectionMonitors/{connection_monitor_name}/stop'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', connection_monitor_name='connection_monitor_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connection_monitors_update_tags(client):
    """Test case for connection_monitors_update_tags

    
    """
    parameters = openapi_server.NetworkWatchersUpdateTagsRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/connectionMonitors/{connection_monitor_name}'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', connection_monitor_name='connection_monitor_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

