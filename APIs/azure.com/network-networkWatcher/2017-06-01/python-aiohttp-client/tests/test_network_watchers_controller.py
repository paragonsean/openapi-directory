# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connectivity_information import ConnectivityInformation
from openapi_server.models.connectivity_parameters import ConnectivityParameters
from openapi_server.models.flow_log_information import FlowLogInformation
from openapi_server.models.flow_log_status_parameters import FlowLogStatusParameters
from openapi_server.models.network_watcher import NetworkWatcher
from openapi_server.models.network_watcher_list_result import NetworkWatcherListResult
from openapi_server.models.next_hop_parameters import NextHopParameters
from openapi_server.models.next_hop_result import NextHopResult
from openapi_server.models.query_troubleshooting_parameters import QueryTroubleshootingParameters
from openapi_server.models.security_group_view_parameters import SecurityGroupViewParameters
from openapi_server.models.security_group_view_result import SecurityGroupViewResult
from openapi_server.models.topology import Topology
from openapi_server.models.topology_parameters import TopologyParameters
from openapi_server.models.troubleshooting_parameters import TroubleshootingParameters
from openapi_server.models.troubleshooting_result import TroubleshootingResult
from openapi_server.models.verification_ip_flow_parameters import VerificationIPFlowParameters
from openapi_server.models.verification_ip_flow_result import VerificationIPFlowResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_network_watchers_check_connectivity(client):
    """Test case for network_watchers_check_connectivity

    
    """
    parameters = {"destination":{"resourceId":"resourceId","address":"address","port":0},"source":{"resourceId":"resourceId","port":6}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/connectivityCheck'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_network_watchers_create_or_update(client):
    """Test case for network_watchers_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"provisioningState":"Succeeded"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_watchers_delete(client):
    """Test case for network_watchers_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_watchers_get(client):
    """Test case for network_watchers_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_network_watchers_get_flow_log_status(client):
    """Test case for network_watchers_get_flow_log_status

    
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
async def test_network_watchers_get_next_hop(client):
    """Test case for network_watchers_get_next_hop

    
    """
    parameters = {"targetResourceId":"targetResourceId","destinationIPAddress":"destinationIPAddress","sourceIPAddress":"sourceIPAddress","targetNicResourceId":"targetNicResourceId"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/nextHop'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_network_watchers_get_topology(client):
    """Test case for network_watchers_get_topology

    
    """
    parameters = {"targetResourceGroupName":"targetResourceGroupName"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/topology'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_network_watchers_get_troubleshooting(client):
    """Test case for network_watchers_get_troubleshooting

    
    """
    parameters = {"targetResourceId":"targetResourceId","properties":{"storagePath":"storagePath","storageId":"storageId"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/troubleshoot'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_network_watchers_get_troubleshooting_result(client):
    """Test case for network_watchers_get_troubleshooting_result

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/queryTroubleshootResult'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_network_watchers_get_vm_security_rules(client):
    """Test case for network_watchers_get_vm_security_rules

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/securityGroupView'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_watchers_list(client):
    """Test case for network_watchers_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_watchers_list_all(client):
    """Test case for network_watchers_list_all

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/networkWatchers'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_network_watchers_set_flow_log_configuration(client):
    """Test case for network_watchers_set_flow_log_configuration

    
    """
    parameters = {"targetResourceId":"targetResourceId","properties":{"retentionPolicy":{"days":0,"enabled":False},"enabled":True,"storageId":"storageId"}}
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


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_network_watchers_verify_ip_flow(client):
    """Test case for network_watchers_verify_ip_flow

    
    """
    parameters = {"targetResourceId":"targetResourceId","protocol":"TCP","localPort":"localPort","remoteIPAddress":"remoteIPAddress","targetNicResourceId":"targetNicResourceId","remotePort":"remotePort","localIPAddress":"localIPAddress","direction":"Inbound"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/ipFlowVerify'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

