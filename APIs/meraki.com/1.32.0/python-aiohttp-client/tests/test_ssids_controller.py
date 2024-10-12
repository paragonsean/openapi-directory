# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_wireless_ssid_identity_psk_request import CreateNetworkWirelessSsidIdentityPskRequest
from openapi_server.models.get_network_appliance_ssids200_response_inner import GetNetworkApplianceSsids200ResponseInner
from openapi_server.models.get_network_wireless_ssid_eap_override200_response import GetNetworkWirelessSsidEapOverride200Response
from openapi_server.models.get_network_wireless_ssid_identity_psks200_response_inner import GetNetworkWirelessSsidIdentityPsks200ResponseInner
from openapi_server.models.get_network_wireless_ssid_splash_settings200_response import GetNetworkWirelessSsidSplashSettings200Response
from openapi_server.models.get_organization_summary_top_ssids_by_usage200_response_inner import GetOrganizationSummaryTopSsidsByUsage200ResponseInner
from openapi_server.models.update_network_appliance_ssid_request import UpdateNetworkApplianceSsidRequest
from openapi_server.models.update_network_wireless_ssid_bonjour_forwarding_request import UpdateNetworkWirelessSsidBonjourForwardingRequest
from openapi_server.models.update_network_wireless_ssid_device_type_group_policies_request import UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest
from openapi_server.models.update_network_wireless_ssid_eap_override_request import UpdateNetworkWirelessSsidEapOverrideRequest
from openapi_server.models.update_network_wireless_ssid_firewall_l3_firewall_rules_request import UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest
from openapi_server.models.update_network_wireless_ssid_firewall_l7_firewall_rules_request import UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest
from openapi_server.models.update_network_wireless_ssid_hotspot20_request import UpdateNetworkWirelessSsidHotspot20Request
from openapi_server.models.update_network_wireless_ssid_identity_psk_request import UpdateNetworkWirelessSsidIdentityPskRequest
from openapi_server.models.update_network_wireless_ssid_request import UpdateNetworkWirelessSsidRequest
from openapi_server.models.update_network_wireless_ssid_schedules_request import UpdateNetworkWirelessSsidSchedulesRequest
from openapi_server.models.update_network_wireless_ssid_splash_settings_request import UpdateNetworkWirelessSsidSplashSettingsRequest
from openapi_server.models.update_network_wireless_ssid_traffic_shaping_rules_request import UpdateNetworkWirelessSsidTrafficShapingRulesRequest
from openapi_server.models.update_network_wireless_ssid_vpn_request import UpdateNetworkWirelessSsidVpnRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_wireless_ssid_identity_psk_1(client):
    """Test case for create_network_wireless_ssid_identity_psk_1

    Create an Identity PSK
    """
    body = openapi_server.CreateNetworkWirelessSsidIdentityPskRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/identityPsks'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_wireless_ssid_identity_psk_1(client):
    """Test case for delete_network_wireless_ssid_identity_psk_1

    Delete an Identity PSK
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/identityPsks/{identity_psk_id}'.format(network_id='network_id_example', number='number_example', identity_psk_id='identity_psk_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_ssid_1(client):
    """Test case for get_network_appliance_ssid_1

    Return a single MX SSID
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/ssids/{number}'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_appliance_ssids_1(client):
    """Test case for get_network_appliance_ssids_1

    List the MX SSIDs in a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/appliance/ssids'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_ssid_1(client):
    """Test case for get_network_wireless_ssid_1

    Return a single MR SSID
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_ssid_bonjour_forwarding_1(client):
    """Test case for get_network_wireless_ssid_bonjour_forwarding_1

    List the Bonjour forwarding setting and rules for the SSID
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/bonjourForwarding'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_ssid_device_type_group_policies_1(client):
    """Test case for get_network_wireless_ssid_device_type_group_policies_1

    List the device type group policies for the SSID
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/deviceTypeGroupPolicies'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_ssid_eap_override_1(client):
    """Test case for get_network_wireless_ssid_eap_override_1

    Return the EAP overridden parameters for an SSID
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/eapOverride'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_ssid_firewall_l3_firewall_rules_1(client):
    """Test case for get_network_wireless_ssid_firewall_l3_firewall_rules_1

    Return the L3 firewall rules for an SSID on an MR network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/firewall/l3FirewallRules'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_ssid_firewall_l7_firewall_rules_1(client):
    """Test case for get_network_wireless_ssid_firewall_l7_firewall_rules_1

    Return the L7 firewall rules for an SSID on an MR network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/firewall/l7FirewallRules'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_ssid_hotspot20_1(client):
    """Test case for get_network_wireless_ssid_hotspot20_1

    Return the Hotspot 2.0 settings for an SSID
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/hotspot20'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_ssid_identity_psk_1(client):
    """Test case for get_network_wireless_ssid_identity_psk_1

    Return an Identity PSK
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/identityPsks/{identity_psk_id}'.format(network_id='network_id_example', number='number_example', identity_psk_id='identity_psk_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_ssid_identity_psks_1(client):
    """Test case for get_network_wireless_ssid_identity_psks_1

    List all Identity PSKs in a wireless network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/identityPsks'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_ssid_schedules_1(client):
    """Test case for get_network_wireless_ssid_schedules_1

    List the outage schedule for the SSID
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/schedules'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_ssid_splash_settings_1(client):
    """Test case for get_network_wireless_ssid_splash_settings_1

    Display the splash page settings for the given SSID
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/splash/settings'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_ssid_traffic_shaping_rules_1(client):
    """Test case for get_network_wireless_ssid_traffic_shaping_rules_1

    Display the traffic shaping settings for a SSID on an MR network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/trafficShaping/rules'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_wireless_ssid_vpn_1(client):
    """Test case for get_network_wireless_ssid_vpn_1

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

async def test_get_network_wireless_ssids_1(client):
    """Test case for get_network_wireless_ssids_1

    List the MR SSIDs in a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/wireless/ssids'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization_summary_top_ssids_by_usage_3(client):
    """Test case for get_organization_summary_top_ssids_by_usage_3

    Return metrics for organization's top 10 ssids by data usage over given time range
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/summary/top/ssids/byUsage'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_appliance_ssid_1(client):
    """Test case for update_network_appliance_ssid_1

    Update the attributes of an MX SSID
    """
    body = openapi_server.UpdateNetworkApplianceSsidRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/appliance/ssids/{number}'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_wireless_ssid_1(client):
    """Test case for update_network_wireless_ssid_1

    Update the attributes of an MR SSID
    """
    body = openapi_server.UpdateNetworkWirelessSsidRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_wireless_ssid_bonjour_forwarding_1(client):
    """Test case for update_network_wireless_ssid_bonjour_forwarding_1

    Update the bonjour forwarding setting and rules for the SSID
    """
    body = openapi_server.UpdateNetworkWirelessSsidBonjourForwardingRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/bonjourForwarding'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_wireless_ssid_device_type_group_policies_1(client):
    """Test case for update_network_wireless_ssid_device_type_group_policies_1

    Update the device type group policies for the SSID
    """
    body = openapi_server.UpdateNetworkWirelessSsidDeviceTypeGroupPoliciesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/deviceTypeGroupPolicies'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_wireless_ssid_eap_override_1(client):
    """Test case for update_network_wireless_ssid_eap_override_1

    Update the EAP overridden parameters for an SSID.
    """
    body = openapi_server.UpdateNetworkWirelessSsidEapOverrideRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/eapOverride'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_wireless_ssid_firewall_l3_firewall_rules_1(client):
    """Test case for update_network_wireless_ssid_firewall_l3_firewall_rules_1

    Update the L3 firewall rules of an SSID on an MR network
    """
    body = openapi_server.UpdateNetworkWirelessSsidFirewallL3FirewallRulesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/firewall/l3FirewallRules'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_wireless_ssid_firewall_l7_firewall_rules_1(client):
    """Test case for update_network_wireless_ssid_firewall_l7_firewall_rules_1

    Update the L7 firewall rules of an SSID on an MR network
    """
    body = openapi_server.UpdateNetworkWirelessSsidFirewallL7FirewallRulesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/firewall/l7FirewallRules'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_wireless_ssid_hotspot20_1(client):
    """Test case for update_network_wireless_ssid_hotspot20_1

    Update the Hotspot 2.0 settings of an SSID
    """
    body = openapi_server.UpdateNetworkWirelessSsidHotspot20Request()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/hotspot20'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_wireless_ssid_identity_psk_1(client):
    """Test case for update_network_wireless_ssid_identity_psk_1

    Update an Identity PSK
    """
    body = openapi_server.UpdateNetworkWirelessSsidIdentityPskRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/identityPsks/{identity_psk_id}'.format(network_id='network_id_example', number='number_example', identity_psk_id='identity_psk_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_wireless_ssid_schedules_1(client):
    """Test case for update_network_wireless_ssid_schedules_1

    Update the outage schedule for the SSID
    """
    body = openapi_server.UpdateNetworkWirelessSsidSchedulesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/schedules'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_wireless_ssid_splash_settings_1(client):
    """Test case for update_network_wireless_ssid_splash_settings_1

    Modify the splash page settings for the given SSID
    """
    body = openapi_server.UpdateNetworkWirelessSsidSplashSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/splash/settings'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_wireless_ssid_traffic_shaping_rules_1(client):
    """Test case for update_network_wireless_ssid_traffic_shaping_rules_1

    Update the traffic shaping settings for an SSID on an MR network
    """
    body = openapi_server.UpdateNetworkWirelessSsidTrafficShapingRulesRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/wireless/ssids/{number}/trafficShaping/rules'.format(network_id='network_id_example', number='number_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_wireless_ssid_vpn_1(client):
    """Test case for update_network_wireless_ssid_vpn_1

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

