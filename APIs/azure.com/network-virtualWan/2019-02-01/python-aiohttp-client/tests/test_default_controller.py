# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_vpn_sites_configuration_request import GetVpnSitesConfigurationRequest
from openapi_server.models.hub_virtual_network_connection import HubVirtualNetworkConnection
from openapi_server.models.list_hub_virtual_network_connections_result import ListHubVirtualNetworkConnectionsResult
from openapi_server.models.list_p2_s_vpn_gateways_result import ListP2SVpnGatewaysResult
from openapi_server.models.list_p2_s_vpn_server_configurations_result import ListP2SVpnServerConfigurationsResult
from openapi_server.models.list_virtual_hubs_result import ListVirtualHubsResult
from openapi_server.models.list_virtual_wans_result import ListVirtualWANsResult
from openapi_server.models.list_vpn_connections_result import ListVpnConnectionsResult
from openapi_server.models.list_vpn_gateways_result import ListVpnGatewaysResult
from openapi_server.models.list_vpn_sites_result import ListVpnSitesResult
from openapi_server.models.p2_s_vpn_gateway import P2SVpnGateway
from openapi_server.models.p2_s_vpn_server_configuration import P2SVpnServerConfiguration
from openapi_server.models.p2s_vpn_gateways_list_default_response import P2sVpnGatewaysListDefaultResponse
from openapi_server.models.virtual_hub import VirtualHub
from openapi_server.models.virtual_wan import VirtualWAN
from openapi_server.models.virtual_wan_security_providers import VirtualWanSecurityProviders
from openapi_server.models.vpn_connection import VpnConnection
from openapi_server.models.vpn_gateway import VpnGateway
from openapi_server.models.vpn_site import VpnSite


pytestmark = pytest.mark.asyncio

async def test_hub_virtual_network_connections_get(client):
    """Test case for hub_virtual_network_connections_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualHubs/{virtual_hub_name}/hubVirtualNetworkConnections/{connection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', virtual_hub_name='virtual_hub_name_example', connection_name='connection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hub_virtual_network_connections_list(client):
    """Test case for hub_virtual_network_connections_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualHubs/{virtual_hub_name}/hubVirtualNetworkConnections'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', virtual_hub_name='virtual_hub_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p2s_vpn_gateways_create_or_update(client):
    """Test case for p2s_vpn_gateways_create_or_update

    
    """
    p2_s_vpn_gateway_parameters = {"etag":"etag","properties":{"vpnClientConnectionHealth":{"totalEgressBytesTransferred":0,"allocatedIpAddresses":["allocatedIpAddresses","allocatedIpAddresses"],"totalIngressBytesTransferred":6,"vpnClientConnectionsCount":1},"customRoutes":{"addressPrefixes":["addressPrefixes","addressPrefixes"]},"vpnGatewayScaleUnit":5,"p2SVpnServerConfiguration":{"id":"id"},"provisioningState":"Succeeded","vpnClientAddressPool":{"addressPrefixes":["addressPrefixes","addressPrefixes"]},"virtualHub":{"id":"id"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/p2svpnGateways/{gateway_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gateway_name='gateway_name_example'),
        headers=headers,
        json=p2_s_vpn_gateway_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p2s_vpn_gateways_delete(client):
    """Test case for p2s_vpn_gateways_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/p2svpnGateways/{gateway_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gateway_name='gateway_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p2s_vpn_gateways_get(client):
    """Test case for p2s_vpn_gateways_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/p2svpnGateways/{gateway_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gateway_name='gateway_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p2s_vpn_gateways_list(client):
    """Test case for p2s_vpn_gateways_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/p2svpnGateways'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p2s_vpn_gateways_list_by_resource_group(client):
    """Test case for p2s_vpn_gateways_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/p2svpnGateways'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p2s_vpn_server_configurations_create_or_update(client):
    """Test case for p2s_vpn_server_configurations_create_or_update

    
    """
    p2_s_vpn_server_configuration_parameters = {"name":"name","etag":"etag","properties":{"p2SVpnServerConfigRadiusServerRootCertificates":[{"name":"name","etag":"etag","properties":{"provisioningState":"provisioningState","publicCertData":"publicCertData"}},{"name":"name","etag":"etag","properties":{"provisioningState":"provisioningState","publicCertData":"publicCertData"}}],"radiusServerSecret":"radiusServerSecret","name":"name","p2SVpnServerConfigVpnClientRevokedCertificates":[{"name":"name","etag":"etag","properties":{"thumbprint":"thumbprint","provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"thumbprint":"thumbprint","provisioningState":"provisioningState"}}],"radiusServerAddress":"radiusServerAddress","etag":"etag","vpnClientIpsecPolicies":[{"ikeIntegrity":"MD5","ikeEncryption":"DES","ipsecIntegrity":"MD5","pfsGroup":"None","saDataSizeKilobytes":0,"saLifeTimeSeconds":6,"dhGroup":"None","ipsecEncryption":"None"},{"ikeIntegrity":"MD5","ikeEncryption":"DES","ipsecIntegrity":"MD5","pfsGroup":"None","saDataSizeKilobytes":0,"saLifeTimeSeconds":6,"dhGroup":"None","ipsecEncryption":"None"}],"p2SVpnServerConfigVpnClientRootCertificates":[{"name":"name","etag":"etag","properties":{"provisioningState":"provisioningState","publicCertData":"publicCertData"}},{"name":"name","etag":"etag","properties":{"provisioningState":"provisioningState","publicCertData":"publicCertData"}}],"provisioningState":"provisioningState","p2SVpnGateways":[{"id":"id"},{"id":"id"}],"p2SVpnServerConfigRadiusClientRootCertificates":[{"name":"name","etag":"etag","properties":{"thumbprint":"thumbprint","provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"thumbprint":"thumbprint","provisioningState":"provisioningState"}}],"vpnProtocols":["IkeV2","IkeV2"]}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualWans/{virtual_wan_name}/p2sVpnServerConfigurations/{p2_s_vpn_server_configuration_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', virtual_wan_name='virtual_wan_name_example', p2_s_vpn_server_configuration_name='p2_s_vpn_server_configuration_name_example'),
        headers=headers,
        json=p2_s_vpn_server_configuration_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p2s_vpn_server_configurations_delete(client):
    """Test case for p2s_vpn_server_configurations_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualWans/{virtual_wan_name}/p2sVpnServerConfigurations/{p2_s_vpn_server_configuration_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', virtual_wan_name='virtual_wan_name_example', p2_s_vpn_server_configuration_name='p2_s_vpn_server_configuration_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p2s_vpn_server_configurations_get(client):
    """Test case for p2s_vpn_server_configurations_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualWans/{virtual_wan_name}/p2sVpnServerConfigurations/{p2_s_vpn_server_configuration_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', virtual_wan_name='virtual_wan_name_example', p2_s_vpn_server_configuration_name='p2_s_vpn_server_configuration_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_p2s_vpn_server_configurations_list_by_virtual_wan(client):
    """Test case for p2s_vpn_server_configurations_list_by_virtual_wan

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualWans/{virtual_wan_name}/p2sVpnServerConfigurations'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', virtual_wan_name='virtual_wan_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_supported_security_providers(client):
    """Test case for supported_security_providers

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualWans/{virtual_wan_name}/supportedSecurityProviders'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', virtual_wan_name='virtual_wan_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_hubs_create_or_update(client):
    """Test case for virtual_hubs_create_or_update

    
    """
    virtual_hub_parameters = {"etag":"etag","properties":{"expressRouteGateway":{"id":"id"},"routeTable":{"routes":[{"addressPrefixes":["addressPrefixes","addressPrefixes"],"nextHopIpAddress":"nextHopIpAddress"},{"addressPrefixes":["addressPrefixes","addressPrefixes"],"nextHopIpAddress":"nextHopIpAddress"}]},"addressPrefix":"addressPrefix","p2SVpnGateway":{"id":"id"},"virtualNetworkConnections":[{"name":"name","etag":"etag","properties":{"allowHubToRemoteVnetTransit":True,"remoteVirtualNetwork":{"id":"id"},"enableInternetSecurity":True,"allowRemoteVnetToUseHubVnetGateways":True,"provisioningState":"Succeeded"}},{"name":"name","etag":"etag","properties":{"allowHubToRemoteVnetTransit":True,"remoteVirtualNetwork":{"id":"id"},"enableInternetSecurity":True,"allowRemoteVnetToUseHubVnetGateways":True,"provisioningState":"Succeeded"}}],"provisioningState":"Succeeded","virtualWan":{"id":"id"},"vpnGateway":{"id":"id"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualHubs/{virtual_hub_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', virtual_hub_name='virtual_hub_name_example'),
        headers=headers,
        json=virtual_hub_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_hubs_delete(client):
    """Test case for virtual_hubs_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualHubs/{virtual_hub_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', virtual_hub_name='virtual_hub_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_hubs_get(client):
    """Test case for virtual_hubs_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualHubs/{virtual_hub_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', virtual_hub_name='virtual_hub_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_hubs_list(client):
    """Test case for virtual_hubs_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/virtualHubs'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_hubs_list_by_resource_group(client):
    """Test case for virtual_hubs_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualHubs'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_wans_create_or_update(client):
    """Test case for virtual_wans_create_or_update

    
    """
    wan_parameters = {"etag":"etag","properties":{"p2SVpnServerConfigurations":[{"name":"name","etag":"etag","properties":{"p2SVpnServerConfigRadiusServerRootCertificates":[{"name":"name","etag":"etag","properties":{"provisioningState":"provisioningState","publicCertData":"publicCertData"}},{"name":"name","etag":"etag","properties":{"provisioningState":"provisioningState","publicCertData":"publicCertData"}}],"radiusServerSecret":"radiusServerSecret","name":"name","p2SVpnServerConfigVpnClientRevokedCertificates":[{"name":"name","etag":"etag","properties":{"thumbprint":"thumbprint","provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"thumbprint":"thumbprint","provisioningState":"provisioningState"}}],"radiusServerAddress":"radiusServerAddress","etag":"etag","vpnClientIpsecPolicies":[{"ikeIntegrity":"MD5","ikeEncryption":"DES","ipsecIntegrity":"MD5","pfsGroup":"None","saDataSizeKilobytes":0,"saLifeTimeSeconds":6,"dhGroup":"None","ipsecEncryption":"None"},{"ikeIntegrity":"MD5","ikeEncryption":"DES","ipsecIntegrity":"MD5","pfsGroup":"None","saDataSizeKilobytes":0,"saLifeTimeSeconds":6,"dhGroup":"None","ipsecEncryption":"None"}],"p2SVpnServerConfigVpnClientRootCertificates":[{"name":"name","etag":"etag","properties":{"provisioningState":"provisioningState","publicCertData":"publicCertData"}},{"name":"name","etag":"etag","properties":{"provisioningState":"provisioningState","publicCertData":"publicCertData"}}],"provisioningState":"provisioningState","p2SVpnGateways":[{"id":"id"},{"id":"id"}],"p2SVpnServerConfigRadiusClientRootCertificates":[{"name":"name","etag":"etag","properties":{"thumbprint":"thumbprint","provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"thumbprint":"thumbprint","provisioningState":"provisioningState"}}],"vpnProtocols":["IkeV2","IkeV2"]}},{"name":"name","etag":"etag","properties":{"p2SVpnServerConfigRadiusServerRootCertificates":[{"name":"name","etag":"etag","properties":{"provisioningState":"provisioningState","publicCertData":"publicCertData"}},{"name":"name","etag":"etag","properties":{"provisioningState":"provisioningState","publicCertData":"publicCertData"}}],"radiusServerSecret":"radiusServerSecret","name":"name","p2SVpnServerConfigVpnClientRevokedCertificates":[{"name":"name","etag":"etag","properties":{"thumbprint":"thumbprint","provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"thumbprint":"thumbprint","provisioningState":"provisioningState"}}],"radiusServerAddress":"radiusServerAddress","etag":"etag","vpnClientIpsecPolicies":[{"ikeIntegrity":"MD5","ikeEncryption":"DES","ipsecIntegrity":"MD5","pfsGroup":"None","saDataSizeKilobytes":0,"saLifeTimeSeconds":6,"dhGroup":"None","ipsecEncryption":"None"},{"ikeIntegrity":"MD5","ikeEncryption":"DES","ipsecIntegrity":"MD5","pfsGroup":"None","saDataSizeKilobytes":0,"saLifeTimeSeconds":6,"dhGroup":"None","ipsecEncryption":"None"}],"p2SVpnServerConfigVpnClientRootCertificates":[{"name":"name","etag":"etag","properties":{"provisioningState":"provisioningState","publicCertData":"publicCertData"}},{"name":"name","etag":"etag","properties":{"provisioningState":"provisioningState","publicCertData":"publicCertData"}}],"provisioningState":"provisioningState","p2SVpnGateways":[{"id":"id"},{"id":"id"}],"p2SVpnServerConfigRadiusClientRootCertificates":[{"name":"name","etag":"etag","properties":{"thumbprint":"thumbprint","provisioningState":"provisioningState"}},{"name":"name","etag":"etag","properties":{"thumbprint":"thumbprint","provisioningState":"provisioningState"}}],"vpnProtocols":["IkeV2","IkeV2"]}}],"vpnSites":[{"id":"id"},{"id":"id"}],"office365LocalBreakoutCategory":"Optimize","virtualHubs":[{"id":"id"},{"id":"id"}],"allowBranchToBranchTraffic":True,"allowVnetToVnetTraffic":True,"provisioningState":"Succeeded","securityProviderName":"securityProviderName","disableVpnEncryption":True}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualWans/{virtual_wan_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', virtual_wan_name='virtual_wan_name_example'),
        headers=headers,
        json=wan_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_wans_delete(client):
    """Test case for virtual_wans_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualWans/{virtual_wan_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', virtual_wan_name='virtual_wan_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_wans_get(client):
    """Test case for virtual_wans_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualWans/{virtual_wan_name}'.format(resource_group_name='resource_group_name_example', virtual_wan_name='virtual_wan_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_wans_list(client):
    """Test case for virtual_wans_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/virtualWans'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_virtual_wans_list_by_resource_group(client):
    """Test case for virtual_wans_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualWans'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vpn_connections_create_or_update(client):
    """Test case for vpn_connections_create_or_update

    
    """
    vpn_connection_parameters = {"name":"name","etag":"etag","properties":{"sharedKey":"sharedKey","vpnConnectionProtocolType":"IKEv2","ingressBytesTransferred":5,"enableRateLimiting":True,"useLocalAzureIpAddress":True,"routingWeight":2,"provisioningState":"Succeeded","ipsecPolicies":[{"ikeIntegrity":"MD5","ikeEncryption":"DES","ipsecIntegrity":"MD5","pfsGroup":"None","saDataSizeKilobytes":0,"saLifeTimeSeconds":6,"dhGroup":"None","ipsecEncryption":"None"},{"ikeIntegrity":"MD5","ikeEncryption":"DES","ipsecIntegrity":"MD5","pfsGroup":"None","saDataSizeKilobytes":0,"saLifeTimeSeconds":6,"dhGroup":"None","ipsecEncryption":"None"}],"enableBgp":True,"connectionBandwidth":1,"enableInternetSecurity":True,"connectionStatus":"Unknown","remoteVpnSite":{"id":"id"},"egressBytesTransferred":5}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/vpnGateways/{gateway_name}/vpnConnections/{connection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gateway_name='gateway_name_example', connection_name='connection_name_example'),
        headers=headers,
        json=vpn_connection_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vpn_connections_delete(client):
    """Test case for vpn_connections_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/vpnGateways/{gateway_name}/vpnConnections/{connection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gateway_name='gateway_name_example', connection_name='connection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vpn_connections_get(client):
    """Test case for vpn_connections_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/vpnGateways/{gateway_name}/vpnConnections/{connection_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gateway_name='gateway_name_example', connection_name='connection_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vpn_connections_list_by_vpn_gateway(client):
    """Test case for vpn_connections_list_by_vpn_gateway

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/vpnGateways/{gateway_name}/vpnConnections'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gateway_name='gateway_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vpn_gateways_create_or_update(client):
    """Test case for vpn_gateways_create_or_update

    
    """
    vpn_gateway_parameters = {"etag":"etag","properties":{"bgpSettings":{"bgpPeeringAddress":"bgpPeeringAddress","asn":0,"peerWeight":6},"vpnGatewayScaleUnit":7,"provisioningState":"Succeeded","connections":[{"name":"name","etag":"etag","properties":{"sharedKey":"sharedKey","vpnConnectionProtocolType":"IKEv2","ingressBytesTransferred":5,"enableRateLimiting":True,"useLocalAzureIpAddress":True,"routingWeight":2,"provisioningState":"Succeeded","ipsecPolicies":[{"ikeIntegrity":"MD5","ikeEncryption":"DES","ipsecIntegrity":"MD5","pfsGroup":"None","saDataSizeKilobytes":0,"saLifeTimeSeconds":6,"dhGroup":"None","ipsecEncryption":"None"},{"ikeIntegrity":"MD5","ikeEncryption":"DES","ipsecIntegrity":"MD5","pfsGroup":"None","saDataSizeKilobytes":0,"saLifeTimeSeconds":6,"dhGroup":"None","ipsecEncryption":"None"}],"enableBgp":True,"connectionBandwidth":1,"enableInternetSecurity":True,"connectionStatus":"Unknown","remoteVpnSite":{"id":"id"},"egressBytesTransferred":5}},{"name":"name","etag":"etag","properties":{"sharedKey":"sharedKey","vpnConnectionProtocolType":"IKEv2","ingressBytesTransferred":5,"enableRateLimiting":True,"useLocalAzureIpAddress":True,"routingWeight":2,"provisioningState":"Succeeded","ipsecPolicies":[{"ikeIntegrity":"MD5","ikeEncryption":"DES","ipsecIntegrity":"MD5","pfsGroup":"None","saDataSizeKilobytes":0,"saLifeTimeSeconds":6,"dhGroup":"None","ipsecEncryption":"None"},{"ikeIntegrity":"MD5","ikeEncryption":"DES","ipsecIntegrity":"MD5","pfsGroup":"None","saDataSizeKilobytes":0,"saLifeTimeSeconds":6,"dhGroup":"None","ipsecEncryption":"None"}],"enableBgp":True,"connectionBandwidth":1,"enableInternetSecurity":True,"connectionStatus":"Unknown","remoteVpnSite":{"id":"id"},"egressBytesTransferred":5}}],"virtualHub":{"id":"id"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/vpnGateways/{gateway_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gateway_name='gateway_name_example'),
        headers=headers,
        json=vpn_gateway_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vpn_gateways_delete(client):
    """Test case for vpn_gateways_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/vpnGateways/{gateway_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gateway_name='gateway_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vpn_gateways_get(client):
    """Test case for vpn_gateways_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/vpnGateways/{gateway_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', gateway_name='gateway_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vpn_gateways_list(client):
    """Test case for vpn_gateways_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/vpnGateways'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vpn_gateways_list_by_resource_group(client):
    """Test case for vpn_gateways_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/vpnGateways'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vpn_sites_configuration_download(client):
    """Test case for vpn_sites_configuration_download

    
    """
    request = {"outputBlobSasUrl":"outputBlobSasUrl","vpnSites":["vpnSites","vpnSites"]}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/virtualWans/{virtual_wan_name}/vpnConfiguration'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', virtual_wan_name='virtual_wan_name_example'),
        headers=headers,
        json=request,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vpn_sites_create_or_update(client):
    """Test case for vpn_sites_create_or_update

    
    """
    vpn_site_parameters = {"etag":"etag","properties":{"bgpProperties":{"bgpPeeringAddress":"bgpPeeringAddress","asn":0,"peerWeight":6},"siteKey":"siteKey","addressSpace":{"addressPrefixes":["addressPrefixes","addressPrefixes"]},"deviceProperties":{"deviceVendor":"deviceVendor","deviceModel":"deviceModel","linkSpeedInMbps":0},"ipAddress":"ipAddress","isSecuritySite":True,"provisioningState":"Succeeded","virtualWan":{"id":"id"}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/vpnSites/{vpn_site_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', vpn_site_name='vpn_site_name_example'),
        headers=headers,
        json=vpn_site_parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vpn_sites_delete(client):
    """Test case for vpn_sites_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/vpnSites/{vpn_site_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', vpn_site_name='vpn_site_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vpn_sites_get(client):
    """Test case for vpn_sites_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/vpnSites/{vpn_site_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', vpn_site_name='vpn_site_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vpn_sites_list(client):
    """Test case for vpn_sites_list

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/vpnSites'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_vpn_sites_list_by_resource_group(client):
    """Test case for vpn_sites_list_by_resource_group

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/vpnSites'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

