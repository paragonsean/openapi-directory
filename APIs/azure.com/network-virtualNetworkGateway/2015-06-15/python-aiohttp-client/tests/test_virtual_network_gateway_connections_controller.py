# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connection_reset_shared_key import ConnectionResetSharedKey
from openapi_server.models.connection_shared_key import ConnectionSharedKey
from openapi_server.models.connection_shared_key_result import ConnectionSharedKeyResult
from openapi_server.models.virtual_network_gateway_connection import VirtualNetworkGatewayConnection
from openapi_server.models.virtual_network_gateway_connection_list_result import VirtualNetworkGatewayConnectionListResult


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_virtual_network_gateway_connections_create_or_update(client):
    """Test case for virtual_network_gateway_connections_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"sharedKey":"sharedKey","authorizationKey":"authorizationKey","ingressBytesTransferred":6,"resourceGuid":"resourceGuid","routingWeight":5,"provisioningState":"provisioningState","connectionType":"IPsec","enableBgp":True,"peer":{"id":"id"},"localNetworkGateway2":{"etag":"etag","properties":{"localNetworkAddressSpace":{"addressPrefixes":["addressPrefixes","addressPrefixes"]},"resourceGuid":"resourceGuid","gatewayIpAddress":"gatewayIpAddress","bgpSettings":{"bgpPeeringAddress":"bgpPeeringAddress","asn":1,"peerWeight":5},"provisioningState":"provisioningState"}},"connectionStatus":"Unknown","virtualNetworkGateway1":{"etag":"etag","properties":{"ipConfigurations":[{"name":"name","etag":"etag","properties":{"subnet":{"id":"id"},"privateIPAllocationMethod":"Static","privateIPAddress":"privateIPAddress","provisioningState":"provisioningState","publicIPAddress":{"id":"id"}}},{"name":"name","etag":"etag","properties":{"subnet":{"id":"id"},"privateIPAllocationMethod":"Static","privateIPAddress":"privateIPAddress","provisioningState":"provisioningState","publicIPAddress":{"id":"id"}}}],"enableBgp":True,"gatewayType":"Vpn","resourceGuid":"resourceGuid","bgpSettings":{"bgpPeeringAddress":"bgpPeeringAddress","asn":1,"peerWeight":5},"vpnClientConfiguration":{"vpnClientRevokedCertificates":[{"name":"name","etag":"etag","properties":{"thumbprint":"thumbprint","provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"thumbprint":"thumbprint","provisioningState":"provisioningState"}}],"vpnClientRootCertificates":[{"name":"name","etag":"etag","properties":{"provisioningState":"provisioningState","publicCertData":"publicCertData"}},{"name":"name","etag":"etag","properties":{"provisioningState":"provisioningState","publicCertData":"publicCertData"}}],"vpnClientAddressPool":{"addressPrefixes":["addressPrefixes","addressPrefixes"]}},"vpnType":"PolicyBased","provisioningState":"provisioningState","sku":{"tier":"Basic","name":"Basic","capacity":2},"gatewayDefaultSite":{"id":"id"}}},"virtualNetworkGateway2":{"etag":"etag","properties":{"ipConfigurations":[{"name":"name","etag":"etag","properties":{"subnet":{"id":"id"},"privateIPAllocationMethod":"Static","privateIPAddress":"privateIPAddress","provisioningState":"provisioningState","publicIPAddress":{"id":"id"}}},{"name":"name","etag":"etag","properties":{"subnet":{"id":"id"},"privateIPAllocationMethod":"Static","privateIPAddress":"privateIPAddress","provisioningState":"provisioningState","publicIPAddress":{"id":"id"}}}],"enableBgp":True,"gatewayType":"Vpn","resourceGuid":"resourceGuid","bgpSettings":{"bgpPeeringAddress":"bgpPeeringAddress","asn":1,"peerWeight":5},"vpnClientConfiguration":{"vpnClientRevokedCertificates":[{"name":"name","etag":"etag","properties":{"thumbprint":"thumbprint","provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"thumbprint":"thumbprint","provisioningState":"provisioningState"}}],"vpnClientRootCertificates":[{"name":"name","etag":"etag","properties":{"provisioningState":"provisioningState","publicCertData":"publicCertData"}},{"name":"name","etag":"etag","properties":{"provisioningState":"provisioningState","publicCertData":"publicCertData"}}],"vpnClientAddressPool":{"addressPrefixes":["addressPrefixes","addressPrefixes"]}},"vpnType":"PolicyBased","provisioningState":"provisioningState","sku":{"tier":"Basic","name":"Basic","capacity":2},"gatewayDefaultSite":{"id":"id"}}},"egressBytesTransferred":0}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/connections/{virtual_network_gateway_connection_name}'.format(resource_group_name='resource_group_name_example', virtual_network_gateway_connection_name='virtual_network_gateway_connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_gateway_connections_delete(client):
    """Test case for virtual_network_gateway_connections_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/connections/{virtual_network_gateway_connection_name}'.format(resource_group_name='resource_group_name_example', virtual_network_gateway_connection_name='virtual_network_gateway_connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_gateway_connections_get(client):
    """Test case for virtual_network_gateway_connections_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/connections/{virtual_network_gateway_connection_name}'.format(resource_group_name='resource_group_name_example', virtual_network_gateway_connection_name='virtual_network_gateway_connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_gateway_connections_get_shared_key(client):
    """Test case for virtual_network_gateway_connections_get_shared_key

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/connections/{virtual_network_gateway_connection_name}/sharedkey'.format(resource_group_name='resource_group_name_example', virtual_network_gateway_connection_name='virtual_network_gateway_connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_gateway_connections_list(client):
    """Test case for virtual_network_gateway_connections_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/connections'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_virtual_network_gateway_connections_reset_shared_key(client):
    """Test case for virtual_network_gateway_connections_reset_shared_key

    
    """
    parameters = {"keyLength":0}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/connections/{virtual_network_gateway_connection_name}/sharedkey/reset'.format(resource_group_name='resource_group_name_example', virtual_network_gateway_connection_name='virtual_network_gateway_connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_virtual_network_gateway_connections_set_shared_key(client):
    """Test case for virtual_network_gateway_connections_set_shared_key

    
    """
    parameters = {"value":"value"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/connections/{virtual_network_gateway_connection_name}/sharedkey'.format(resource_group_name='resource_group_name_example', virtual_network_gateway_connection_name='virtual_network_gateway_connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

