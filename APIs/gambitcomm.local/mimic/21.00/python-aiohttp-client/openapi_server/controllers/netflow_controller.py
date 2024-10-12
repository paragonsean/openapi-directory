from typing import List, Dict
from aiohttp import web

from openapi_server.models.config_netflow import ConfigNETFLOW
from openapi_server import util


async def protocol_netflow_change_attr(request: web.Request, agent_num, flowset_uid, field_num, attr, value) -> web.Response:
    """Change NETFLOW export attributes

    Change attributes

    :param agent_num: Agent to set the NETFLOW
    :type agent_num: int
    :param flowset_uid: 
    :type flowset_uid: int
    :param field_num: 
    :type field_num: int
    :param attr: 
    :type attr: str
    :param value: 
    :type value: str

    """
    return web.Response(status=200)


async def protocol_netflow_change_dfs(request: web.Request, agent_num, interval) -> web.Response:
    """Change NETFLOW data export interval

    Interval in msec .

    :param agent_num: Agent to set the NETFLOW
    :type agent_num: int
    :param interval: NETFLOW export interval
    :type interval: int

    """
    return web.Response(status=200)


async def protocol_netflow_change_tfs(request: web.Request, agent_num, interval) -> web.Response:
    """Change NETFLOW template export interval

    Interval in msec .

    :param agent_num: Agent to set the NETFLOW
    :type agent_num: int
    :param interval: NETFLOW export interval
    :type interval: int

    """
    return web.Response(status=200)


async def protocol_netflow_get_args(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s NETFLOW argument structure

    Agent&#39;s NETFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to show the NETFLOW argument structure
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_netflow_get_config(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s NETFLOW configuration

    Agent&#39;s NETFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to show the NETFLOW configuration
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_netflow_get_statistics(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s NETFLOW statistics

    Statistics of fields indicated in the headers

    :param agent_num: Agent to show NETFLOW statistics
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_netflow_get_stats_hdr(request: web.Request, ) -> web.Response:
    """Show the NETFLOW statistics headers

    The headers of statistics fields


    """
    return web.Response(status=200)


async def protocol_netflow_get_trace(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s NETFLOW traffic tracing

    Trace 1 means enabled, 0 means not

    :param agent_num: Agent to show whether NETFLOW tracing is enabled
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_netflow_halt(request: web.Request, agent_num) -> web.Response:
    """Halt NETFLOW traffic

    Halt NETFLOW traffic

    :param agent_num: Agent to set the NETFLOW
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_netflow_list(request: web.Request, agent_num) -> web.Response:
    """Show list of NETFLOW exports

    Show list of NETFLOW exports

    :param agent_num: Agent to show NETFLOW statistics
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_netflow_reload(request: web.Request, agent_num) -> web.Response:
    """Reload NETFLOW configuration before resuming traffic

    Reload NETFLOW configuration before resuming traffic

    :param agent_num: Agent to set the NETFLOW
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_netflow_resume(request: web.Request, agent_num) -> web.Response:
    """Resuming traffic

    Resuming traffic

    :param agent_num: Agent to set the NETFLOW
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_netflow_set_collector(request: web.Request, agent_num, collector_ip) -> web.Response:
    """Swap NETFLOW collector

    Allow changing collector without stopping agent

    :param agent_num: Agent to set the NETFLOW
    :type agent_num: int
    :param collector_ip: file name to load config
    :type collector_ip: str

    """
    return web.Response(status=200)


async def protocol_netflow_set_config(request: web.Request, agent_num, argument, value) -> web.Response:
    """Set the agent&#39;s NETFLOW configuration

    Agent&#39;s NETFLOW configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to set the NETFLOW configuration
    :type agent_num: int
    :param argument: Parameter to set the NETFLOW configuration
    :type argument: str
    :param value: Value to set the NETFLOW configuration
    :type value: str

    """
    return web.Response(status=200)


async def protocol_netflow_set_file_name(request: web.Request, agent_num, file_name) -> web.Response:
    """Swap NETFLOW configuration file

    Allow reloading the configuration file for an agent without stopping agent

    :param agent_num: Agent to set the NETFLOW
    :type agent_num: int
    :param file_name: file name to load config
    :type file_name: str

    """
    return web.Response(status=200)


async def protocol_netflow_set_trace(request: web.Request, agent_num, enable_or_not) -> web.Response:
    """Set the agent&#39;s NETFLOW traffic tracing

    1 to enable, 0 to disable

    :param agent_num: Agent to set the NETFLOW tracing
    :type agent_num: int
    :param enable_or_not: Value to set the NETFLOW tracing
    :type enable_or_not: str

    """
    return web.Response(status=200)
