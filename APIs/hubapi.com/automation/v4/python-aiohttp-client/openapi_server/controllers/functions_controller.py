from typing import List, Dict
from aiohttp import web

from openapi_server.models.collection_response_public_action_function_identifier_no_paging import CollectionResponsePublicActionFunctionIdentifierNoPaging
from openapi_server.models.error import Error
from openapi_server.models.public_action_function import PublicActionFunction
from openapi_server.models.public_action_function_identifier import PublicActionFunctionIdentifier
from openapi_server import util


async def delete_automation_v4_actions_app_id_definition_id_functions_function_type_archive_by_function_type(request: web.Request, definition_id, function_type, app_id) -> web.Response:
    """Delete a function for a definition

    

    :param definition_id: 
    :type definition_id: str
    :param function_type: 
    :type function_type: str
    :param app_id: 
    :type app_id: int

    """
    return web.Response(status=200)


async def delete_automation_v4_actions_app_id_definition_id_functions_function_type_function_id_archive(request: web.Request, definition_id, function_type, function_id, app_id) -> web.Response:
    """Archive a function for a definition

    

    :param definition_id: 
    :type definition_id: str
    :param function_type: 
    :type function_type: str
    :param function_id: 
    :type function_id: str
    :param app_id: 
    :type app_id: int

    """
    return web.Response(status=200)


async def get_automation_v4_actions_app_id_definition_id_functions_function_type_function_id_get_by_id(request: web.Request, definition_id, function_type, function_id, app_id) -> web.Response:
    """Get a function for a given definition

    

    :param definition_id: 
    :type definition_id: str
    :param function_type: 
    :type function_type: str
    :param function_id: 
    :type function_id: str
    :param app_id: 
    :type app_id: int

    """
    return web.Response(status=200)


async def get_automation_v4_actions_app_id_definition_id_functions_function_type_get_by_function_type(request: web.Request, definition_id, function_type, app_id) -> web.Response:
    """Get all functions by a type for a given definition

    

    :param definition_id: 
    :type definition_id: str
    :param function_type: 
    :type function_type: str
    :param app_id: 
    :type app_id: int

    """
    return web.Response(status=200)


async def get_automation_v4_actions_app_id_definition_id_functions_get_page(request: web.Request, definition_id, app_id) -> web.Response:
    """Get all functions for a given definition

    

    :param definition_id: 
    :type definition_id: str
    :param app_id: 
    :type app_id: int

    """
    return web.Response(status=200)


async def put_automation_v4_actions_app_id_definition_id_functions_function_type_create_or_replace_by_function_type(request: web.Request, definition_id, function_type, app_id, body) -> web.Response:
    """Insert a function for a definition

    

    :param definition_id: 
    :type definition_id: str
    :param function_type: 
    :type function_type: str
    :param app_id: 
    :type app_id: int
    :param body: 
    :type body: str

    """
    return web.Response(status=200)


async def put_automation_v4_actions_app_id_definition_id_functions_function_type_function_id_create_or_replace(request: web.Request, definition_id, function_type, function_id, app_id, body) -> web.Response:
    """Insert a function for a definition

    

    :param definition_id: 
    :type definition_id: str
    :param function_type: 
    :type function_type: str
    :param function_id: 
    :type function_id: str
    :param app_id: 
    :type app_id: int
    :param body: 
    :type body: str

    """
    return web.Response(status=200)
