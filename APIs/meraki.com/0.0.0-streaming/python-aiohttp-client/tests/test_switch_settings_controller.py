# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_switch_settings_qos_rule_request import CreateNetworkSwitchSettingsQosRuleRequest
from openapi_server.models.update_network_switch_settings_multicast_request import UpdateNetworkSwitchSettingsMulticastRequest
from openapi_server.models.update_network_switch_settings_qos_rule_request import UpdateNetworkSwitchSettingsQosRuleRequest
from openapi_server.models.update_network_switch_settings_qos_rules_order_request import UpdateNetworkSwitchSettingsQosRulesOrderRequest
from openapi_server.models.update_network_switch_settings_request import UpdateNetworkSwitchSettingsRequest
from openapi_server.models.update_network_switch_settings_storm_control_request import UpdateNetworkSwitchSettingsStormControlRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_switch_settings_qos_rule(client):
    """Test case for create_network_switch_settings_qos_rule

    Add a quality of service rule
    """
    body = openapi_server.CreateNetworkSwitchSettingsQosRuleRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v0/networks/{network_id}/switch/settings/qosRules'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_switch_settings_qos_rule(client):
    """Test case for delete_network_switch_settings_qos_rule

    Delete a quality of service rule
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v0/networks/{network_id}/switch/settings/qosRules/{qos_rule_id}'.format(network_id='network_id_example', qos_rule_id='qos_rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_settings(client):
    """Test case for get_network_switch_settings

    Returns the switch network settings
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/switch/settings'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_settings_mtu(client):
    """Test case for get_network_switch_settings_mtu

    Return the MTU configuration
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/switch/settings/mtu'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_settings_multicast(client):
    """Test case for get_network_switch_settings_multicast

    Return multicast settings for a network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/switch/settings/multicast'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_settings_qos_rule(client):
    """Test case for get_network_switch_settings_qos_rule

    Return a quality of service rule
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/switch/settings/qosRules/{qos_rule_id}'.format(network_id='network_id_example', qos_rule_id='qos_rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_settings_qos_rules(client):
    """Test case for get_network_switch_settings_qos_rules

    List quality of service rules
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/switch/settings/qosRules'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_settings_qos_rules_order(client):
    """Test case for get_network_switch_settings_qos_rules_order

    Return the quality of service rule IDs by order in which they will be processed by the switch
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/switch/settings/qosRules/order'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_settings_storm_control(client):
    """Test case for get_network_switch_settings_storm_control

    Return the storm control configuration for a switch network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v0/networks/{network_id}/switch/settings/stormControl'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_settings(client):
    """Test case for update_network_switch_settings

    Update switch network settings
    """
    body = openapi_server.UpdateNetworkSwitchSettingsRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/switch/settings'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_settings_multicast(client):
    """Test case for update_network_switch_settings_multicast

    Update multicast settings for a network
    """
    body = openapi_server.UpdateNetworkSwitchSettingsMulticastRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/switch/settings/multicast'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_settings_qos_rule(client):
    """Test case for update_network_switch_settings_qos_rule

    Update a quality of service rule
    """
    body = openapi_server.UpdateNetworkSwitchSettingsQosRuleRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/switch/settings/qosRules/{qos_rule_id}'.format(network_id='network_id_example', qos_rule_id='qos_rule_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_settings_qos_rules_order(client):
    """Test case for update_network_switch_settings_qos_rules_order

    Update the order in which the rules should be processed by the switch
    """
    body = openapi_server.UpdateNetworkSwitchSettingsQosRulesOrderRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/switch/settings/qosRules/order'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_settings_storm_control(client):
    """Test case for update_network_switch_settings_storm_control

    Update the storm control configuration for a switch network
    """
    body = openapi_server.UpdateNetworkSwitchSettingsStormControlRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v0/networks/{network_id}/switch/settings/stormControl'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

