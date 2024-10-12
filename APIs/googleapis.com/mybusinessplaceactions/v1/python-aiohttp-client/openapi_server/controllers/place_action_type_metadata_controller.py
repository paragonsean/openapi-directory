from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_place_action_type_metadata_response import ListPlaceActionTypeMetadataResponse
from openapi_server import util


async def mybusinessplaceactions_place_action_type_metadata_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, language_code=None, page_size=None, page_token=None) -> web.Response:
    """mybusinessplaceactions_place_action_type_metadata_list

    Returns the list of available place action types for a location or country.

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
    :param filter: Optional. A filter constraining the place action types to return metadata for. The response includes entries that match the filter. We support only the following filters: 1. location&#x3D;XYZ where XYZ is a string indicating the resource name of a location, in the format &#x60;locations/{location_id}&#x60;. 2. region_code&#x3D;XYZ where XYZ is a Unicode CLDR region code to find available action types. If no filter is provided, all place action types are returned.
    :type filter: str
    :param language_code: Optional. The IETF BCP-47 code of language to get display names in. If this language is not available, they will be provided in English.
    :type language_code: str
    :param page_size: Optional. How many action types to include per page. Default is 10, minimum is 1.
    :type page_size: int
    :param page_token: Optional. If specified, the next page of place action type metadata is retrieved. The &#x60;pageToken&#x60; is returned when a call to &#x60;placeActionTypeMetadata.list&#x60; returns more results than can fit into the requested page size.
    :type page_token: str

    """
    return web.Response(status=200)
