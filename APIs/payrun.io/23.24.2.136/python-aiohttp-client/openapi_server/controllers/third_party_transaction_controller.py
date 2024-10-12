from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.tag import Tag
from openapi_server import util


async def delete_third_party_transaction_tag_0(request: web.Request, employer_id, third_party_transaction_id, tag_id, authorization, api_version) -> web.Response:
    """Delete third party transaction tag

    Deletes a tag from the third party transaction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param third_party_transaction_id: The third party transaction unique identifier. E.g TP001
    :type third_party_transaction_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_third_party_transaction_tags_0(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get all third party transaction tags

    Gets all the third party transaction tags

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_third_party_transactions_with_tag_0(request: web.Request, employer_id, tag_id, authorization, api_version) -> web.Response:
    """Get links to tagged third party transactions

    Gets the third party transactions with the specified tag

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tag_from_third_party_transaction_0(request: web.Request, employer_id, third_party_transaction_id, tag_id, authorization, api_version) -> web.Response:
    """Get third party transaction tag

    Gets a tag from the third party transaction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param third_party_transaction_id: The third party transaction unique identifier. E.g TP001
    :type third_party_transaction_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_tags_from_third_party_transaction_0(request: web.Request, employer_id, third_party_transaction_id, authorization, api_version) -> web.Response:
    """Get tags from third party transaction

    Gets all tags from the third party transaction

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


async def put_third_party_transaction_tag_0(request: web.Request, employer_id, third_party_transaction_id, tag_id, authorization, api_version) -> web.Response:
    """insert third party transaction tag

    Inserts a tag on the third party transaction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param third_party_transaction_id: The third party transaction unique identifier. E.g TP001
    :type third_party_transaction_id: str
    :param tag_id: The tag unique identifier. E.g. MyTag
    :type tag_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)
