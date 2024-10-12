# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_network_appliance_vpn_site_to_site_vpn200_response import GetNetworkApplianceVpnSiteToSiteVpn200Response
from openapi_server.models.get_organization_appliance_vpn_third_party_vpn_peers200_response import GetOrganizationApplianceVpnThirdPartyVPNPeers200Response
from openapi_server.models.update_network_appliance_vpn_bgp_request import UpdateNetworkApplianceVpnBgpRequest
from openapi_server.models.update_network_appliance_vpn_site_to_site_vpn_request import UpdateNetworkApplianceVpnSiteToSiteVpnRequest
from openapi_server.models.update_network_wireless_ssid_vpn_request import UpdateNetworkWirelessSsidVpnRequest
from openapi_server.models.update_organization_appliance_vpn_third_party_vpn_peers_request import UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest
from openapi_server.models.update_organization_appliance_vpn_vpn_firewall_rules_request import UpdateOrganizationApplianceVpnVpnFirewallRulesRequest


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_vpn_bgp_1(client):
    """Test case for get_network_appliance_vpn_bgp_1

    Return a Hub BGP Configuration
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/vpn/bgp'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_vpn_site_to_site_vpn_1(client):
    """Test case for get_network_appliance_vpn_site_to_site_vpn_1

    Return the site-to-site VPN settings of a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/vpn/siteToSiteVpn'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_ssid_vpn_2(client):
    """Test case for get_network_wireless_ssid_vpn_2

    List the VPN settings for the SSID.
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/vpn'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_appliance_vpn_stats_1(client):
    """Test case for get_organization_appliance_vpn_stats_1

    Show VPN history stat for networks in an organization
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkIds', ['network_ids_example']),
                    ('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/appliance/vpn/stats'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_appliance_vpn_statuses_1(client):
    """Test case for get_organization_appliance_vpn_statuses_1

    Show VPN status for networks in an organization
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkIds', ['network_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/appliance/vpn/statuses'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_appliance_vpn_third_party_vpn_peers_1(client):
    """Test case for get_organization_appliance_vpn_third_party_vpn_peers_1

    Return the third party VPN peers for an organization
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/appliance/vpn/thirdPartyVPNPeers'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_appliance_vpn_vpn_firewall_rules_1(client):
    """Test case for get_organization_appliance_vpn_vpn_firewall_rules_1

    Return the firewall rules for an organization's site-to-site VPN
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/appliance/vpn/vpnFirewallRules'.format(organization_id='organization_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_vpn_bgp_1(client):
    """Test case for update_network_appliance_vpn_bgp_1

    Update a Hub BGP Configuration
    """
    body = openapi_server.UpdateNetworkApplianceVpnBgpRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/vpn/bgp'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_vpn_site_to_site_vpn_1(client):
    """Test case for update_network_appliance_vpn_site_to_site_vpn_1

    Update the site-to-site VPN settings of a network
    """
    body = openapi_server.UpdateNetworkApplianceVpnSiteToSiteVpnRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/vpn/siteToSiteVpn'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_wireless_ssid_vpn_2(client):
    """Test case for update_network_wireless_ssid_vpn_2

    Update the VPN settings for the SSID
    """
    body = openapi_server.UpdateNetworkWirelessSsidVpnRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/vpn'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_appliance_vpn_third_party_vpn_peers_1(client):
    """Test case for update_organization_appliance_vpn_third_party_vpn_peers_1

    Update the third party VPN peers for an organization
    """
    body = openapi_server.UpdateOrganizationApplianceVpnThirdPartyVPNPeersRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/appliance/vpn/thirdPartyVPNPeers'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_organization_appliance_vpn_vpn_firewall_rules_1(client):
    """Test case for update_organization_appliance_vpn_vpn_firewall_rules_1

    Update the firewall rules of an organization's site-to-site VPN
    """
    body = openapi_server.UpdateOrganizationApplianceVpnVpnFirewallRulesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/organizations/{organization_id}/appliance/vpn/vpnFirewallRules'.format(organization_id='organization_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

