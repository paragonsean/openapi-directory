# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_network_mqtt_broker_request import CreateNetworkMqttBrokerRequest
from openapi_server.models.update_network_mqtt_broker_request import UpdateNetworkMqttBrokerRequest


pytestmark = pytest.mark.asyncio

async def test_create_network_mqtt_broker_1(client):
    """Test case for create_network_mqtt_broker_1

    Add an MQTT broker
    """
    body = openapi_server.CreateNetworkMqttBrokerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/networks/{network_id}/mqttBrokers'.format(network_id='network_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_network_mqtt_broker_1(client):
    """Test case for delete_network_mqtt_broker_1

    Delete an MQTT broker
    """
    headers = { 
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/networks/{network_id}/mqttBrokers/{mqtt_broker_id}'.format(network_id='network_id_example', mqtt_broker_id='mqtt_broker_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_mqtt_broker_1(client):
    """Test case for get_network_mqtt_broker_1

    Return an MQTT broker
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/mqttBrokers/{mqtt_broker_id}'.format(network_id='network_id_example', mqtt_broker_id='mqtt_broker_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_network_mqtt_brokers_1(client):
    """Test case for get_network_mqtt_brokers_1

    List the MQTT brokers for this network
    """
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/networks/{network_id}/mqttBrokers'.format(network_id='network_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_network_mqtt_broker_1(client):
    """Test case for update_network_mqtt_broker_1

    Update an MQTT broker
    """
    body = openapi_server.UpdateNetworkMqttBrokerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/networks/{network_id}/mqttBrokers/{mqtt_broker_id}'.format(network_id='network_id_example', mqtt_broker_id='mqtt_broker_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

