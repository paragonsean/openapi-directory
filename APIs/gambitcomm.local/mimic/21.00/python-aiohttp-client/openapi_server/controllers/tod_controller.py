from typing import List, Dict
from aiohttp import web

from openapi_server.models.config_tod import ConfigTOD
from openapi_server import util


async def protocol_tod_get_args(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s TOD argument structure

    Agent&#39;s TOD configuration

    :param agent_num: Agent to show the TOD argument structure
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_tod_get_config(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s TOD configuration

    Agent&#39;s TOD configuration

    :param agent_num: Agent to show the TOD configuration
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_tod_get_statistics(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s TOD statistics

    Statistics of fields indicated in the headers

    :param agent_num: Agent to show TOD statistics
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_tod_get_stats_hdr(request: web.Request, ) -> web.Response:
    """Show the TOD statistics headers

    The headers of statistics fields


    """
    return web.Response(status=200)


async def protocol_tod_get_trace(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s TOD traffic tracing

    Trace 1 means enabled, 0 means not

    :param agent_num: Agent to show whether TOD tracing is enabled
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_tod_gettime(request: web.Request, agent_num, server_addr, port_num, script_name, time_sec, num_retries) -> web.Response:
    """Retrieve TOD time

    Retrive time from server

    :param agent_num: Agent to show TOD return
    :type agent_num: int
    :param server_addr: serverAddr
    :type server_addr: str
    :param port_num: portNum
    :type port_num: int
    :param script_name: scriptName
    :type script_name: str
    :param time_sec: timeSec
    :type time_sec: int
    :param num_retries: numRetries
    :type num_retries: int

    """
    return web.Response(status=200)


async def protocol_tod_set_config(request: web.Request, agent_num, argument, value) -> web.Response:
    """Set the agent&#39;s TOD configuration

    Agent&#39;s TOD configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to set the TOD configuration
    :type agent_num: int
    :param argument: Parameter to set the TOD configuration
    :type argument: str
    :param value: Value to set the TOD configuration
    :type value: str

    """
    return web.Response(status=200)


async def protocol_tod_set_trace(request: web.Request, agent_num, enable_or_not) -> web.Response:
    """Set the agent&#39;s TOD traffic tracing

    1 to enable, 0 to disable

    :param agent_num: Agent to set the TOD tracing
    :type agent_num: int
    :param enable_or_not: Value to set the TOD tracing
    :type enable_or_not: str

    """
    return web.Response(status=200)
