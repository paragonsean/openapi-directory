from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_model import ErrorModel
from openapi_server.models.link_collection import LinkCollection
from openapi_server.models.rti_transaction_base import RtiTransactionBase
from openapi_server import util


async def delete_rti_transaction(request: web.Request, employer_id, rti_transaction_id, authorization, api_version) -> web.Response:
    """Delete the RTI transaction

    Deletes the specified RTI transaction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param rti_transaction_id: The RTI transaction unique identifier. E.g. FPS001
    :type rti_transaction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_all_rti_transaction_tags_0(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get all RTI transaction tags

    Gets all the RTI transaction tags

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_rti_transaction_from_employer(request: web.Request, employer_id, rti_transaction_id, authorization, api_version) -> web.Response:
    """Get the RTI transaction

    Returns the specified RTI transaction

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param rti_transaction_id: The RTI transaction unique identifier. E.g. FPS001
    :type rti_transaction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_rti_transaction_summaries_from_employer(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get all RTI transaction summaries for the employer

    Get links for all RTI transaction summaries for the specified employer

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_rti_transaction_summary_from_employer(request: web.Request, employer_id, rti_transaction_id, authorization, api_version) -> web.Response:
    """Get the RTI transaction summary

    Returns the specified RTI transaction summary data excluding some poroperties

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param rti_transaction_id: The RTI transaction unique identifier. E.g. FPS001
    :type rti_transaction_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_rti_transactions_from_employer(request: web.Request, employer_id, authorization, api_version) -> web.Response:
    """Get all RTI transactions for the employer

    Get links for all RTI transactions for the specified employer

    :param employer_id: The employers&#39; unique identifier. E.g ER001
    :type employer_id: str
    :param authorization: The OAuth 1 authorization header. &amp;apos;Auto&amp;apos; enables auto complete.
    :type authorization: str
    :param api_version: The version of the api to target. Omit or set as &amp;apos;default&amp;apos; to target the current api version.
    :type api_version: str

    """
    return web.Response(status=200)


async def get_rti_transactions_with_tag_0(request: web.Request, employer_id, tag_id, authorization, api_version) -> web.Response:
    """Get RTI transactions with tag

    Gets the RTI transactions with the tag

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
