from typing import List, Dict
from aiohttp import web

from openapi_server.models.card import Card
from openapi_server.models.create_custom_card_request import CreateCustomCardRequest
from openapi_server.models.font_for_customizer import FontForCustomizer
from openapi_server.models.upload_custom_logo200_response import UploadCustomLogo200Response
from openapi_server import util


async def create_custom_card(request: web.Request, body) -> web.Response:
    """Create a new custom card

    

    :param body: additional parameters
    :type body: dict | bytes

    """
    body = CreateCustomCardRequest.from_dict(body)
    return web.Response(status=200)


async def fonts_list_for_customizer(request: web.Request, ) -> web.Response:
    """Lists fonts available for use with the card customizer

    


    """
    return web.Response(status=200)


async def upload_custom_logo(request: web.Request, file, type, uid) -> web.Response:
    """upload logo or cover image for card

    

    :param file: upload images for customc cards
    :type file: str
    :param type: set to cover or header
    :type type: str
    :param uid: uid of the user
    :type uid: str

    """
    return web.Response(status=200)
