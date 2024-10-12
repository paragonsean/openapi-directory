from typing import List, Dict
from aiohttp import web

from openapi_server.models.collection_response_public_action_revision_forward_paging import CollectionResponsePublicActionRevisionForwardPaging
from openapi_server.models.error import Error
from openapi_server.models.public_action_revision import PublicActionRevision
from openapi_server import util


async def get_automation_v4_actions_app_id_definition_id_revisions_get_page(request: web.Request, definition_id, app_id, limit=None, after=None) -> web.Response:
    """Get all revisions for a given definition

    

    :param definition_id: 
    :type definition_id: str
    :param app_id: 
    :type app_id: int
    :param limit: The maximum number of results to display per page.
    :type limit: int
    :param after: The paging cursor token of the last successfully read resource will be returned as the &#x60;paging.next.after&#x60; JSON property of a paged response containing more results.
    :type after: str

    """
    return web.Response(status=200)


async def get_automation_v4_actions_app_id_definition_id_revisions_revision_id_get_by_id(request: web.Request, definition_id, revision_id, app_id) -> web.Response:
    """Gets a revision for a given definition by revision id

    

    :param definition_id: 
    :type definition_id: str
    :param revision_id: 
    :type revision_id: str
    :param app_id: 
    :type app_id: int

    """
    return web.Response(status=200)
