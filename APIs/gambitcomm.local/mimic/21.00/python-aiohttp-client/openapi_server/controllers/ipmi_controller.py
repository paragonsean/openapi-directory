from typing import List, Dict
from aiohttp import web

from openapi_server.models.config_ipmi import ConfigIPMI
from openapi_server import util


async def protocol_ipmi_get_args(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s IPMI argument structure

    Agent&#39;s IPMI configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to show the IPMI argument structure
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_ipmi_get_attr(request: web.Request, agent_num, attr) -> web.Response:
    """Show the outgoing message&#39;s attributes

    Attribute can be working_authtype ,session_id, outbound_seq, inbound_seq , field_N

    :param agent_num: Agent to set the IPMI tracing
    :type agent_num: int
    :param attr: Attribute
    :type attr: str

    """
    return web.Response(status=200)


async def protocol_ipmi_get_config(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s IPMI configuration

    Agent&#39;s IPMI configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to show the IPMI configuration
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_ipmi_get_statistics(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s IPMI statistics

    Statistics of fields indicated in the headers

    :param agent_num: Agent to show IPMI statistics
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_ipmi_get_stats_hdr(request: web.Request, ) -> web.Response:
    """Show the IPMI statistics headers

    The headers of statistics fields


    """
    return web.Response(status=200)


async def protocol_ipmi_get_trace(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s IPMI traffic tracing

    Trace 1 means enabled, 0 means not

    :param agent_num: Agent to show whether IPMI tracing is enabled
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_ipmi_set_attr(request: web.Request, agent_num, attr, value) -> web.Response:
    """Set the outgoing message&#39;s attributes

    Attribute can be working_authtype ,session_id, outbound_seq, inbound_seq , field_N

    :param agent_num: Agent to set the IPMI tracing
    :type agent_num: int
    :param attr: Attribute
    :type attr: str
    :param value: 
    :type value: str

    """
    return web.Response(status=200)


async def protocol_ipmi_set_config(request: web.Request, agent_num, argument, value) -> web.Response:
    """Set the agent&#39;s IPMI configuration

    Agent&#39;s IPMI configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to set the IPMI configuration
    :type agent_num: int
    :param argument: Parameter to set the IPMI configuration
    :type argument: str
    :param value: Value to set the IPMI configuration
    :type value: str

    """
    return web.Response(status=200)


async def protocol_ipmi_set_trace(request: web.Request, agent_num, enable_or_not) -> web.Response:
    """Set the agent&#39;s IPMI traffic tracing

    1 to enable, 0 to disable

    :param agent_num: Agent to set the IPMI tracing
    :type agent_num: int
    :param enable_or_not: Value to set the IPMI tracing
    :type enable_or_not: str

    """
    return web.Response(status=200)
