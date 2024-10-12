from typing import List, Dict
from aiohttp import web

from openapi_server.models.list_voices_response import ListVoicesResponse
from openapi_server import util


async def texttospeech_voices_list(request: web.Request, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, language_code=None) -> web.Response:
    """texttospeech_voices_list

    Returns a list of Voice supported for synthesis.

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
    :param language_code: Optional. Recommended. [BCP-47](https://www.rfc-editor.org/rfc/bcp/bcp47.txt) language tag. If not specified, the API will return all supported voices. If specified, the ListVoices call will only return voices that can be used to synthesize this language_code. For example, if you specify &#x60;\&quot;en-NZ\&quot;&#x60;, all &#x60;\&quot;en-NZ\&quot;&#x60; voices will be returned. If you specify &#x60;\&quot;no\&quot;&#x60;, both &#x60;\&quot;no-\\*\&quot;&#x60; (Norwegian) and &#x60;\&quot;nb-\\*\&quot;&#x60; (Norwegian Bokmal) voices will be returned.
    :type language_code: str

    """
    return web.Response(status=200)
