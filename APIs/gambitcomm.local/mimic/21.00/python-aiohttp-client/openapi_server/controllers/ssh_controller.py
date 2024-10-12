from typing import List, Dict
from aiohttp import web

from openapi_server.models.config_ssh import ConfigSSH
from openapi_server.models.ip_alias import IPAlias
from openapi_server import util


async def protocol_ssh_get_args(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s SSH argument structure

    Agent&#39;s SSH configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to show the SSH argument structure
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_ssh_get_config(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s SSH configuration

    Agent&#39;s SSH configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to show the SSH configuration
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_ssh_get_statistics(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s SSH statistics

    Statistics of fields indicated in the headers

    :param agent_num: Agent to show SSH statistics
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_ssh_get_stats_hdr(request: web.Request, ) -> web.Response:
    """Show the SSH statistics headers

    The headers of statistics fields


    """
    return web.Response(status=200)


async def protocol_ssh_get_trace(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s SSH traffic tracing

    Trace 1 means enabled, 0 means not

    :param agent_num: Agent to show whether SSH tracing is enabled
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_ssh_ipalias_disable(request: web.Request, agent_num, ipaddress, port) -> web.Response:
    """Disable individual IP aliases on the agent and the simulator host

    By default, the MIMIC SSH server listens on all the IP addresses (aliases) that are configured for an agent

    :param agent_num: Agent to manipulate SSH IP alias
    :type agent_num: int
    :param ipaddress: 
    :type ipaddress: str
    :param port: 
    :type port: int

    """
    return web.Response(status=200)


async def protocol_ssh_ipalias_enable(request: web.Request, agent_num, ipaddress, port) -> web.Response:
    """Enable individual IP aliases on the agent and the simulator host

    By default, the MIMIC SSH server listens on all the IP addresses (aliases) that are configured for an agent

    :param agent_num: Agent to manipulate SSH IP alias
    :type agent_num: int
    :param ipaddress: 
    :type ipaddress: str
    :param port: 
    :type port: int

    """
    return web.Response(status=200)


async def protocol_ssh_ipalias_isenabled(request: web.Request, agent_num, ipaddress, port) -> web.Response:
    """Check individual IP aliases on the agent and the simulator host

    By default, the MIMIC SSH server listens on all the IP addresses (aliases) that are configured for an agent

    :param agent_num: Agent to manipulate SSH IP alias
    :type agent_num: int
    :param ipaddress: 
    :type ipaddress: str
    :param port: 
    :type port: int

    """
    return web.Response(status=200)


async def protocol_ssh_ipalias_list(request: web.Request, agent_num) -> web.Response:
    """List all IP aliases on the agent and the simulator host

    By default, the MIMIC SSH server listens on all the IP addresses (aliases) that are configured for an agent

    :param agent_num: Agent to manipulate SSH IP alias
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_ssh_set_config(request: web.Request, agent_num, argument, value) -> web.Response:
    """Set the agent&#39;s SSH configuration

    Agent&#39;s SSH configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to set the SSH configuration
    :type agent_num: int
    :param argument: Parameter to set the SSH configuration
    :type argument: str
    :param value: Value to set the SSH configuration
    :type value: str

    """
    return web.Response(status=200)


async def protocol_ssh_set_trace(request: web.Request, agent_num, enable_or_not) -> web.Response:
    """Set the agent&#39;s SSH traffic tracing

    1 to enable, 0 to disable

    :param agent_num: Agent to set the SSH tracing
    :type agent_num: int
    :param enable_or_not: Value to set the SSH tracing
    :type enable_or_not: str

    """
    return web.Response(status=200)
