from typing import List, Dict
from aiohttp import web

from openapi_server.models.audit import Audit
from openapi_server.models.feedback import Feedback
from openapi_server import util


async def create_feedbacks(request: web.Request, body) -> web.Response:
    """Create a feedback

    Create a feedback

    :param body: JSON object Feedback
    :type body: dict | bytes

    """
    body = Feedback.from_dict(body)
    return web.Response(status=200)


async def get_feedbacks(request: web.Request, fields=None) -> web.Response:
    """Get feedbacks

    Returns a list of feedbacks

    :param fields: Fields to return separate by comas (es. name,id)
    :type fields: str

    """
    return web.Response(status=200)


async def get_fields_feedbacks(request: web.Request, ) -> web.Response:
    """Get the list of fields

    Returns a list of fields


    """
    return web.Response(status=200)
