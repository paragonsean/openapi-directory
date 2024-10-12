from typing import List, Dict
from aiohttp import web

from openapi_server.models.collection_response_public_action_definition_forward_paging import CollectionResponsePublicActionDefinitionForwardPaging
from openapi_server.models.error import Error
from openapi_server.models.public_action_definition import PublicActionDefinition
from openapi_server.models.public_action_definition_egg import PublicActionDefinitionEgg
from openapi_server.models.public_action_definition_patch import PublicActionDefinitionPatch
from openapi_server import util


async def delete_automation_v4_actions_app_id_definition_id_archive(request: web.Request, definition_id, app_id) -> web.Response:
    """Archive an extension definition

    

    :param definition_id: 
    :type definition_id: str
    :param app_id: 
    :type app_id: int

    """
    return web.Response(status=200)


async def get_automation_v4_actions_app_id_definition_id_get_by_id(request: web.Request, definition_id, app_id, archived=None) -> web.Response:
    """Get extension definition by Id

    

    :param definition_id: 
    :type definition_id: str
    :param app_id: 
    :type app_id: int
    :param archived: Whether to return only results that have been archived.
    :type archived: bool

    """
    return web.Response(status=200)


async def get_automation_v4_actions_app_id_get_page(request: web.Request, app_id, limit=None, after=None, archived=None) -> web.Response:
    """Get paged extension definitions

    

    :param app_id: 
    :type app_id: int
    :param limit: The maximum number of results to display per page.
    :type limit: int
    :param after: The paging cursor token of the last successfully read resource will be returned as the &#x60;paging.next.after&#x60; JSON property of a paged response containing more results.
    :type after: str
    :param archived: Whether to return only results that have been archived.
    :type archived: bool

    """
    return web.Response(status=200)


async def patch_automation_v4_actions_app_id_definition_id_update(request: web.Request, definition_id, app_id, body) -> web.Response:
    """Patch an existing extension definition

    

    :param definition_id: 
    :type definition_id: str
    :param app_id: 
    :type app_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PublicActionDefinitionPatch.from_dict(body)
    return web.Response(status=200)


async def post_automation_v4_actions_app_id_create(request: web.Request, app_id, body) -> web.Response:
    """Create a new extension definition

    

    :param app_id: 
    :type app_id: int
    :param body: 
    :type body: dict | bytes

    """
    body = PublicActionDefinitionEgg.from_dict(body)
    return web.Response(status=200)
