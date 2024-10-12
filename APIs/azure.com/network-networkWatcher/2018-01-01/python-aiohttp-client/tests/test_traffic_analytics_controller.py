# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.flow_log_information import FlowLogInformation
from openapi_server.models.flow_log_status_parameters import FlowLogStatusParameters


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_network_watchers_get_flow_log_status_0(client):
    """Test case for network_watchers_get_flow_log_status_0

    
    """
    parameters = {"targetResourceId":"targetResourceId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/queryFlowLogStatus'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_network_watchers_set_flow_log_configuration_0(client):
    """Test case for network_watchers_set_flow_log_configuration_0

    
    """
    parameters = {"targetResourceId":"targetResourceId","flowAnalyticsConfiguration":{"networkWatcherFlowAnalyticsConfiguration":{"workspaceResourceId":"workspaceResourceId","workspaceRegion":"workspaceRegion","enabled":True,"workspaceId":"workspaceId"}},"properties":{"retentionPolicy":{"days":0,"enabled":False},"enabled":True,"storageId":"storageId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/configureFlowLog'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

