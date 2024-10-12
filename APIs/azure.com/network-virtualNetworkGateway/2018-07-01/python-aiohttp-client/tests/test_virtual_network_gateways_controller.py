# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bgp_peer_status_list_result import BgpPeerStatusListResult
from openapi_server.models.gateway_route_list_result import GatewayRouteListResult
from openapi_server.models.virtual_network_gateway import VirtualNetworkGateway
from openapi_server.models.virtual_network_gateway_connections_update_tags_request import VirtualNetworkGatewayConnectionsUpdateTagsRequest
from openapi_server.models.virtual_network_gateway_list_connections_result import VirtualNetworkGatewayListConnectionsResult
from openapi_server.models.virtual_network_gateway_list_result import VirtualNetworkGatewayListResult
from openapi_server.models.vpn_client_i_psec_parameters import VpnClientIPsecParameters
from openapi_server.models.vpn_client_parameters import VpnClientParameters
from openapi_server.models.vpn_device_script_parameters import VpnDeviceScriptParameters


pytestmark = pytest.mark.asyncio

async def test_virtual_network_gateways_create_or_update(client):
    """Test case for virtual_network_gateways_create_or_update

    
    """
    parameters = {"etag":"etag","properties":{"ipConfigurations":[{"name":"name","etag":"etag","properties":{"subnet":{"id":"id"},"privateIPAllocationMethod":"Static","provisioningState":"provisioningState","publicIPAddress":{"id":"id"}}},{"name":"name","etag":"etag","properties":{"subnet":{"id":"id"},"privateIPAllocationMethod":"Static","provisioningState":"provisioningState","publicIPAddress":{"id":"id"}}}],"enableBgp":True,"activeActive":True,"gatewayType":"Vpn","resourceGuid":"resourceGuid","bgpSettings":{"bgpPeeringAddress":"bgpPeeringAddress","asn":5,"peerWeight":2},"vpnClientConfiguration":{"radiusServerSecret":"radiusServerSecret","vpnClientRevokedCertificates":[{"name":"name","etag":"etag","properties":{"thumbprint":"thumbprint","provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"thumbprint":"thumbprint","provisioningState":"provisioningState"}}],"radiusServerAddress":"radiusServerAddress","vpnClientRootCertificates":[{"name":"name","etag":"etag","properties":{"provisioningState":"provisioningState","publicCertData":"publicCertData"}},{"name":"name","etag":"etag","properties":{"provisioningState":"provisioningState","publicCertData":"publicCertData"}}],"vpnClientIpsecPolicies":[{"ikeIntegrity":"MD5","ikeEncryption":"DES","ipsecIntegrity":"MD5","pfsGroup":"None","saDataSizeKilobytes":1,"saLifeTimeSeconds":5,"dhGroup":"None","ipsecEncryption":"None"},{"ikeIntegrity":"MD5","ikeEncryption":"DES","ipsecIntegrity":"MD5","pfsGroup":"None","saDataSizeKilobytes":1,"saLifeTimeSeconds":5,"dhGroup":"None","ipsecEncryption":"None"}],"vpnClientAddressPool":{"addressPrefixes":["addressPrefixes","addressPrefixes"]},"vpnClientProtocols":["IkeV2","IkeV2"]},"vpnType":"PolicyBased","provisioningState":"provisioningState","sku":{"tier":"Basic","name":"Basic","capacity":2},"gatewayDefaultSite":{"id":"id"}}}
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

async def test_virtual_network_gateways_generate_vpn_profile(client):
    """Test case for virtual_network_gateways_generate_vpn_profile

    
    """
    parameters = {"clientRootCertificates":["clientRootCertificates","clientRootCertificates"],"authenticationMethod":"EAPTLS","radiusServerAuthCertificate":"radiusServerAuthCertificate","processorArchitecture":"Amd64"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworkGateways/{virtual_network_gateway_name}/generatevpnprofile'.format(resource_group_name='resource_group_name_example', virtual_network_gateway_name='virtual_network_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_gateways_generatevpnclientpackage(client):
    """Test case for virtual_network_gateways_generatevpnclientpackage

    
    """
    parameters = {"clientRootCertificates":["clientRootCertificates","clientRootCertificates"],"authenticationMethod":"EAPTLS","radiusServerAuthCertificate":"radiusServerAuthCertificate","processorArchitecture":"Amd64"}
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

async def test_virtual_network_gateways_get_advertised_routes(client):
    """Test case for virtual_network_gateways_get_advertised_routes

    
    """
    params = [('peer', 'peer_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworkGateways/{virtual_network_gateway_name}/getAdvertisedRoutes'.format(resource_group_name='resource_group_name_example', virtual_network_gateway_name='virtual_network_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_gateways_get_bgp_peer_status(client):
    """Test case for virtual_network_gateways_get_bgp_peer_status

    
    """
    params = [('peer', 'peer_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworkGateways/{virtual_network_gateway_name}/getBgpPeerStatus'.format(resource_group_name='resource_group_name_example', virtual_network_gateway_name='virtual_network_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_gateways_get_learned_routes(client):
    """Test case for virtual_network_gateways_get_learned_routes

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworkGateways/{virtual_network_gateway_name}/getLearnedRoutes'.format(resource_group_name='resource_group_name_example', virtual_network_gateway_name='virtual_network_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_gateways_get_vpn_profile_package_url(client):
    """Test case for virtual_network_gateways_get_vpn_profile_package_url

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworkGateways/{virtual_network_gateway_name}/getvpnprofilepackageurl'.format(resource_group_name='resource_group_name_example', virtual_network_gateway_name='virtual_network_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_gateways_get_vpnclient_ipsec_parameters(client):
    """Test case for virtual_network_gateways_get_vpnclient_ipsec_parameters

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworkGateways/{virtual_network_gateway_name}/getvpnclientipsecparameters'.format(resource_group_name='resource_group_name_example', virtual_network_gateway_name='virtual_network_gateway_name_example', subscription_id='subscription_id_example'),
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

async def test_virtual_network_gateways_list_connections(client):
    """Test case for virtual_network_gateways_list_connections

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworkGateways/{virtual_network_gateway_name}/connections'.format(resource_group_name='resource_group_name_example', virtual_network_gateway_name='virtual_network_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_gateways_reset(client):
    """Test case for virtual_network_gateways_reset

    
    """
    params = [('gatewayVip', 'gateway_vip_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworkGateways/{virtual_network_gateway_name}/reset'.format(resource_group_name='resource_group_name_example', virtual_network_gateway_name='virtual_network_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_gateways_set_vpnclient_ipsec_parameters(client):
    """Test case for virtual_network_gateways_set_vpnclient_ipsec_parameters

    
    """
    vpnclient_ipsec_params = {"ikeIntegrity":"MD5","ikeEncryption":"DES","ipsecIntegrity":"MD5","pfsGroup":"None","saDataSizeKilobytes":0,"saLifeTimeSeconds":6,"dhGroup":"None","ipsecEncryption":"None"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworkGateways/{virtual_network_gateway_name}/setvpnclientipsecparameters'.format(resource_group_name='resource_group_name_example', virtual_network_gateway_name='virtual_network_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=vpnclient_ipsec_params,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_gateways_supported_vpn_devices(client):
    """Test case for virtual_network_gateways_supported_vpn_devices

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworkGateways/{virtual_network_gateway_name}/supportedvpndevices'.format(resource_group_name='resource_group_name_example', virtual_network_gateway_name='virtual_network_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_gateways_update_tags(client):
    """Test case for virtual_network_gateways_update_tags

    
    """
    parameters = openapi_server.VirtualNetworkGatewayConnectionsUpdateTagsRequest()
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualNetworkGateways/{virtual_network_gateway_name}'.format(resource_group_name='resource_group_name_example', virtual_network_gateway_name='virtual_network_gateway_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_network_gateways_vpn_device_configuration_script(client):
    """Test case for virtual_network_gateways_vpn_device_configuration_script

    
    """
    parameters = {"vendor":"vendor","deviceFamily":"deviceFamily","firmwareVersion":"firmwareVersion"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/connections/{virtual_network_gateway_connection_name}/vpndeviceconfigurationscript'.format(resource_group_name='resource_group_name_example', virtual_network_gateway_connection_name='virtual_network_gateway_connection_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

