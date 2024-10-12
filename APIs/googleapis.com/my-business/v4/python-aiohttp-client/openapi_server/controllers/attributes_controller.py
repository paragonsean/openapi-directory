from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_attribute_metadata_response import ListAttributeMetadataResponse
from openapi_server import util


async def mybusiness_attributes_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, category_id=None, country=None, language_code=None, name=None, page_size=None, page_token=None) -> web.Response:
    """mybusiness_attributes_list

    Returns the list of available attributes that would be available for a location with the given primary category and country.

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
    :param category_id: The primary category stable ID to find available attributes.
    :type category_id: str
    :param country: The ISO 3166-1 alpha-2 country code to find available attributes.
    :type country: str
    :param language_code: The BCP 47 code of language to get attribute display names in. If this language is not available, they will be provided in English.
    :type language_code: str
    :param name: Resource name of the location to look up available attributes.
    :type name: str
    :param page_size: How many attributes to include per page. Default is 200, minimum is 1.
    :type page_size: int
    :param page_token: If specified, the next page of attribute metadata is retrieved. The &#x60;pageToken&#x60; is returned when a call to &#x60;attributes.list&#x60; returns more results than can fit into the requested page size.
    :type page_token: str

    """
    return web.Response(status=200)
