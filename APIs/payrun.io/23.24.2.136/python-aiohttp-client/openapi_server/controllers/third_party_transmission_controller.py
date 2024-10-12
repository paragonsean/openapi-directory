from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.third_party_transaction import ThirdPartyTransaction
from openapi_server import util


async def delete_third_party_transaction(request: web.Request, employer_id, third_party_transaction_id, authorization, api_version) -> web.Response:
    """Delete third party transaction

    Deletes a third party transaction record from the given resource location

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param third_party_transaction_id: The third party transaction unique identifier. E.g TP001
    :type third_party_transaction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_third_party_transaction(request: web.Request, employer_id, third_party_transaction_id, authorization, api_version) -> web.Response:
    """Get a third party transaction

    Get a third party transaction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param third_party_transaction_id: The third party transaction unique identifier. E.g TP001
    :type third_party_transaction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_third_party_transactions(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get all third party transaction links

    Get all third party transaction links

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)
