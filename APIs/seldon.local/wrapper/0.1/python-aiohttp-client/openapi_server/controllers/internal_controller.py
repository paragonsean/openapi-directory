from typing import List, Dict
from aiohttp import web

from openapi_server.models.feedback import Feedback
from openapi_server.models.seldon_message import SeldonMessage
from openapi_server.models.seldon_message_list import SeldonMessageList
from openapi_server import util


async def aggregate(request: web.Request, body) -> web.Response:
    """aggregate

    

    :param body: 
    :type body: dict | bytes

    """
    body = .from_dict(body)
    return web.Response(status=200)


async def aggregate2(request: web.Request, _json=None) -> web.Response:
    """aggregate2

    

    :param _json: 
    :type _json: dict | bytes

    """
    _json = SeldonMessageList.from_dict(_json)
    return web.Response(status=200)


async def route(request: web.Request, _json=None) -> web.Response:
    """route

    

    :param _json: 
    :type _json: dict | bytes

    """
    _json = SeldonMessage.from_dict(_json)
    return web.Response(status=200)


async def route2(request: web.Request, _json) -> web.Response:
    """route2

    

    :param _json: 
    :type _json: dict | bytes

    """
    _json = .from_dict(_json)
    return web.Response(status=200)


async def send_feedback(request: web.Request, _json=None) -> web.Response:
    """send_feedback

    

    :param _json: 
    :type _json: dict | bytes

    """
    _json = Feedback.from_dict(_json)
    return web.Response(status=200)


async def send_feedback2(request: web.Request, _json) -> web.Response:
    """send_feedback2

    

    :param _json: 
    :type _json: dict | bytes

    """
    _json = .from_dict(_json)
    return web.Response(status=200)


async def transform_input(request: web.Request, _json=None) -> web.Response:
    """transform_input

    

    :param _json: 
    :type _json: dict | bytes

    """
    _json = SeldonMessage.from_dict(_json)
    return web.Response(status=200)


async def transform_input2(request: web.Request, _json) -> web.Response:
    """transform_input2

    

    :param _json: 
    :type _json: dict | bytes

    """
    _json = .from_dict(_json)
    return web.Response(status=200)


async def transform_input3(request: web.Request, _json=None) -> web.Response:
    """transform_input3

    

    :param _json: 
    :type _json: dict | bytes

    """
    _json = SeldonMessage.from_dict(_json)
    return web.Response(status=200)


async def transform_input4(request: web.Request, _json) -> web.Response:
    """transform_input4

    

    :param _json: 
    :type _json: dict | bytes

    """
    _json = .from_dict(_json)
    return web.Response(status=200)


async def transform_output(request: web.Request, _json=None) -> web.Response:
    """transform_output

    

    :param _json: 
    :type _json: dict | bytes

    """
    _json = SeldonMessage.from_dict(_json)
    return web.Response(status=200)


async def transform_output2(request: web.Request, _json) -> web.Response:
    """transform_output2

    

    :param _json: 
    :type _json: dict | bytes

    """
    _json = .from_dict(_json)
    return web.Response(status=200)
