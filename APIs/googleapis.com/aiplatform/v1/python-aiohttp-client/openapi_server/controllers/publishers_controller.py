from typing import List, Dict
from aiohttp import web

from openapi_server.models.google_cloud_aiplatform_v1_publisher_model import GoogleCloudAiplatformV1PublisherModel
from openapi_server import util


async def aiplatform_publishers_models_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, language_code=None, view=None) -> web.Response:
    """aiplatform_publishers_models_get

    Gets a Model Garden publisher model.

    :param name: Required. The name of the PublisherModel resource. Format: &#x60;publishers/{publisher}/models/{publisher_model}&#x60;
    :type name: str
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
    :param language_code: Optional. The IETF BCP-47 language code representing the language in which the publisher model&#39;s text information should be written in (see go/bcp47).
    :type language_code: str
    :param view: Optional. PublisherModel view specifying which fields to read.
    :type view: str

    """
    return web.Response(status=200)
