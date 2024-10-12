from typing import List, Dict
from aiohttp import web

from openapi_server.models.government_department import GovernmentDepartment
from openapi_server.models.government_opposition_post_item import GovernmentOppositionPostItem
from openapi_server.models.member_item import MemberItem
from openapi_server.models.post_type import PostType
from openapi_server import util


async def api_posts_departments_type_get(request: web.Request, type) -> web.Response:
    """Returns a list of departments.

    

    :param type: Departments by type
    :type type: dict | bytes

    """
    type = .from_dict(type)
    return web.Response(status=200)


async def api_posts_government_posts_get(request: web.Request, department_id=None) -> web.Response:
    """Returns a list of government posts.

    

    :param department_id: Government posts by department ID
    :type department_id: int

    """
    return web.Response(status=200)


async def api_posts_opposition_posts_get(request: web.Request, department_id=None) -> web.Response:
    """Returns a list of opposition posts.

    

    :param department_id: Opposition posts by department ID
    :type department_id: int

    """
    return web.Response(status=200)


async def api_posts_speaker_and_deputies_for_date_get(request: web.Request, for_date) -> web.Response:
    """Returns a list containing the speaker and deputy speakers.

    

    :param for_date: Speaker and deputy speakers for date specified
    :type for_date: str

    """
    for_date = util.deserialize_datetime(for_date)
    return web.Response(status=200)


async def api_posts_spokespersons_get(request: web.Request, party_id=None) -> web.Response:
    """Returns a list of spokespersons.

    

    :param party_id: Spokespersons by party ID
    :type party_id: int

    """
    return web.Response(status=200)
