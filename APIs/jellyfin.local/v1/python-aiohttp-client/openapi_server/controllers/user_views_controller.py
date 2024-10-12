from typing import List, Dict
from aiohttp import web

from openapi_server.models.base_item_dto_query_result import BaseItemDtoQueryResult
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.special_view_option_dto import SpecialViewOptionDto
from openapi_server import util


async def get_grouping_options(request: web.Request, user_id) -> web.Response:
    """Get user view grouping options.

    

    :param user_id: User id.
    :type user_id: str
    :type user_id: str

    """
    return web.Response(status=200)


async def get_user_views(request: web.Request, user_id, include_external_content=None, preset_views=None, include_hidden=None) -> web.Response:
    """Get user views.

    

    :param user_id: User id.
    :type user_id: str
    :type user_id: str
    :param include_external_content: Whether or not to include external views such as channels or live tv.
    :type include_external_content: bool
    :param preset_views: Preset views.
    :type preset_views: List[str]
    :param include_hidden: Whether or not to include hidden content.
    :type include_hidden: bool

    """
    return web.Response(status=200)
