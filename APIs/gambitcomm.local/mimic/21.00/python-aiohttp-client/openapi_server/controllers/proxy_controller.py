from typing import List, Dict
from aiohttp import web

from openapi_server.models.config_proxy import ConfigPROXY
from openapi_server import util


async def protocol_proxy_get_args(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s PROXY argument structure

    Agent&#39;s PROXY configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to show the PROXY argument structure
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_proxy_get_config(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s PROXY configuration

    Agent&#39;s PROXY configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to show the PROXY configuration
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_proxy_get_statistics(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s PROXY statistics

    Statistics of fields indicated in the headers

    :param agent_num: Agent to show PROXY statistics
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_proxy_get_stats_hdr(request: web.Request, ) -> web.Response:
    """Show the PROXY statistics headers

    The headers of statistics fields


    """
    return web.Response(status=200)


async def protocol_proxy_get_trace(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s PROXY traffic tracing

    Trace 1 means enabled, 0 means not

    :param agent_num: Agent to show whether PROXY tracing is enabled
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_proxy_port_add(request: web.Request, agent_num, port, target, target_port) -> web.Response:
    """Add individual proxy target on the agent and the simulator host

    Additional proxy target

    :param agent_num: Agent to manipulate PROXY target
    :type agent_num: int
    :param port: 
    :type port: int
    :param target: 
    :type target: str
    :param target_port: 
    :type target_port: int

    """
    return web.Response(status=200)


async def protocol_proxy_port_isstarted(request: web.Request, agent_num, port) -> web.Response:
    """Check individual target

    Check individual target

    :param agent_num: Agent to manipulate PROXY target
    :type agent_num: int
    :param port: 
    :type port: int

    """
    return web.Response(status=200)


async def protocol_proxy_port_list(request: web.Request, agent_num) -> web.Response:
    """List all proxy targets

    

    :param agent_num: Agent to manipulate PROXY target
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_proxy_port_remove(request: web.Request, agent_num, port) -> web.Response:
    """Remove individual proxy target on the agent and the simulator host

    Remove proxy target

    :param agent_num: Agent to manipulate PROXY target
    :type agent_num: int
    :param port: 
    :type port: int

    """
    return web.Response(status=200)


async def protocol_proxy_port_start(request: web.Request, agent_num, port) -> web.Response:
    """Start additional target

    Start additional target

    :param agent_num: Agent to manipulate PROXY target
    :type agent_num: int
    :param port: 
    :type port: int

    """
    return web.Response(status=200)


async def protocol_proxy_port_stop(request: web.Request, agent_num, port) -> web.Response:
    """Stop additional target

    Stop additional target

    :param agent_num: Agent to manipulate PROXY target
    :type agent_num: int
    :param port: 
    :type port: int

    """
    return web.Response(status=200)


async def protocol_proxy_set_config(request: web.Request, agent_num, argument, value) -> web.Response:
    """Set the agent&#39;s PROXY configuration

    Agent&#39;s PROXY configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to set the PROXY configuration
    :type agent_num: int
    :param argument: Parameter to set the PROXY configuration
    :type argument: str
    :param value: Value to set the PROXY configuration
    :type value: str

    """
    return web.Response(status=200)


async def protocol_proxy_set_trace(request: web.Request, agent_num, enable_or_not) -> web.Response:
    """Set the agent&#39;s PROXY traffic tracing

    1 to enable, 0 to disable

    :param agent_num: Agent to set the PROXY tracing
    :type agent_num: int
    :param enable_or_not: Value to set the PROXY tracing
    :type enable_or_not: str

    """
    return web.Response(status=200)
