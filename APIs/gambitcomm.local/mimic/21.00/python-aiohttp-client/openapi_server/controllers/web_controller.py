from typing import List, Dict
from aiohttp import web

from openapi_server.models.config_web import ConfigWEB
from openapi_server import util


async def protocol_web_get_args(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s WEB argument structure

    Agent&#39;s WEB configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to show the WEB argument structure
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_web_get_config(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s WEB configuration

    Agent&#39;s WEB configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to show the WEB configuration
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_web_get_statistics(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s WEB statistics

    Statistics of fields indicated in the headers

    :param agent_num: Agent to show WEB statistics
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_web_get_stats_hdr(request: web.Request, ) -> web.Response:
    """Show the WEB statistics headers

    The headers of statistics fields


    """
    return web.Response(status=200)


async def protocol_web_get_trace(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s WEB traffic tracing

    Trace 1 means enabled, 0 means not

    :param agent_num: Agent to show whether WEB tracing is enabled
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_web_port_add(request: web.Request, agent_num, port) -> web.Response:
    """Add the agent&#39;s WEB port

    Add port

    :param agent_num: Agent to add WEB port
    :type agent_num: int
    :param port: TCP port
    :type port: int

    """
    return web.Response(status=200)


async def protocol_web_port_exists(request: web.Request, agent_num, port) -> web.Response:
    """Show the agent&#39;s WEB port

    Check the port. 1 means existing, 0 means not

    :param agent_num: Agent to show WEB configuration
    :type agent_num: int
    :param port: TCP port
    :type port: int

    """
    return web.Response(status=200)


async def protocol_web_port_remove(request: web.Request, agent_num, port) -> web.Response:
    """Remove the agent&#39;s WEB port

    Remove port

    :param agent_num: Agent to remove WEB port
    :type agent_num: int
    :param port: TCP port
    :type port: int

    """
    return web.Response(status=200)


async def protocol_web_port_set(request: web.Request, agent_num, port, protocol, version) -> web.Response:
    """Set the agent&#39;s WEB port attribute

    Set port

    :param agent_num: Agent to set WEB port
    :type agent_num: int
    :param port: TCP port
    :type port: int
    :param protocol: Encryption or related protocol
    :type protocol: str
    :param version: Encryption or related protocol version
    :type version: str

    """
    return web.Response(status=200)


async def protocol_web_port_start(request: web.Request, agent_num, port) -> web.Response:
    """Start the agent&#39;s WEB port

    Start port

    :param agent_num: Agent to start WEB port
    :type agent_num: int
    :param port: TCP port
    :type port: int

    """
    return web.Response(status=200)


async def protocol_web_port_stop(request: web.Request, agent_num, port) -> web.Response:
    """Stop the agent&#39;s WEB port

    Stop port

    :param agent_num: Agent to stop WEB port
    :type agent_num: int
    :param port: TCP port
    :type port: int

    """
    return web.Response(status=200)


async def protocol_web_set_config(request: web.Request, agent_num, argument, value) -> web.Response:
    """Set the agent&#39;s WEB configuration

    Agent&#39;s WEB configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to set the WEB configuration
    :type agent_num: int
    :param argument: Parameter to set the WEB configuration
    :type argument: str
    :param value: Value to set the WEB configuration
    :type value: str

    """
    return web.Response(status=200)


async def protocol_web_set_trace(request: web.Request, agent_num, enable_or_not) -> web.Response:
    """Set the agent&#39;s WEB traffic tracing

    1 to enable, 0 to disable

    :param agent_num: Agent to set the WEB tracing
    :type agent_num: int
    :param enable_or_not: Value to set the WEB tracing
    :type enable_or_not: str

    """
    return web.Response(status=200)
