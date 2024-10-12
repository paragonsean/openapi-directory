from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def api_reactions_post(request: web.Request, category, reactable_id, reactable_type) -> web.Response:
    """create reaction

    This endpoint allows the client to create a reaction to a specified reactable (eg, Article, Comment, or User). For examples:         * \&quot;Like\&quot;ing an Article will create a new \&quot;like\&quot; Reaction from the user for that Articles         * \&quot;Like\&quot;ing that Article a second time will return the previous \&quot;like\&quot;

    :param category: 
    :type category: str
    :param reactable_id: 
    :type reactable_id: int
    :param reactable_type: 
    :type reactable_type: str

    """
    return web.Response(status=200)


async def api_reactions_toggle_post(request: web.Request, category, reactable_id, reactable_type) -> web.Response:
    """toggle reaction

    This endpoint allows the client to toggle the user&#39;s reaction to a specified reactable (eg, Article, Comment, or User). For examples:         * \&quot;Like\&quot;ing an Article will create a new \&quot;like\&quot; Reaction from the user for that Articles         * \&quot;Like\&quot;ing that Article a second time will remove the \&quot;like\&quot; from the user

    :param category: 
    :type category: str
    :param reactable_id: 
    :type reactable_id: int
    :param reactable_type: 
    :type reactable_type: str

    """
    return web.Response(status=200)
