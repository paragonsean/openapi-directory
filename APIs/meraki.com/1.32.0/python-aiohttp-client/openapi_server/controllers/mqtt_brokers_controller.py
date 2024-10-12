from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_network_mqtt_broker_request import CreateNetworkMqttBrokerRequest
from openapi_server.models.update_network_mqtt_broker_request import UpdateNetworkMqttBrokerRequest
from openapi_server import util


async def create_network_mqtt_broker_1(request: web.Request, network_id, body) -> web.Response:
    """Add an MQTT broker

    Add an MQTT broker

    :param network_id: 
    :type network_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = CreateNetworkMqttBrokerRequest.from_dict(body)
    return web.Response(status=200)


async def delete_network_mqtt_broker_1(request: web.Request, network_id, mqtt_broker_id) -> web.Response:
    """Delete an MQTT broker

    Delete an MQTT broker

    :param network_id: 
    :type network_id: str
    :param mqtt_broker_id: 
    :type mqtt_broker_id: str

    """
    return web.Response(status=200)


async def get_network_mqtt_broker_1(request: web.Request, network_id, mqtt_broker_id) -> web.Response:
    """Return an MQTT broker

    Return an MQTT broker

    :param network_id: 
    :type network_id: str
    :param mqtt_broker_id: 
    :type mqtt_broker_id: str

    """
    return web.Response(status=200)


async def get_network_mqtt_brokers_1(request: web.Request, network_id) -> web.Response:
    """List the MQTT brokers for this network

    List the MQTT brokers for this network

    :param network_id: 
    :type network_id: str

    """
    return web.Response(status=200)


async def update_network_mqtt_broker_1(request: web.Request, network_id, mqtt_broker_id, body=None) -> web.Response:
    """Update an MQTT broker

    Update an MQTT broker

    :param network_id: 
    :type network_id: str
    :param mqtt_broker_id: 
    :type mqtt_broker_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateNetworkMqttBrokerRequest.from_dict(body)
    return web.Response(status=200)
