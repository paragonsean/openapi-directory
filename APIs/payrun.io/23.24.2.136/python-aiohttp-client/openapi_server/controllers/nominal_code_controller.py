from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link import Link
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.nominal_code import NominalCode
from openapi_server import util


async def delete_nominal_code(request: web.Request, employer_id, nominal_code_id, authorization, api_version) -> web.Response:
    """Deletes the nominal codes

    Deletes the nominal code

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param nominal_code_id: The nominal code unique identifier. E.g. NOM001
    :type nominal_code_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_nominal_code_from_employer(request: web.Request, employer_id, nominal_code_id, authorization, api_version) -> web.Response:
    """Gets the nominal code

    Gets the nominal code

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param nominal_code_id: The nominal code unique identifier. E.g. NOM001
    :type nominal_code_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_nominal_codes_from_employer(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Gets the nominal codes

    Gets the nominal code links

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def post_nominal_code(request: web.Request, employer_id, authorization, api_version, body) -> web.Response:
    """Insert nominal code

    Inserts a new nominal code

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The nominal code object.
    :type body: dict | bytes

    """
    body = NominalCode.from_dict(body)
    return web.Response(status=200)


async def put_nominal_code(request: web.Request, employer_id, nominal_code_id, authorization, api_version, body) -> web.Response:
    """Insert nominal code

    Inserts a new nominal code at the specified resource location

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param nominal_code_id: The nominal code unique identifier. E.g. NOM001
    :type nominal_code_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str
    :param body: The nominal code object.
    :type body: dict | bytes

    """
    body = NominalCode.from_dict(body)
    return web.Response(status=200)
