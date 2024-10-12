from typing import List, Dict
from aiohttp import web

from openapi_server.models.case_type import CaseType
from openapi_server.models.lorem_type import LoremType
from openapi_server.models.text_action_type import TextActionType
from openapi_server.models.text_dto import TextDto
from openapi_server.models.text_type import TextType
from openapi_server import util


async def api_text_humanize_post(request: web.Request, body, x_api_key=None) -> web.Response:
    """Humanize text

    

    :param body: 
    :type body: dict | bytes
    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    body = TextDto.from_dict(body)
    return web.Response(status=200)


async def api_text_lorem_ipsum_get(request: web.Request, lorem_type, type, number, x_api_key=None) -> web.Response:
    """Generate lorem ipsum

    

    :param lorem_type: 
    :type lorem_type: dict | bytes
    :param type: 
    :type type: dict | bytes
    :param number: 
    :type number: int
    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    lorem_type = .from_dict(lorem_type)
    type = .from_dict(type)
    return web.Response(status=200)


async def api_text_password_get(request: web.Request, length, has_digits, has_uppercase, has_special, x_api_key=None) -> web.Response:
    """Generate password

    

    :param length: 
    :type length: int
    :param has_digits: 
    :type has_digits: bool
    :param has_uppercase: 
    :type has_uppercase: bool
    :param has_special: 
    :type has_special: bool
    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    return web.Response(status=200)


async def api_text_review_post(request: web.Request, product, quantity, x_api_key=None) -> web.Response:
    """Get reviews (max quantity&#x3D;500)

    

    :param product: 
    :type product: str
    :param quantity: 
    :type quantity: int
    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    return web.Response(status=200)


async def api_text_transform_post(request: web.Request, text_action_type, body, case_type=None, find=None, replace=None, x_api_key=None) -> web.Response:
    """Transform text

    

    :param text_action_type: 
    :type text_action_type: dict | bytes
    :param body: 
    :type body: dict | bytes
    :param case_type: 
    :type case_type: dict | bytes
    :param find: 
    :type find: str
    :param replace: 
    :type replace: str
    :param x_api_key: Enter your key
    :type x_api_key: str

    """
    text_action_type = .from_dict(text_action_type)
    body = TextDto.from_dict(body)
    case_type = .from_dict(case_type)
    return web.Response(status=200)
