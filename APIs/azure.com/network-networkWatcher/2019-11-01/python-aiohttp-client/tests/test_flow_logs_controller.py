# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connection_monitors_list_default_response import ConnectionMonitorsListDefaultResponse
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.flow_log import FlowLog
from openapi_server.models.flow_log_list_result import FlowLogListResult


pytestmark = pytest.mark.asyncio

async def test_flow_logs_create_or_update(client):
    """Test case for flow_logs_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"targetResourceId":"targetResourceId","format":{"type":"JSON","version":6},"targetResourceGuid":"targetResourceGuid","provisioningState":"Succeeded","retentionPolicy":{"days":1,"enabled":False},"flowAnalyticsConfiguration":{"networkWatcherFlowAnalyticsConfiguration":{"trafficAnalyticsInterval":0,"workspaceResourceId":"workspaceResourceId","workspaceRegion":"workspaceRegion","enabled":True,"workspaceId":"workspaceId"}},"enabled":True,"storageId":"storageId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/flowLogs/{flow_log_name}'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', flow_log_name='flow_log_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flow_logs_delete(client):
    """Test case for flow_logs_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/flowLogs/{flow_log_name}'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', flow_log_name='flow_log_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flow_logs_get(client):
    """Test case for flow_logs_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/flowLogs/{flow_log_name}'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', flow_log_name='flow_log_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_flow_logs_list(client):
    """Test case for flow_logs_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/flowLogs'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

