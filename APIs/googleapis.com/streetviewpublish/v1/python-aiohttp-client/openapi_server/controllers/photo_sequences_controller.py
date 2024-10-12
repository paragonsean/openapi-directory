from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_photo_sequences_response import ListPhotoSequencesResponse
from openapi_server import util


async def streetviewpublish_photo_sequences_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, filter=None, page_size=None, page_token=None) -> web.Response:
    """streetviewpublish_photo_sequences_list

    Lists all the PhotoSequences that belong to the user, in descending CreatePhotoSequence timestamp order.

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
    :param filter: Optional. The filter expression. For example: &#x60;imagery_type&#x3D;SPHERICAL&#x60;. The filters supported are: &#x60;imagery_type&#x60;, &#x60;processing_state&#x60;, &#x60;min_latitude&#x60;, &#x60;max_latitude&#x60;, &#x60;min_longitude&#x60;, &#x60;max_longitude&#x60;, &#x60;filename_query&#x60;, &#x60;min_capture_time_seconds&#x60;, &#x60;max_capture_time_seconds. See https://google.aip.dev/160 for more information. Filename queries should sent as a Phrase in order to support multiple words and special characters by adding escaped quotes. Ex: filename_query&#x3D;\&quot;example of a phrase.mp4\&quot;
    :type filter: str
    :param page_size: Optional. The maximum number of photo sequences to return. &#x60;pageSize&#x60; must be non-negative. If &#x60;pageSize&#x60; is zero or is not provided, the default page size of 100 is used. The number of photo sequences returned in the response may be less than &#x60;pageSize&#x60; if the number of matches is less than &#x60;pageSize&#x60;. This is currently unimplemented but is in process.
    :type page_size: int
    :param page_token: Optional. The nextPageToken value returned from a previous ListPhotoSequences request, if any.
    :type page_token: str

    """
    return web.Response(status=200)
