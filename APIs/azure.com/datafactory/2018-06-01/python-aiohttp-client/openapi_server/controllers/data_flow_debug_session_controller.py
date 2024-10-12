from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_data_flow_to_debug_session_response import AddDataFlowToDebugSessionResponse
from openapi_server.models.cloud_error import CloudError
from openapi_server.models.create_data_flow_debug_session_request import CreateDataFlowDebugSessionRequest
from openapi_server.models.create_data_flow_debug_session_response import CreateDataFlowDebugSessionResponse
from openapi_server.models.data_flow_debug_command_request import DataFlowDebugCommandRequest
from openapi_server.models.data_flow_debug_command_response import DataFlowDebugCommandResponse
from openapi_server.models.data_flow_debug_package import DataFlowDebugPackage
from openapi_server.models.delete_data_flow_debug_session_request import DeleteDataFlowDebugSessionRequest
from openapi_server.models.query_data_flow_debug_sessions_response import QueryDataFlowDebugSessionsResponse
from openapi_server import util


async def data_flow_debug_session_add_data_flow(request: web.Request, subscription_id, resource_group_name, factory_name, api_version, request) -> web.Response:
    """data_flow_debug_session_add_data_flow

    Add a data flow into debug session.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param api_version: The API version.
    :type api_version: str
    :param request: Data flow debug session definition with debug content.
    :type request: dict | bytes

    """
    request = DataFlowDebugPackage.from_dict(request)
    return web.Response(status=200)


async def data_flow_debug_session_create(request: web.Request, subscription_id, resource_group_name, factory_name, api_version, request) -> web.Response:
    """data_flow_debug_session_create

    Creates a data flow debug session.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param api_version: The API version.
    :type api_version: str
    :param request: Data flow debug session definition
    :type request: dict | bytes

    """
    request = CreateDataFlowDebugSessionRequest.from_dict(request)
    return web.Response(status=200)


async def data_flow_debug_session_delete(request: web.Request, subscription_id, resource_group_name, factory_name, api_version, request) -> web.Response:
    """data_flow_debug_session_delete

    Deletes a data flow debug session.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param api_version: The API version.
    :type api_version: str
    :param request: Data flow debug session definition for deletion
    :type request: dict | bytes

    """
    request = DeleteDataFlowDebugSessionRequest.from_dict(request)
    return web.Response(status=200)


async def data_flow_debug_session_execute_command(request: web.Request, subscription_id, resource_group_name, factory_name, api_version, request) -> web.Response:
    """data_flow_debug_session_execute_command

    Execute a data flow debug command.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param api_version: The API version.
    :type api_version: str
    :param request: Data flow debug command definition.
    :type request: dict | bytes

    """
    request = DataFlowDebugCommandRequest.from_dict(request)
    return web.Response(status=200)


async def data_flow_debug_session_query_by_factory(request: web.Request, subscription_id, resource_group_name, factory_name, api_version) -> web.Response:
    """data_flow_debug_session_query_by_factory

    Query all active data flow debug sessions.

    :param subscription_id: The subscription identifier.
    :type subscription_id: str
    :param resource_group_name: The resource group name.
    :type resource_group_name: str
    :param factory_name: The factory name.
    :type factory_name: str
    :param api_version: The API version.
    :type api_version: str

    """
    return web.Response(status=200)
