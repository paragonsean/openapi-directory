from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_cloud_videointelligence_v1beta2_annotate_video_request import GoogleCloudVideointelligenceV1beta2AnnotateVideoRequest
from openapi_server.models.google_longrunning_operation import GoogleLongrunningOperation
from openapi_server import util


async def videointelligence_videos_annotate(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """videointelligence_videos_annotate

    Performs asynchronous video annotation. Progress and results can be retrieved through the &#x60;google.longrunning.Operations&#x60; interface. &#x60;Operation.metadata&#x60; contains &#x60;AnnotateVideoProgress&#x60; (progress). &#x60;Operation.response&#x60; contains &#x60;AnnotateVideoResponse&#x60; (results).

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
    :param body: 
    :type body: dict | bytes

    """
    body = GoogleCloudVideointelligenceV1beta2AnnotateVideoRequest.from_dict(body)
    return web.Response(status=200)
