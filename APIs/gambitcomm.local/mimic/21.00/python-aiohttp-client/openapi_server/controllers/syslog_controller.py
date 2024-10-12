from typing import List, Dict
from aiohttp import web

from openapi_server.models.config_syslog import ConfigSYSLOG
from openapi_server.models.syslog_msg import SyslogMsg
from openapi_server import util


async def protocol_syslog_get_args(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s SYSLOG argument structure

    Agent&#39;s SYSLOG configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to show the SYSLOG argument structure
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_syslog_get_attr(request: web.Request, agent_num, attr) -> web.Response:
    """Show the outgoing message&#39;s attributes

    Attribute can be server , sequence , separator , hostname , timestamp

    :param agent_num: Agent to set the SYSLOG tracing
    :type agent_num: int
    :param attr: Attribute
    :type attr: str

    """
    return web.Response(status=200)


async def protocol_syslog_get_config(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s SYSLOG configuration

    Agent&#39;s SYSLOG configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to show the SYSLOG configuration
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_syslog_get_statistics(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s SYSLOG statistics

    Statistics of fields indicated in the headers

    :param agent_num: Agent to show SYSLOG statistics
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_syslog_get_stats_hdr(request: web.Request, ) -> web.Response:
    """Show the SYSLOG statistics headers

    The headers of statistics fields


    """
    return web.Response(status=200)


async def protocol_syslog_get_trace(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s SYSLOG traffic tracing

    Trace 1 means enabled, 0 means not

    :param agent_num: Agent to show whether SYSLOG tracing is enabled
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_syslog_send(request: web.Request, agent_num, pri, body) -> web.Response:
    """Set the agent&#39;s SYSLOG traffic tracing

    1 to enable, 0 to disable

    :param agent_num: Agent to set the SYSLOG tracing
    :type agent_num: int
    :param pri: Message Priority
    :type pri: int
    :param body: 
    :type body: dict | bytes

    """
    body = SyslogMsg.from_dict(body)
    return web.Response(status=200)


async def protocol_syslog_set_attr(request: web.Request, agent_num, attr, value) -> web.Response:
    """Set the outgoing message&#39;s attributes

    Attribute can be server , sequence , separator , hostname , timestamp

    :param agent_num: Agent to set the SYSLOG tracing
    :type agent_num: int
    :param attr: Attribute
    :type attr: str
    :param value: 
    :type value: str

    """
    return web.Response(status=200)


async def protocol_syslog_set_config(request: web.Request, agent_num, argument, value) -> web.Response:
    """Set the agent&#39;s SYSLOG configuration

    Agent&#39;s SYSLOG configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to set the SYSLOG configuration
    :type agent_num: int
    :param argument: Parameter to set the SYSLOG configuration
    :type argument: str
    :param value: Value to set the SYSLOG configuration
    :type value: str

    """
    return web.Response(status=200)


async def protocol_syslog_set_trace(request: web.Request, agent_num, enable_or_not) -> web.Response:
    """Set the agent&#39;s SYSLOG traffic tracing

    1 to enable, 0 to disable

    :param agent_num: Agent to set the SYSLOG tracing
    :type agent_num: int
    :param enable_or_not: Value to set the SYSLOG tracing
    :type enable_or_not: str

    """
    return web.Response(status=200)
