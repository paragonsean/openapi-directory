from typing import List, Dict
from aiohttp import web

from openapi_server.models.feedback import Feedback
from openapi_server import util


async def get_feedback(request: web.Request, authorization, feedback_id) -> web.Response:
    """get_feedback

    Retrieve feedback

    :param authorization: Authorization token (provided upon successful login)
    :type authorization: str
    :param feedback_id: 
    :type feedback_id: str

    """
    return web.Response(status=200)


async def send_feedback(request: web.Request, body) -> web.Response:
    """send_feedback

    Submit feedback for the bank

    :param body: Feedback details including name, email the subject and complete message
    :type body: dict | bytes

    """
    body = Feedback.from_dict(body)
    return web.Response(status=200)
