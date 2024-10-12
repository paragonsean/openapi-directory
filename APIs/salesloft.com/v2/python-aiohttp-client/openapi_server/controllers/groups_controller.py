from typing import List, Dict
from aiohttp import web

from openapi_server.models.group import Group
from openapi_server import util


async def v2_groups_id_json_get(request: web.Request, id) -> web.Response:
    """Fetch a group

    Fetches a group, by ID only. 

    :param id: Group ID
    :type id: str

    """
    return web.Response(status=200)


async def v2_groups_json_get(request: web.Request, ids=None, sort_by=None, sort_direction=None) -> web.Response:
    """List groups

    Fetches multiple group records. The records can be filtered, and sorted according to the respective parameters. 

    :param ids: IDs of groups to fetch.
    :type ids: List[int]
    :param sort_by: Key to sort on, must be one of: created_at, updated_at. Defaults to updated_at
    :type sort_by: str
    :param sort_direction: Direction to sort in, must be one of: ASC, DESC. Defaults to DESC
    :type sort_direction: str

    """
    return web.Response(status=200)
