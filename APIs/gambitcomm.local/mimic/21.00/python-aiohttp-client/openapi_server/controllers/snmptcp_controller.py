from typing import List, Dict
from aiohttp import web

from openapi_server.models.config_snmptcp import ConfigSNMPTCP
from openapi_server.models.ip_alias import IPAlias
from openapi_server import util


async def protocol_snmptcp_get_args(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s SNMPTCP argument structure

    Agent&#39;s SNMPTCP configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to show the SNMPTCP argument structure
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_snmptcp_get_config(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s SNMPTCP configuration

    Agent&#39;s SNMPTCP configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to show the SNMPTCP configuration
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_snmptcp_get_statistics(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s SNMPTCP statistics

    Statistics of fields indicated in the headers

    :param agent_num: Agent to show SNMPTCP statistics
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_snmptcp_get_stats_hdr(request: web.Request, ) -> web.Response:
    """Show the SNMPTCP statistics headers

    The headers of statistics fields


    """
    return web.Response(status=200)


async def protocol_snmptcp_get_trace(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s SNMPTCP traffic tracing

    Trace 1 means enabled, 0 means not

    :param agent_num: Agent to show whether SNMPTCP tracing is enabled
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_snmptcp_ipalias_disable(request: web.Request, agent_num, ipaddress, port) -> web.Response:
    """Disable individual IP aliases on the agent and the simulator host

    By default, the MIMIC SNMPTCP server listens on all the IP addresses (aliases) that are configured for an agent

    :param agent_num: Agent to manipulate SNMPTCP IP alias
    :type agent_num: int
    :param ipaddress: 
    :type ipaddress: str
    :param port: 
    :type port: int

    """
    return web.Response(status=200)


async def protocol_snmptcp_ipalias_enable(request: web.Request, agent_num, ipaddress, port) -> web.Response:
    """Enable individual IP aliases on the agent and the simulator host

    By default, the MIMIC SNMPTCP server listens on all the IP addresses (aliases) that are configured for an agent

    :param agent_num: Agent to manipulate SNMPTCP IP alias
    :type agent_num: int
    :param ipaddress: 
    :type ipaddress: str
    :param port: 
    :type port: int

    """
    return web.Response(status=200)


async def protocol_snmptcp_ipalias_isenabled(request: web.Request, agent_num, ipaddress, port) -> web.Response:
    """Check individual IP aliases on the agent and the simulator host

    By default, the MIMIC SNMPTCP server listens on all the IP addresses (aliases) that are configured for an agent

    :param agent_num: Agent to manipulate SNMPTCP IP alias
    :type agent_num: int
    :param ipaddress: 
    :type ipaddress: str
    :param port: 
    :type port: int

    """
    return web.Response(status=200)


async def protocol_snmptcp_ipalias_list(request: web.Request, agent_num) -> web.Response:
    """List all IP aliases on the agent and the simulator host

    By default, the MIMIC SNMPTCP server listens on all the IP addresses (aliases) that are configured for an agent

    :param agent_num: Agent to manipulate SNMPTCP IP alias
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_snmptcp_set_config(request: web.Request, agent_num, argument, value) -> web.Response:
    """Set the agent&#39;s SNMPTCP configuration

    Agent&#39;s SNMPTCP configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to set the SNMPTCP configuration
    :type agent_num: int
    :param argument: Parameter to set the SNMPTCP configuration
    :type argument: str
    :param value: Value to set the SNMPTCP configuration
    :type value: str

    """
    return web.Response(status=200)


async def protocol_snmptcp_set_trace(request: web.Request, agent_num, enable_or_not) -> web.Response:
    """Set the agent&#39;s SNMPTCP traffic tracing

    1 to enable, 0 to disable

    :param agent_num: Agent to set the SNMPTCP tracing
    :type agent_num: int
    :param enable_or_not: Value to set the SNMPTCP tracing
    :type enable_or_not: str

    """
    return web.Response(status=200)
