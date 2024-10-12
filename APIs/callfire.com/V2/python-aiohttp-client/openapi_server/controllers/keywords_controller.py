from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.keyword_config import KeywordConfig
from openapi_server.models.keyword_lease import KeywordLease
from openapi_server.models.keyword_lease_page import KeywordLeasePage
from openapi_server.models.keyword_list import KeywordList
from openapi_server.models.page import Page
from openapi_server import util


async def find_keyword_lease_configs(request: web.Request, limit=None, offset=None, filter=None, label_name=None, fields=None) -> web.Response:
    """Find keyword lease configs

    Searches for all keyword lease configs for the user. Returns a paged list of KeywordConfig

    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param offset: Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    :type offset: int
    :param filter: Filter by part of Keyword name or Label name of Keyword
    :type filter: str
    :param label_name: An exact label name to search by
    :type label_name: str
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def find_keyword_leases(request: web.Request, limit=None, offset=None, filter=None, label_name=None, fields=None) -> web.Response:
    """Find keyword leases

    Searches for all keywords owned by user. A keyword lease is the ownership information involving a keyword

    :param limit: To set the maximum number of records to return in a paged list response. The default is 100
    :type limit: int
    :param offset: Offset to the start of a given page. The default is 0. Check [pagination](https://developers.callfire.com/docs.html#pagination) page for more information about pagination in CallFire API.
    :type offset: int
    :param filter: Filter by part of Keyword name or Label name of Keyword
    :type filter: str
    :param label_name: An exact label name to search by
    :type label_name: str
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def find_keywords(request: web.Request, keywords=None) -> web.Response:
    """Find keywords

    Searches for all keywords available for purchase on the CallFire platform. If a keyword appears in the response, it is available for purchase. List the &#39;keywords&#39; in a query parameter to search for multiple keywords (at least one keyword should be sent in request). Keyword should only consist of uppercase and lowercase letters and numbers. Number of characters must be greater than 2, but less than 65.

    :param keywords: A keyword to search for
    :type keywords: List[str]

    """
    return web.Response(status=200)


async def get_keyword_lease(request: web.Request, keyword, fields=None) -> web.Response:
    """Find a specific lease

    Searches for all keywords owned by user

    :param keyword: Keyword text that a lease is desired for
    :type keyword: str
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def get_keyword_lease_by_id(request: web.Request, id, fields=None) -> web.Response:
    """Find a keyword by id

    Get keyword by id

    :param id: ~
    :type id: int
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def get_keyword_lease_config(request: web.Request, keyword, fields=None) -> web.Response:
    """Find a specific keyword lease config

    Returns a single KeywordConfig instance for a given keyword lease

    :param keyword: A Keyword to get KeywordConfig by
    :type keyword: str
    :param fields: Limit fields received in response. E.g. fields: id, name or fields items (id, name), see more at [partial response](https://developers.callfire.com/docs.html#partial-response) page.
    :type fields: str

    """
    return web.Response(status=200)


async def is_keyword_available(request: web.Request, keyword) -> web.Response:
    """Check for a specific keyword

    Searches for the specific keyword to purchase on the CallFire platform. Returns &#39;true&#39; if keyword is available. Keyword should only consist of uppercase and lowercase letters and numbers. Number of characters must be greater than 2, but less than 65.

    :param keyword: To specify a keyword to search for. Example: SUN, MOON
    :type keyword: str

    """
    return web.Response(status=200)


async def update_keyword_lease(request: web.Request, keyword, body=None) -> web.Response:
    """Update a lease

    Updates a keyword lease. Turns the autoRenew on/off. Configure double opt in feature. Add/remove contact list from keyword.

    :param keyword: To update a keyword lease
    :type keyword: str
    :param body: A keyword lease object
    :type body: dict | bytes

    """
    body = KeywordLease.from_dict(body)
    return web.Response(status=200)


async def update_keyword_lease_config(request: web.Request, keyword, body=None) -> web.Response:
    """Update a keyword lease config

    Updates a keyword lease configuration. Use this API endpoint to enable/disable inbound SMS forwarding, set forward number. Forward number must be in E.164 format)

    :param keyword: To update a keyword lease config
    :type keyword: str
    :param body: The configuration of a keyword lease object.
    :type body: dict | bytes

    """
    body = KeywordConfig.from_dict(body)
    return web.Response(status=200)
