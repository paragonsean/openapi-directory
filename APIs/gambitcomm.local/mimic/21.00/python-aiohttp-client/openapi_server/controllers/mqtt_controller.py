from typing import List, Dict
from aiohttp import web

from openapi_server.models.config_mqtt import ConfigMQTT
from openapi_server import util


async def protocol_mqtt_client_get_protstate(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s MQTT TCP connection state

    0 - stopped, 2 - disconnected, 3 - connecting, 4 - connected, 5 - waiting for CONNACK, 6 - waiting for SUBACK, 7 - CONNACK received, in steady state

    :param agent_num: Agent to show MQTT state
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_mqtt_client_get_state(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s MQTT state

    0 means stopped, 1 means running

    :param agent_num: Agent to show MQTT state
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_mqtt_client_message_card(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s current messages&#39; cardinality

    0 or more

    :param agent_num: Agent to show MQTT message state
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_mqtt_client_message_get(request: web.Request, agent_num, msg_num, attr) -> web.Response:
    """Show the agent&#39;s message attributes

    Attribute can be topic, interval, count, sent , pre, post, properties(list of PUBLISH properties), properties.i (i-th PUBLISH property), properties.PROP-NAME (PUBLISH property with name PROP-NAME)

    :param agent_num: Agent to show MQTT state
    :type agent_num: int
    :param msg_num: Message Number
    :type msg_num: int
    :param attr: Attribute
    :type attr: str

    """
    return web.Response(status=200)


async def protocol_mqtt_client_message_set(request: web.Request, agent_num, msg_num, attr, value) -> web.Response:
    """Set the agent&#39;s message attributes

    Attribute can not be sent or properties . Use set/{msgNum}/count/{value} together with get/{msgNum}/count to throttle the outgoing MQTT message to the broker.

    :param agent_num: Agent to show MQTT state
    :type agent_num: int
    :param msg_num: Message Number
    :type msg_num: int
    :param attr: Attribute
    :type attr: str
    :param value: Value
    :type value: str

    """
    return web.Response(status=200)


async def protocol_mqtt_client_resubscribe(request: web.Request, agent_num, sub_num) -> web.Response:
    """Restart receiving messages from a subcription of the agent

    Restarts a subscription

    :param agent_num: Agent to change MQTT state
    :type agent_num: int
    :param sub_num: Subscription Number
    :type sub_num: int

    """
    return web.Response(status=200)


async def protocol_mqtt_client_runtime_abort(request: web.Request, agent_num) -> web.Response:
    """Abort agent&#39;s MQTT TCP session without sending DISCONNECT command

    Abort a connection

    :param agent_num: Agent to set MQTT behavior
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_mqtt_client_runtime_connect(request: web.Request, agent_num) -> web.Response:
    """Start agent&#39;s MQTT TCP session

    Start a connection

    :param agent_num: Agent to set MQTT behavior
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_mqtt_client_runtime_disconnect(request: web.Request, agent_num) -> web.Response:
    """Disconnect agent&#39;s MQTT TCP session by sending DISCONNECT command

    Graceful disconnect

    :param agent_num: Agent to set MQTT behavior
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_mqtt_client_set_broker(request: web.Request, agent_num, broker_addr) -> web.Response:
    """Set the agent&#39;s MQTT TCP connection target broker

    Broker IP address

    :param agent_num: Agent to set MQTT config
    :type agent_num: int
    :param broker_addr: Broker address
    :type broker_addr: str

    """
    return web.Response(status=200)


async def protocol_mqtt_client_set_cleansession(request: web.Request, agent_num, clean_or_not) -> web.Response:
    """Set the agent&#39;s MQTT session

    1 for clean session , 0 not

    :param agent_num: Agent to set MQTT config
    :type agent_num: int
    :param clean_or_not: Clean session
    :type clean_or_not: int

    """
    return web.Response(status=200)


async def protocol_mqtt_client_set_clientid(request: web.Request, agent_num, client_id) -> web.Response:
    """Set the agent&#39;s MQTT client ID

    MQTT client ID

    :param agent_num: Agent to set MQTT config
    :type agent_num: int
    :param client_id: Client ID
    :type client_id: str

    """
    return web.Response(status=200)


async def protocol_mqtt_client_set_keepalive(request: web.Request, agent_num, alive_time) -> web.Response:
    """Set the agent&#39;s MQTT TCP keepalive

    Keep alive the TCP connection

    :param agent_num: Agent to set MQTT config
    :type agent_num: int
    :param alive_time: period to send keepalive messages
    :type alive_time: int

    """
    return web.Response(status=200)


async def protocol_mqtt_client_set_on_disconnect(request: web.Request, agent_num, action) -> web.Response:
    """Set the agent&#39;s MQTT disconnection action

    Action to take when MQTT session is disconnected

    :param agent_num: Agent to set MQTT config
    :type agent_num: int
    :param action: Action to take
    :type action: str

    """
    return web.Response(status=200)


async def protocol_mqtt_client_set_password(request: web.Request, agent_num, password) -> web.Response:
    """Set the agent&#39;s MQTT client password

    Client password

    :param agent_num: Agent to set MQTT config
    :type agent_num: int
    :param password: Password
    :type password: str

    """
    return web.Response(status=200)


async def protocol_mqtt_client_set_port(request: web.Request, agent_num, port) -> web.Response:
    """Set the agent&#39;s MQTT TCP connection target port

    target TCP port

    :param agent_num: Agent to set MQTT config
    :type agent_num: int
    :param port: TCP port
    :type port: str

    """
    return web.Response(status=200)


async def protocol_mqtt_client_set_username(request: web.Request, agent_num, username) -> web.Response:
    """Set the agent&#39;s MQTT client username

    Client username

    :param agent_num: Agent to set MQTT config
    :type agent_num: int
    :param username: User name
    :type username: str

    """
    return web.Response(status=200)


async def protocol_mqtt_client_set_willmsg(request: web.Request, agent_num, msg) -> web.Response:
    """Set the agent&#39;s MQTT client&#39;s will

    Will message

    :param agent_num: Agent to set MQTT config
    :type agent_num: int
    :param msg: Will message
    :type msg: str

    """
    return web.Response(status=200)


async def protocol_mqtt_client_set_willqos(request: web.Request, agent_num, qos) -> web.Response:
    """Set the agent&#39;s MQTT will message&#39;s QOS field

    QOS field

    :param agent_num: Agent to set MQTT config
    :type agent_num: int
    :param qos: Quality of service field
    :type qos: str

    """
    return web.Response(status=200)


async def protocol_mqtt_client_set_willretain(request: web.Request, agent_num, retain) -> web.Response:
    """Set the agent&#39;s MQTT retained will

    Retaining will

    :param agent_num: Agent to set MQTT config
    :type agent_num: int
    :param retain: Retaining will
    :type retain: str

    """
    return web.Response(status=200)


async def protocol_mqtt_client_set_willtopic(request: web.Request, agent_num, topic) -> web.Response:
    """Set the agent&#39;s MQTT client will&#39;s topic

    Will topic for the will message

    :param agent_num: Agent to set MQTT config
    :type agent_num: int
    :param topic: topic
    :type topic: str

    """
    return web.Response(status=200)


async def protocol_mqtt_client_subscribe_card(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s current subscriptions&#39; cardinality

    0 or more

    :param agent_num: Agent to show MQTT subscription state
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_mqtt_client_subscribe_get(request: web.Request, agent_num, sub_num, attr) -> web.Response:
    """Show the agent&#39;s subscription attributes

    Attribute can be topic, properties(list of SUBSCRIBE properties), properties.i (i-th SUBSCRIBE property), properties.PROP-NAME (SUBSCRIBE property with name PROP-NAME)

    :param agent_num: Agent to show MQTT state
    :type agent_num: int
    :param sub_num: Subscribe Number
    :type sub_num: int
    :param attr: Attribute
    :type attr: str

    """
    return web.Response(status=200)


async def protocol_mqtt_client_subscribe_set(request: web.Request, agent_num, sub_num, attr, value) -> web.Response:
    """Set the agent&#39;s subscribe attributes

    Attribute can not be properties .

    :param agent_num: Agent to show MQTT state
    :type agent_num: int
    :param sub_num: Subscribe Number
    :type sub_num: int
    :param attr: Attribute
    :type attr: str
    :param value: Value
    :type value: str

    """
    return web.Response(status=200)


async def protocol_mqtt_client_unsubscribe(request: web.Request, agent_num, sub_num) -> web.Response:
    """Stops receiving messages from a subcription of the agent

    Stops a subscription

    :param agent_num: Agent to change MQTT state
    :type agent_num: int
    :param sub_num: Subscription Number
    :type sub_num: int

    """
    return web.Response(status=200)


async def protocol_mqtt_get_args(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s MQTT argument structure

    Agent&#39;s MQTT configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to show the MQTT argument structure
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_mqtt_get_config(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s MQTT configuration

    Agent&#39;s MQTT configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to show the MQTT configuration
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_mqtt_get_statistics(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s MQTT statistics

    Statistics of fields indicated in the headers

    :param agent_num: Agent to show MQTT statistics
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_mqtt_get_stats_hdr(request: web.Request, ) -> web.Response:
    """Show the MQTT statistics headers

    The headers of statistics fields


    """
    return web.Response(status=200)


async def protocol_mqtt_get_trace(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s MQTT traffic tracing

    Trace 1 means enabled, 0 means not

    :param agent_num: Agent to show whether MQTT tracing is enabled
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_mqtt_set_config(request: web.Request, agent_num, argument, value) -> web.Response:
    """Set the agent&#39;s MQTT configuration

    Agent&#39;s MQTT configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to set the MQTT configuration
    :type agent_num: int
    :param argument: Parameter to set the MQTT configuration
    :type argument: str
    :param value: Value to set the MQTT configuration
    :type value: str

    """
    return web.Response(status=200)


async def protocol_mqtt_set_trace(request: web.Request, agent_num, enable_or_not) -> web.Response:
    """Set the agent&#39;s MQTT traffic tracing

    1 to enable, 0 to disable

    :param agent_num: Agent to set the MQTT tracing
    :type agent_num: int
    :param enable_or_not: Value to set the MQTT tracing
    :type enable_or_not: str

    """
    return web.Response(status=200)
