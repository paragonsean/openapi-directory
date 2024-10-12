from typing import List, Dict
from aiohttp import web

from openapi_server.models.directory_list import DirectoryList
from openapi_server.models.rest_description import RestDescription
from openapi_server import util


async def discovery_apis_get_rest(request: web.Request, api, version, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None) -> web.Response:
    """discovery_apis_get_rest

    Retrieve the description of a particular version of an api.

    :param api: The name of the API.
    :type api: str
    :param version: The version of the API.
    :type version: str
    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str

    """
    return web.Response(status=200)


async def discovery_apis_list(request: web.Request, alt=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, user_ip=None, name=None, preferred=None) -> web.Response:
    """discovery_apis_list

    Retrieve the list of APIs supported at this endpoint.

    :param alt: Data format for the response.
    :type alt: str
    :param fields: Selector specifying which fields to include in a partial response.
    :type fields: str
    :param key: API key. Your API key identifies your project and provides you with API access, quota, and reports. Required unless you provide an OAuth 2.0 token.
    :type key: str
    :param oauth_token: OAuth 2.0 token for the current user.
    :type oauth_token: str
    :param pretty_print: Returns response with indentations and line breaks.
    :type pretty_print: bool
    :param quota_user: An opaque string that represents a user for quota purposes. Must not exceed 40 characters.
    :type quota_user: str
    :param user_ip: Deprecated. Please use quotaUser instead.
    :type user_ip: str
    :param name: Only include APIs with the given name.
    :type name: str
    :param preferred: Return only the preferred version of an API.
    :type preferred: bool

    """
    return web.Response(status=200)
