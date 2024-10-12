from typing import List, Dict
from aiohttp import web

from openapi_server.models.config_coap import ConfigCOAP
from openapi_server import util


async def protocol_coap_get_args(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s COAP argument structure

    Agent&#39;s COAP configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to show the COAP argument structure
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_coap_get_config(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s COAP configuration

    Agent&#39;s COAP configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to show the COAP configuration
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_coap_get_statistics(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s COAP statistics

    Statistics of fields indicated in the headers

    :param agent_num: Agent to show COAP statistics
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_coap_get_stats_hdr(request: web.Request, ) -> web.Response:
    """Show the COAP statistics headers

    The headers of statistics fields


    """
    return web.Response(status=200)


async def protocol_coap_get_trace(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s COAP traffic tracing

    Trace 1 means enabled, 0 means not

    :param agent_num: Agent to show whether COAP tracing is enabled
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_coap_set_config(request: web.Request, agent_num, argument, value) -> web.Response:
    """Set the agent&#39;s COAP configuration

    Agent&#39;s COAP configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to set the COAP configuration
    :type agent_num: int
    :param argument: Parameter to set the COAP configuration
    :type argument: str
    :param value: Value to set the COAP configuration
    :type value: str

    """
    return web.Response(status=200)


async def protocol_coap_set_trace(request: web.Request, agent_num, enable_or_not) -> web.Response:
    """Set the agent&#39;s COAP traffic tracing

    1 to enable, 0 to disable

    :param agent_num: Agent to set the COAP tracing
    :type agent_num: int
    :param enable_or_not: Value to set the COAP tracing
    :type enable_or_not: str

    """
    return web.Response(status=200)
