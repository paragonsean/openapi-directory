# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.available_providers_list import AvailableProvidersList
from openapi_server.models.available_providers_list_parameters import AvailableProvidersListParameters
from openapi_server.models.azure_reachability_report import AzureReachabilityReport
from openapi_server.models.azure_reachability_report_parameters import AzureReachabilityReportParameters
from openapi_server.models.connectivity_information import ConnectivityInformation
from openapi_server.models.connectivity_parameters import ConnectivityParameters
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.flow_log_information import FlowLogInformation
from openapi_server.models.flow_log_status_parameters import FlowLogStatusParameters
from openapi_server.models.network_configuration_diagnostic_parameters import NetworkConfigurationDiagnosticParameters
from openapi_server.models.network_configuration_diagnostic_response import NetworkConfigurationDiagnosticResponse
from openapi_server.models.network_watcher import NetworkWatcher
from openapi_server.models.network_watcher_list_result import NetworkWatcherListResult
from openapi_server.models.network_watchers_update_tags_request import NetworkWatchersUpdateTagsRequest
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

async def test_network_watchers_check_connectivity(client):
    """Test case for network_watchers_check_connectivity

    
    """
    parameters = {"protocolConfiguration":{"HTTPConfiguration":{"headers":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"method":"Get","validStatusCodes":[6,6]}},"protocol":"Tcp","destination":{"resourceId":"resourceId","address":"address","port":0},"source":{"resourceId":"resourceId","port":1}}
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
        'Accept': 'application/json',
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

async def test_network_watchers_get_azure_reachability_report(client):
    """Test case for network_watchers_get_azure_reachability_report

    
    """
    parameters = {"providerLocation":{"country":"country","city":"city","state":"state"},"startTime":"2000-01-23T04:56:07.000+00:00","endTime":"2000-01-23T04:56:07.000+00:00","azureLocations":["azureLocations","azureLocations"],"providers":["providers","providers"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/azureReachabilityReport'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

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

async def test_network_watchers_get_network_configuration_diagnostic(client):
    """Test case for network_watchers_get_network_configuration_diagnostic

    
    """
    parameters = {"targetResourceId":"targetResourceId","profiles":[{"destinationPort":"destinationPort","protocol":"protocol","destination":"destination","source":"source","direction":"Inbound"},{"destinationPort":"destinationPort","protocol":"protocol","destination":"destination","source":"source","direction":"Inbound"}],"verbosityLevel":"Normal"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/networkConfigurationDiagnostic'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

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

async def test_network_watchers_get_topology(client):
    """Test case for network_watchers_get_topology

    
    """
    parameters = {"targetSubnet":{"id":"id"},"targetVirtualNetwork":{"id":"id"},"targetResourceGroupName":"targetResourceGroupName"}
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

async def test_network_watchers_list_available_providers(client):
    """Test case for network_watchers_list_available_providers

    
    """
    parameters = {"country":"country","city":"city","state":"state","azureLocations":["azureLocations","azureLocations"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}/availableProvidersList'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_network_watchers_set_flow_log_configuration(client):
    """Test case for network_watchers_set_flow_log_configuration

    
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


pytestmark = pytest.mark.asyncio

async def test_network_watchers_update_tags(client):
    """Test case for network_watchers_update_tags

    
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
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/networkWatchers/{network_watcher_name}'.format(resource_group_name='resource_group_name_example', network_watcher_name='network_watcher_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

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

