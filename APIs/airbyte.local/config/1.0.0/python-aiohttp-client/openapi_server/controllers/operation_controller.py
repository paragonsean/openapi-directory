from typing import List, Dict
from aiohttp import web

from openapi_server.models.check_operation_read import CheckOperationRead
from openapi_server.models.connection_id_request_body import ConnectionIdRequestBody
from openapi_server.models.invalid_input_exception_info import InvalidInputExceptionInfo
from openapi_server.models.not_found_known_exception_info import NotFoundKnownExceptionInfo
from openapi_server.models.operation_create import OperationCreate
from openapi_server.models.operation_id_request_body import OperationIdRequestBody
from openapi_server.models.operation_read import OperationRead
from openapi_server.models.operation_read_list import OperationReadList
from openapi_server.models.operation_update import OperationUpdate
from openapi_server.models.operator_configuration import OperatorConfiguration
from openapi_server import util


async def check_operation(request: web.Request, body) -> web.Response:
    """Check if an operation to be created is valid

    

    :param body: 
    :type body: dict | bytes

    """
    body = OperatorConfiguration.from_dict(body)
    return web.Response(status=200)


async def create_operation(request: web.Request, body) -> web.Response:
    """Create an operation to be applied as part of a connection pipeline

    

    :param body: 
    :type body: dict | bytes

    """
    body = OperationCreate.from_dict(body)
    return web.Response(status=200)


async def delete_operation(request: web.Request, body) -> web.Response:
    """Delete an operation

    

    :param body: 
    :type body: dict | bytes

    """
    body = OperationIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def get_operation(request: web.Request, body) -> web.Response:
    """Returns an operation

    

    :param body: 
    :type body: dict | bytes

    """
    body = OperationIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def list_operations_for_connection(request: web.Request, body) -> web.Response:
    """Returns all operations for a connection.

    List operations for connection.

    :param body: 
    :type body: dict | bytes

    """
    body = ConnectionIdRequestBody.from_dict(body)
    return web.Response(status=200)


async def update_operation(request: web.Request, body) -> web.Response:
    """Update an operation

    

    :param body: 
    :type body: dict | bytes

    """
    body = OperationUpdate.from_dict(body)
    return web.Response(status=200)
