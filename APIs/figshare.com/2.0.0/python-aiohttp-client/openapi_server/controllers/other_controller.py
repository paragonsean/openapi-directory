from typing import List, Dict
from aiohttp import web

from openapi_server.models.account import Account
from openapi_server.models.category import Category
from openapi_server.models.error_message import ErrorMessage
from openapi_server.models.funding_information import FundingInformation
from openapi_server.models.funding_search import FundingSearch
from openapi_server.models.item_type import ItemType
from openapi_server.models.license import License
from openapi_server import util


async def categories_list(request: web.Request, ) -> web.Response:
    """Public Categories

    Returns a list of public categories


    """
    return web.Response(status=200)


async def file_download(request: web.Request, file_id) -> web.Response:
    """Public File Download

    Starts the download of a file

    :param file_id: 
    :type file_id: int

    """
    return web.Response(status=200)


async def item_types_list(request: web.Request, group_id=None) -> web.Response:
    """Item Types

    Returns the list of Item Types of the requested group. If no user is authenticated, returns the item types available for Figshare.

    :param group_id: Identifier of the group for which the item types are requested
    :type group_id: int

    """
    return web.Response(status=200)


async def licenses_list(request: web.Request, ) -> web.Response:
    """Public Licenses

    Returns a list of public licenses


    """
    return web.Response(status=200)


async def private_account(request: web.Request, ) -> web.Response:
    """Private Account information

    Account information for token/personal token


    """
    return web.Response(status=200)


async def private_funding_search(request: web.Request, body=None) -> web.Response:
    """Search Funding

    Search for fundings

    :param body: Search Parameters
    :type body: dict | bytes

    """
    body = FundingSearch.from_dict(body)
    return web.Response(status=200)


async def private_licenses_list(request: web.Request, ) -> web.Response:
    """Private Account Licenses

    This is a private endpoint that requires OAuth. It will return a list with figshare public licenses AND licenses defined for account&#39;s institution.


    """
    return web.Response(status=200)
