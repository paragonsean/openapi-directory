# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.virtual_network_gateway import VirtualNetworkGateway
from openapi_server.models.virtual_network_gateway_list_result import VirtualNetworkGatewayListResult
from openapi_server.models.vpn_client_parameters import VpnClientParameters


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_virtual_network_gateways_create_or_update(client):
    """Test case for virtual_network_gateways_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"ipConfigurations":[{"name":"name","etag":"etag","properties":{"subnet":{"id":"id"},"privateIPAllocationMethod":"Static","provisioningState":"provisioningState","publicIPAddress":{"id":"id"}}},{"name":"name","etag":"etag","properties":{"subnet":{"id":"id"},"privateIPAllocationMethod":"Static","provisioningState":"provisioningState","publicIPAddress":{"id":"id"}}}],"enableBgp":True,"activeActive":True,"gatewayType":"Vpn","resourceGuid":"resourceGuid","bgpSettings":{"bgpPeeringAddress":"bgpPeeringAddress","asn":1,"peerWeight":5},"vpnClientConfiguration":{"vpnClientRevokedCertificates":[{"name":"name","etag":"etag","properties":{"thumbprint":"thumbprint","provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"thumbprint":"thumbprint","provisioningState":"provisioningState"}}],"vpnClientRootCertificates":[{"name":"name","etag":"etag","properties":{"provisioningState":"provisioningState","publicCertData":"publicCertData"}},{"name":"name","etag":"etag","properties":{"provisioningState":"provisioningState","publicCertData":"publicCertData"}}],"vpnClientAddressPool":{"addressPrefixes":["addressPrefixes","addressPrefixes"]}},"vpnType":"PolicyBased","provisioningState":"provisioningState","sku":{"tier":"Basic","name":"Basic","capacity":2},"gatewayDefaultSite":{"id":"id"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworkGateways/{virtual_network_gateway_name}'.format(resource_group_name='resource_group_name_example', virtual_network_gateway_name='virtual_network_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_gateways_delete(client):
    """Test case for virtual_network_gateways_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworkGateways/{virtual_network_gateway_name}'.format(resource_group_name='resource_group_name_example', virtual_network_gateway_name='virtual_network_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_virtual_network_gateways_generatevpnclientpackage(client):
    """Test case for virtual_network_gateways_generatevpnclientpackage

    
    """
    parameters = {"ProcessorArchitecture":"Amd64"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworkGateways/{virtual_network_gateway_name}/generatevpnclientpackage'.format(resource_group_name='resource_group_name_example', virtual_network_gateway_name='virtual_network_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_gateways_get(client):
    """Test case for virtual_network_gateways_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworkGateways/{virtual_network_gateway_name}'.format(resource_group_name='resource_group_name_example', virtual_network_gateway_name='virtual_network_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_gateways_list(client):
    """Test case for virtual_network_gateways_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworkGateways'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_virtual_network_gateways_reset(client):
    """Test case for virtual_network_gateways_reset

    
    """
    parameters = {"etag":"etag","properties":{"ipConfigurations":[{"name":"name","etag":"etag","properties":{"subnet":{"id":"id"},"privateIPAllocationMethod":"Static","provisioningState":"provisioningState","publicIPAddress":{"id":"id"}}},{"name":"name","etag":"etag","properties":{"subnet":{"id":"id"},"privateIPAllocationMethod":"Static","provisioningState":"provisioningState","publicIPAddress":{"id":"id"}}}],"enableBgp":True,"activeActive":True,"gatewayType":"Vpn","resourceGuid":"resourceGuid","bgpSettings":{"bgpPeeringAddress":"bgpPeeringAddress","asn":1,"peerWeight":5},"vpnClientConfiguration":{"vpnClientRevokedCertificates":[{"name":"name","etag":"etag","properties":{"thumbprint":"thumbprint","provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"thumbprint":"thumbprint","provisioningState":"provisioningState"}}],"vpnClientRootCertificates":[{"name":"name","etag":"etag","properties":{"provisioningState":"provisioningState","publicCertData":"publicCertData"}},{"name":"name","etag":"etag","properties":{"provisioningState":"provisioningState","publicCertData":"publicCertData"}}],"vpnClientAddressPool":{"addressPrefixes":["addressPrefixes","addressPrefixes"]}},"vpnType":"PolicyBased","provisioningState":"provisioningState","sku":{"tier":"Basic","name":"Basic","capacity":2},"gatewayDefaultSite":{"id":"id"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworkGateways/{virtual_network_gateway_name}/reset'.format(resource_group_name='resource_group_name_example', virtual_network_gateway_name='virtual_network_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

