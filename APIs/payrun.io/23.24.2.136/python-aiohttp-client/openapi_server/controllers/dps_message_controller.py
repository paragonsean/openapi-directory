from typing import List, Dict
from aiohttp import web

from openapi_server.models.dps_message import DpsMessage
from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server import util


async def delete_dps_message(request: web.Request, employer_id, dps_message_id, authorization, api_version) -> web.Response:
    """Deletes the DPS message

    Deletes the DPS message

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param dps_message_id: The DPS message unique identifier. E.g. DPS001
    :type dps_message_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_dps_message_from_employer(request: web.Request, employer_id, dps_message_id, authorization, api_version) -> web.Response:
    """Gets the DPS message

    Gets the DPS message

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param dps_message_id: The DPS message unique identifier. E.g. DPS001
    :type dps_message_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_dps_messages_from_employer(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Gets the DPS messages

    Gets the DPS message links

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def patch_dps_message(request: web.Request, employer_id, dps_message_id, authorization, api_version) -> web.Response:
    """Patches the DPS message

    Patches the specified DPS message with the supplied values

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param dps_message_id: The DPS message unique identifier. E.g. DPS001
    :type dps_message_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def post_dps_message(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Posta the DPS message

    Insert new DPS message

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def put_dps_message(request: web.Request, employer_id, dps_message_id, authorization, api_version) -> web.Response:
    """Puts the DPS message

    Puts the DPS message

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param dps_message_id: The DPS message unique identifier. E.g. DPS001
    :type dps_message_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)
