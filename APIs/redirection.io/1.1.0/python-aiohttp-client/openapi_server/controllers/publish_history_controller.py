from typing import List, Dict
from aiohttp import web

from openapi_server.models.publish_history_read import PublishHistoryRead
from openapi_server import util


async def get_publish_history_collection(request: web.Request, project_id, created_at_before=None, created_at_strictly_before=None, created_at_after=None, created_at_strictly_after=None, page=None) -> web.Response:
    """Retrieves the collection of PublishHistory resources.

    

    :param project_id: 
    :type project_id: str
    :param created_at_before: 
    :type created_at_before: str
    :param created_at_strictly_before: 
    :type created_at_strictly_before: str
    :param created_at_after: 
    :type created_at_after: str
    :param created_at_strictly_after: 
    :type created_at_strictly_after: str
    :param page: The collection page number
    :type page: int

    """
    return web.Response(status=200)


async def get_publish_history_item(request: web.Request, id) -> web.Response:
    """Retrieves a PublishHistory resource.

    

    :param id: 
    :type id: str

    """
    return web.Response(status=200)
