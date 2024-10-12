from typing import List, Dict
from aiohttp import web

from openapi_server.models.item_fields import ItemFields
from openapi_server.models.recommendation_dto import RecommendationDto
from openapi_server import util


async def get_movie_recommendations(request: web.Request, user_id=None, parent_id=None, fields=None, category_limit=None, item_limit=None) -> web.Response:
    """Gets movie recommendations.

    

    :param user_id: Optional. Filter by user id, and attach user data.
    :type user_id: str
    :type user_id: str
    :param parent_id: Specify this to localize the search to a specific item or folder. Omit to use the root.
    :type parent_id: str
    :type parent_id: str
    :param fields: Optional. The fields to return.
    :type fields: list | bytes
    :param category_limit: The max number of categories to return.
    :type category_limit: int
    :param item_limit: The max number of items to return per category.
    :type item_limit: int

    """
    fields = [ItemFields.from_dict(d) for d in fields]
    return web.Response(status=200)
