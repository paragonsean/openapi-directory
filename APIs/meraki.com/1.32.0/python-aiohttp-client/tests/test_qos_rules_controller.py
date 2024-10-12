# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_switch_qos_rule_request import CreateNetworkSwitchQosRuleRequest
from openapi_server.models.update_network_switch_qos_rule_request import UpdateNetworkSwitchQosRuleRequest
from openapi_server.models.update_network_switch_qos_rules_order_request import UpdateNetworkSwitchQosRulesOrderRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_switch_qos_rule_1(client):
    """Test case for create_network_switch_qos_rule_1

    Add a quality of service rule
    """
    body = openapi_server.CreateNetworkSwitchQosRuleRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/switch/qosRules'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_switch_qos_rule_1(client):
    """Test case for delete_network_switch_qos_rule_1

    Delete a quality of service rule
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/switch/qosRules/{qos_rule_id}'.format(network_id='network_id_example', qos_rule_id='qos_rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_qos_rule_1(client):
    """Test case for get_network_switch_qos_rule_1

    Return a quality of service rule
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/qosRules/{qos_rule_id}'.format(network_id='network_id_example', qos_rule_id='qos_rule_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_qos_rules_1(client):
    """Test case for get_network_switch_qos_rules_1

    List quality of service rules
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/qosRules'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_switch_qos_rules_order_1(client):
    """Test case for get_network_switch_qos_rules_order_1

    Return the quality of service rule IDs by order in which they will be processed by the switch
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/switch/qosRules/order'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_qos_rule_1(client):
    """Test case for update_network_switch_qos_rule_1

    Update a quality of service rule
    """
    body = openapi_server.UpdateNetworkSwitchQosRuleRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/qosRules/{qos_rule_id}'.format(network_id='network_id_example', qos_rule_id='qos_rule_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_switch_qos_rules_order_1(client):
    """Test case for update_network_switch_qos_rules_order_1

    Update the order in which the rules should be processed by the switch
    """
    body = openapi_server.UpdateNetworkSwitchQosRulesOrderRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/switch/qosRules/order'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

