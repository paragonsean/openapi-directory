from typing import List, Dict
from aiohttp import web

from openapi_server.models.config_dhcp import ConfigDHCP
from openapi_server import util


async def protocol_dhcp_get_args(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s DHCP argument structure

    Agent&#39;s DHCP configuration particulars

    :param agent_num: Agent to show the DHCP argument structure
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_dhcp_get_config(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s DHCP configuration

    Agent&#39;s DHCP configuration hwaddr,classid,add_options,script

    :param agent_num: Agent to show the DHCP configuration
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_dhcp_get_statistics(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s DHCP statistics

    Statistics of fields indicated in the headers

    :param agent_num: Agent to show DHCP statistics
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_dhcp_get_stats_hdr(request: web.Request, ) -> web.Response:
    """Show the DHCP statistics headers

    The headers of statistics fields


    """
    return web.Response(status=200)


async def protocol_dhcp_get_trace(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s DHCP traffic tracing

    Trace 1 means enabled, 0 means not

    :param agent_num: Agent to show whether DHCP tracing is enabled
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_dhcp_params(request: web.Request, agent_num) -> web.Response:
    """Show the parameters configured by the server in its DHCP-OFFER message

    DHCP-OFFER message parameters

    :param agent_num: Agent to show DHCP DHCP-OFFER message
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_dhcp_set_config(request: web.Request, agent_num, argument, value) -> web.Response:
    """Set the agent&#39;s DHCP configuration

    Agent&#39;s DHCP configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to set the DHCP configuration
    :type agent_num: int
    :param argument: Parameter to set the DHCP configuration
    :type argument: str
    :param value: Value to set the DHCP configuration
    :type value: str

    """
    return web.Response(status=200)


async def protocol_dhcp_set_trace(request: web.Request, agent_num, enable_or_not) -> web.Response:
    """Set the agent&#39;s DHCP traffic tracing

    1 to enable, 0 to disable

    :param agent_num: Agent to set the DHCP tracing
    :type agent_num: int
    :param enable_or_not: Value to set the DHCP tracing
    :type enable_or_not: str

    """
    return web.Response(status=200)
