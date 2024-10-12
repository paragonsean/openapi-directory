from typing import List, Dict
from aiohttp import web

from openapi_server.models.config_telnet import ConfigTELNET
from openapi_server.models.ip_alias import IPAlias
from openapi_server.models.telnet_user import TelnetUser
from openapi_server import util


async def protocol_telnet_connection_logon(request: web.Request, agent_num, connection_id, user, password) -> web.Response:
    """Changes the connection&#39;s current logon.

    Logon change allows (hidden) commands for a different access mode to run.

    :param agent_num: Agent to manipulate TELNET connection
    :type agent_num: int
    :param connection_id: 
    :type connection_id: int
    :param user: 
    :type user: str
    :param password: 
    :type password: str

    """
    return web.Response(status=200)


async def protocol_telnet_connection_request(request: web.Request, agent_num, connection_id, command) -> web.Response:
    """Executes the command asynchronously .

    Equivalent of the command typed in by the user.

    :param agent_num: Agent to manipulate TELNET connection
    :type agent_num: int
    :param connection_id: 
    :type connection_id: int
    :param command: 
    :type command: str

    """
    return web.Response(status=200)


async def protocol_telnet_connection_signal(request: web.Request, agent_num, connection_id, signal_name) -> web.Response:
    """Triggers the asynchronous signal event with the specified signal name

    Signal name is either connect or idle

    :param agent_num: Agent to manipulate TELNET connection
    :type agent_num: int
    :param connection_id: 
    :type connection_id: int
    :param signal_name: 
    :type signal_name: str

    """
    return web.Response(status=200)


async def protocol_telnet_get_args(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s TELNET argument structure

    Agent&#39;s TELNET configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to show the TELNET argument structure
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_telnet_get_config(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s TELNET configuration

    Agent&#39;s TELNET configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to show the TELNET configuration
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_telnet_get_statistics(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s TELNET statistics

    Statistics of fields indicated in the headers

    :param agent_num: Agent to show TELNET statistics
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_telnet_get_stats_hdr(request: web.Request, ) -> web.Response:
    """Show the TELNET statistics headers

    The headers of statistics fields


    """
    return web.Response(status=200)


async def protocol_telnet_get_trace(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s TELNET traffic tracing

    Trace 1 means enabled, 0 means not

    :param agent_num: Agent to show whether TELNET tracing is enabled
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_telnet_ipalias_disable(request: web.Request, agent_num, ipaddress, port) -> web.Response:
    """Disable individual IP aliases on the agent and the simulator host

    By default, the MIMIC TELNET server listens on all the IP addresses (aliases) that are configured for an agent

    :param agent_num: Agent to manipulate TELNET IP alias
    :type agent_num: int
    :param ipaddress: 
    :type ipaddress: str
    :param port: 
    :type port: int

    """
    return web.Response(status=200)


async def protocol_telnet_ipalias_enable(request: web.Request, agent_num, ipaddress, port) -> web.Response:
    """Enable individual IP aliases on the agent and the simulator host

    By default, the MIMIC TELNET server listens on all the IP addresses (aliases) that are configured for an agent

    :param agent_num: Agent to manipulate TELNET IP alias
    :type agent_num: int
    :param ipaddress: 
    :type ipaddress: str
    :param port: 
    :type port: int

    """
    return web.Response(status=200)


async def protocol_telnet_ipalias_isenabled(request: web.Request, agent_num, ipaddress, port) -> web.Response:
    """Check individual IP aliases on the agent and the simulator host

    By default, the MIMIC TELNET server listens on all the IP addresses (aliases) that are configured for an agent

    :param agent_num: Agent to manipulate TELNET IP alias
    :type agent_num: int
    :param ipaddress: 
    :type ipaddress: str
    :param port: 
    :type port: int

    """
    return web.Response(status=200)


async def protocol_telnet_ipalias_list(request: web.Request, agent_num) -> web.Response:
    """List all IP aliases on the agent and the simulator host

    By default, the MIMIC TELNET server listens on all the IP addresses (aliases) that are configured for an agent

    :param agent_num: Agent to manipulate TELNET IP alias
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_telnet_server_get_connections(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s TELNET connections

    IDs of all connected connections

    :param agent_num: Agent to show TELNET configuration
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_telnet_server_get_keymap(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s TELNET keymap file name

    Keymap file name

    :param agent_num: Agent to show TELNET statistics
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_telnet_server_get_rulesdb(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s TELNET rules db file name

    Rules db file name

    :param agent_num: Agent to show TELNET statistics
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_telnet_server_get_state(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s TELNET server state

    Return 1 means accepting connections, 0 not

    :param agent_num: Agent to show TELNET statistics
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_telnet_server_get_userdb(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s TELNET user db file name

    User db file name

    :param agent_num: Agent to show TELNET statistics
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_telnet_server_get_users(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s TELNET users

    List of users

    :param agent_num: Agent to show TELNET configuration
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_telnet_set_config(request: web.Request, agent_num, argument, value) -> web.Response:
    """Set the agent&#39;s TELNET configuration

    Agent&#39;s TELNET configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to set the TELNET configuration
    :type agent_num: int
    :param argument: Parameter to set the TELNET configuration
    :type argument: str
    :param value: Value to set the TELNET configuration
    :type value: str

    """
    return web.Response(status=200)


async def protocol_telnet_set_trace(request: web.Request, agent_num, enable_or_not) -> web.Response:
    """Set the agent&#39;s TELNET traffic tracing

    1 to enable, 0 to disable

    :param agent_num: Agent to set the TELNET tracing
    :type agent_num: int
    :param enable_or_not: Value to set the TELNET tracing
    :type enable_or_not: str

    """
    return web.Response(status=200)
