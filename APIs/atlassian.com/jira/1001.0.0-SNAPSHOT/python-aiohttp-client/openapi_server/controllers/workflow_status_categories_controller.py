from typing import List, Dict
from aiohttp import web

from openapi_server.models.status_category import StatusCategory
from openapi_server import util


async def get_status_categories(request: web.Request, ) -> web.Response:
    """Get all status categories

    Returns a list of all status categories.  **[Permissions](#permissions) required:** Permission to access Jira.


    """
    return web.Response(status=200)


async def get_status_category(request: web.Request, id_or_key) -> web.Response:
    """Get status category

    Returns a status category. Status categories provided a mechanism for categorizing [statuses](#api-rest-api-3-status-idOrName-get).  **[Permissions](#permissions) required:** Permission to access Jira.

    :param id_or_key: The ID or key of the status category.
    :type id_or_key: str

    """
    return web.Response(status=200)
