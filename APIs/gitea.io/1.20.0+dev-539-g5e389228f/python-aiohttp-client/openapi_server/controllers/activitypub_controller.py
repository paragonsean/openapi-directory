from typing import List, Dict
from aiohttp import web

from openapi_server.models.activity_pub import ActivityPub
from openapi_server import util


async def activitypub_person(request: web.Request, user_id) -> web.Response:
    """Returns the Person actor for a user

    

    :param user_id: user ID of the user
    :type user_id: int

    """
    return web.Response(status=200)


async def activitypub_person_inbox(request: web.Request, user_id) -> web.Response:
    """Send to the inbox

    

    :param user_id: user ID of the user
    :type user_id: int

    """
    return web.Response(status=200)
