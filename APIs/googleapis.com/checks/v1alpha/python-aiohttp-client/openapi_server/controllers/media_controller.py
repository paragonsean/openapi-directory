from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_checks_report_v1alpha_analyze_upload_request import GoogleChecksReportV1alphaAnalyzeUploadRequest
from openapi_server.models.operation import Operation
from openapi_server import util


async def checks_media_upload(request: web.Request, parent, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, body=None) -> web.Response:
    """checks_media_upload

    Analyzes the uploaded app bundle and returns a google.longrunning.Operation containing the generated Report. ## Example (upload only) Send a regular POST request with the header &#x60;X-Goog-Upload-Protocol: raw&#x60;. &#x60;&#x60;&#x60; POST https://checks.googleapis.com/upload/v1alpha/{parent&#x3D;accounts/*/apps/*}/reports:analyzeUpload HTTP/1.1 X-Goog-Upload-Protocol: raw Content-Length: Content-Type: application/octet-stream &#x60;&#x60;&#x60; ## Example (upload with metadata) Send a multipart POST request where the first body part contains the metadata JSON and the second body part contains the binary upload. Include the header &#x60;X-Goog-Upload-Protocol: multipart&#x60;. &#x60;&#x60;&#x60; POST https://checks.googleapis.com/upload/v1alpha/{parent&#x3D;accounts/*/apps/*}/reports:analyzeUpload HTTP/1.1 X-Goog-Upload-Protocol: multipart Content-Length: ? Content-Type: multipart/related; boundary&#x3D;BOUNDARY --BOUNDARY Content-Type: application/json {\&quot;code_reference_id\&quot;:\&quot;db5bcc20f94055fb5bc08cbb9b0e7a5530308786\&quot;} --BOUNDARY --BOUNDARY-- &#x60;&#x60;&#x60; *Note:* Metadata-only requests are not supported. 

    :param parent: Required. Resource name of the app. Example: &#x60;accounts/123/apps/456&#x60;
    :type parent: str
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
    body = GoogleChecksReportV1alphaAnalyzeUploadRequest.from_dict(body)
    return web.Response(status=200)
