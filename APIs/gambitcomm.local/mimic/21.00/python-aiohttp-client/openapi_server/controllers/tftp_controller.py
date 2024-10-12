from typing import List, Dict
from aiohttp import web

from openapi_server.models.config_tftp import ConfigTFTP
from openapi_server import util


async def protocol_tftp_get_args(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s TFTP argument structure

    Agent&#39;s TFTP configuration with port,rule,prompt,paging_prompt,userdb,keymap

    :param agent_num: Agent to show the TFTP argument structure
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_tftp_get_config(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s TFTP configuration

    Agent&#39;s TFTP configuration

    :param agent_num: Agent to show the TFTP configuration
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_tftp_get_statistics(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s TFTP statistics

    Statistics of fields indicated in the headers

    :param agent_num: Agent to show TFTP statistics
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_tftp_get_stats_hdr(request: web.Request, ) -> web.Response:
    """Show the TFTP statistics headers

    The headers of statistics fields


    """
    return web.Response(status=200)


async def protocol_tftp_get_trace(request: web.Request, agent_num) -> web.Response:
    """Show the agent&#39;s TFTP traffic tracing

    Trace 1 means enabled, 0 means not

    :param agent_num: Agent to show whether TFTP tracing is enabled
    :type agent_num: int

    """
    return web.Response(status=200)


async def protocol_tftp_session_get_parameter(request: web.Request, agent_num, session_id, parameter) -> web.Response:
    """Show a parameter of a TFTP sesssion

    Parameter is server , port , or dstfile

    :param agent_num: Agent to show TFTP parameter
    :type agent_num: int
    :param session_id: SessionID
    :type session_id: str
    :param parameter: Parameter to show
    :type parameter: str

    """
    return web.Response(status=200)


async def protocol_tftp_session_read(request: web.Request, agent_num, srcfile) -> web.Response:
    """Create a read session to download srcfile from server

    Session ID is returned

    :param agent_num: Agent to show TFTP statistics
    :type agent_num: int
    :param srcfile: File name to retrieve from server
    :type srcfile: str

    """
    return web.Response(status=200)


async def protocol_tftp_session_set_parameter(request: web.Request, agent_num, session_id, parameter, value) -> web.Response:
    """Set a parameter of a TFTP sesssion

    Parameter is server , port , or dstfile

    :param agent_num: Agent to set TFTP parameter
    :type agent_num: int
    :param session_id: SessionID
    :type session_id: str
    :param parameter: Parameter to set
    :type parameter: str
    :param value: Value to set
    :type value: str

    """
    return web.Response(status=200)


async def protocol_tftp_session_start(request: web.Request, agent_num, session_id) -> web.Response:
    """Start a TFTP sesssion

    Start uploading or downloading the file

    :param agent_num: Agent to start TFTP transaction
    :type agent_num: int
    :param session_id: SessionID
    :type session_id: str

    """
    return web.Response(status=200)


async def protocol_tftp_session_status(request: web.Request, agent_num, session_id) -> web.Response:
    """Check a TFTP sesssion&#39;s status

    Status includes running state, bytes transfered, and time elapsed

    :param agent_num: Agent to show TFTP transaction
    :type agent_num: int
    :param session_id: SessionID
    :type session_id: str

    """
    return web.Response(status=200)


async def protocol_tftp_session_stop(request: web.Request, agent_num, session_id) -> web.Response:
    """Stop a TFTP sesssion

    Stop uploading or downloading the file

    :param agent_num: Agent to stop TFTP transaction
    :type agent_num: int
    :param session_id: SessionID
    :type session_id: str

    """
    return web.Response(status=200)


async def protocol_tftp_session_write(request: web.Request, agent_num, srcfile) -> web.Response:
    """Create a read session to upload srcfile to server

    Session ID is returned

    :param agent_num: Agent to show TFTP statistics
    :type agent_num: int
    :param srcfile: File name to upload to server
    :type srcfile: str

    """
    return web.Response(status=200)


async def protocol_tftp_set_config(request: web.Request, agent_num, argument, value) -> web.Response:
    """Set the agent&#39;s TFTP configuration

    Agent&#39;s TFTP configuration

    :param agent_num: Agent to set the TFTP configuration
    :type agent_num: int
    :param argument: Parameter to set the TFTP configuration
    :type argument: str
    :param value: Value to set the TFTP configuration
    :type value: str

    """
    return web.Response(status=200)


async def protocol_tftp_set_trace(request: web.Request, agent_num, enable_or_not) -> web.Response:
    """Set the agent&#39;s TFTP traffic tracing

    1 to enable, 0 to disable

    :param agent_num: Agent to set the TFTP tracing
    :type agent_num: int
    :param enable_or_not: Value to set the TFTP tracing
    :type enable_or_not: str

    """
    return web.Response(status=200)
