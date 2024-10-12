from typing import List, Dict
from aiohttp import web

from openapi_server.models.config_sflow import ConfigSFLOW
from openapi_server import util


async def protocol_sflow_get_args(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s SFLOW argument structure

    Agent&#39;s SFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to show the SFLOW argument structure
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_sflow_get_config(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s SFLOW configuration

    Agent&#39;s SFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to show the SFLOW configuration
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_sflow_get_statistics(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s SFLOW statistics

    Statistics of fields indicated in the headers

    :param agent_num: Agent to show SFLOW statistics
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_sflow_get_stats_hdr(request: web.Request, ) -> web.Response:
    """Show the SFLOW statistics headers

    The headers of statistics fields


    """
    return web.Response(status=200)


async def protocol_sflow_get_trace(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s SFLOW traffic tracing

    Trace 1 means enabled, 0 means not

    :param agent_num: Agent to show whether SFLOW tracing is enabled
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_sflow_halt(request: web.Request, agent_num) -> web.Response:
    """Halt SFLOW traffic

    Halt SFLOW traffic

    :param agent_num: Agent to set the SFLOW
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_sflow_reload(request: web.Request, agent_num) -> web.Response:
    """Reload SFLOW configuration before resuming traffic

    Reload SFLOW configuration before resuming traffic

    :param agent_num: Agent to set the SFLOW
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_sflow_resume(request: web.Request, agent_num) -> web.Response:
    """Resuming traffic

    Resuming traffic

    :param agent_num: Agent to set the SFLOW
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_sflow_set_config(request: web.Request, agent_num, argument, value) -> web.Response:
    """Set the agent&#39;s SFLOW configuration

    Agent&#39;s SFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to set the SFLOW configuration
    :type agent_num: int
    :param argument: Parameter to set the SFLOW configuration
    :type argument: str
    :param value: Value to set the SFLOW configuration
    :type value: str

    """
    return web.Response(status=200)


async def protocol_sflow_set_trace(request: web.Request, agent_num, enable_or_not) -> web.Response:
    """Set the agent&#39;s SFLOW traffic tracing

    1 to enable, 0 to disable

    :param agent_num: Agent to set the SFLOW tracing
    :type agent_num: int
    :param enable_or_not: Value to set the SFLOW tracing
    :type enable_or_not: str

    """
    return web.Response(status=200)
