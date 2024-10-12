from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_attribute_metadata_response import ListAttributeMetadataResponse
from openapi_server import util


async def mybusinessbusinessinformation_attributes_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, category_name=None, language_code=None, page_size=None, page_token=None, parent=None, region_code=None, show_all=None) -> web.Response:
    """mybusinessbusinessinformation_attributes_list

    Returns the list of attributes that would be available for a location with the given primary category and country.

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
    :param category_name: The primary category stable ID to find available attributes. Must be of the format categories/{category_id}.
    :type category_name: str
    :param language_code: The BCP 47 code of language to get attribute display names in. If this language is not available, they will be provided in English.
    :type language_code: str
    :param page_size: How many attributes to include per page. Default is 200, minimum is 1.
    :type page_size: int
    :param page_token: If specified, the next page of attribute metadata is retrieved.
    :type page_token: str
    :param parent: Resource name of the location to look up available attributes. If this field is set, category_name, region_code, language_code and show_all are not required and must not be set.
    :type parent: str
    :param region_code: The ISO 3166-1 alpha-2 country code to find available attributes.
    :type region_code: str
    :param show_all: Metadata for all available attributes are returned when this field is set to true, disregarding parent and category_name fields. language_code and region_code are required when show_all is set to true.
    :type show_all: bool

    """
    return web.Response(status=200)
