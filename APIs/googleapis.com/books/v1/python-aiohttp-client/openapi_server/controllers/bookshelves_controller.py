from typing import List, Dict
from aiohttp import web

from openapi_server.models.bookshelf import Bookshelf
from openapi_server.models.bookshelves import Bookshelves
from openapi_server.models.volumes import Volumes
from openapi_server import util


async def books_bookshelves_get(request: web.Request, user_id, shelf, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, source=None) -> web.Response:
    """books_bookshelves_get

    Retrieves metadata for a specific bookshelf for the specified user.

    :param user_id: ID of user for whom to retrieve bookshelves.
    :type user_id: str
    :param shelf: ID of bookshelf to retrieve.
    :type shelf: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param source: String to identify the originator of this request.
    :type source: str

    """
    return web.Response(status=200)


async def books_bookshelves_list(request: web.Request, user_id, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, source=None) -> web.Response:
    """books_bookshelves_list

    Retrieves a list of public bookshelves for the specified user.

    :param user_id: ID of user for whom to retrieve bookshelves.
    :type user_id: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param source: String to identify the originator of this request.
    :type source: str

    """
    return web.Response(status=200)


async def books_bookshelves_volumes_list(request: web.Request, user_id, shelf, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, max_results=None, show_preorders=None, source=None, start_index=None) -> web.Response:
    """books_bookshelves_volumes_list

    Retrieves volumes in a specific bookshelf for the specified user.

    :param user_id: ID of user for whom to retrieve bookshelf volumes.
    :type user_id: str
    :param shelf: ID of bookshelf to retrieve volumes.
    :type shelf: str
    :param xgafv: V1 error format.
    :type xgafv: str
    :param access_token: OAuth access token.
    :type access_token: str
    :param alt: Data format for response.
    :type alt: str
    :param param_callback: JSONP
    :type param_callback: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: Available to use for quota purposes for server-side applications. Can be any arbitrary string assigned to a user, but should not exceed 40 characters.
    :type quota_user: str
    :param upload_protocol: Upload protocol for media (e.g. \&quot;raw\&quot;, \&quot;multipart\&quot;).
    :type upload_protocol: str
    :param upload_type: Legacy upload protocol for media (e.g. \&quot;media\&quot;, \&quot;multipart\&quot;).
    :type upload_type: str
    :param max_results: Maximum number of results to return
    :type max_results: int
    :param show_preorders: Set to true to show pre-ordered books. Defaults to false.
    :type show_preorders: bool
    :param source: String to identify the originator of this request.
    :type source: str
    :param start_index: Index of the first element to return (starts at 0)
    :type start_index: int

    """
    return web.Response(status=200)
