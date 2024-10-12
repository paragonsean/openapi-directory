from typing import List, Dict
from aiohttp import web

from openapi_server.models.operation import Operation
from openapi_server import util


async def accesscontextmanager_operations_get(request: web.Request, name, xgafv=None, access_token=None, alt=None, param_callback=None, fields=None, key=None, oauth_token=None, pretty_print=None, quota_user=None, upload_protocol=None, upload_type=None, access_level_format=None) -> web.Response:
    """accesscontextmanager_operations_get

    Gets the latest state of a long-running operation. Clients can use this method to poll the operation result at intervals as recommended by the API service.

    :param name: The name of the operation resource.
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
    :param access_level_format: Whether to return &#x60;BasicLevels&#x60; in the Cloud Common Expression Language rather than as &#x60;BasicLevels&#x60;. Defaults to AS_DEFINED, where Access Levels are returned as &#x60;BasicLevels&#x60; or &#x60;CustomLevels&#x60; based on how they were created. If set to CEL, all Access Levels are returned as &#x60;CustomLevels&#x60;. In the CEL case, &#x60;BasicLevels&#x60; are translated to equivalent &#x60;CustomLevels&#x60;.
    :type access_level_format: str

    """
    return web.Response(status=200)
