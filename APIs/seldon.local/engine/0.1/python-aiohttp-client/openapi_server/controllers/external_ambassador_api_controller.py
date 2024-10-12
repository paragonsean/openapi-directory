from typing import List, Dict
from aiohttp import web

from openapi_server.models.feedback import Feedback
from openapi_server.models.seldon_message import SeldonMessage
from openapi_server import util


async def predict(request: web.Request, namespace, deployment, body) -> web.Response:
    """predict

    

    :param namespace: 
    :type namespace: str
    :param deployment: 
    :type deployment: str
    :param body: 
    :type body: dict | bytes

    """
    body = SeldonMessage.from_dict(body)
    return web.Response(status=200)


async def send_feedback(request: web.Request, namespace, deployment, body) -> web.Response:
    """send_feedback

    

    :param namespace: 
    :type namespace: str
    :param deployment: 
    :type deployment: str
    :param body: 
    :type body: dict | bytes

    """
    body = Feedback.from_dict(body)
    return web.Response(status=200)
