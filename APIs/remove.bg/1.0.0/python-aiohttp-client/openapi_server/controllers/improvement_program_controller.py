from typing import List, Dict
from aiohttp import web

from openapi_server.models.auth_failed import AuthFailed
from openapi_server.models.improve_post400_response import ImprovePost400Response
from openapi_server.models.improvement_program_json import ImprovementProgramJson
from openapi_server.models.improvement_program_json_response import ImprovementProgramJsonResponse
from openapi_server.models.improvement_program_multipart import ImprovementProgramMultipart
from openapi_server.models.rate_limit import RateLimit
from openapi_server import util


async def improve_post(request: web.Request, body) -> web.Response:
    """improve_post

    Submit an image to the remove.bg Improvement program * Contribute an image that remove.bg is currently not able to remove the background from properly * Help us make remove.bg better * Get better results for similiar images in the future  Notes:   * By submitting images through the API you agree to the &lt;a target&#x3D;\&quot;_blank\&quot; rel&#x3D;\&quot;noopener\&quot; href&#x3D;\&quot;/ipc\&quot;&gt;Improvement Program Conditions&lt;/a&gt;   * File size: up to 12MB   * up to 100 files per day. &lt;br&gt; Higher Rate Limits are available for Enterprise customers &lt;a href&#x3D;\&quot;/support/contact?subject&#x3D;Improvement+Program+Rate+Limit\&quot;&gt;upon request&lt;/a&gt;.  Requires either an API Key to be provided in the &#x60;X-API-Key&#x60; request header or an OAuth 2.0 access token to be provided in the &#x60;Authorization&#x60; request header.  Please note that submissions are used on a best-effort basis and the extent of expected improvement varies depending on many factors, including the number of provided images, their complexity and visual similarity. Improvements usually take several weeks to become effective. 

    :param body: 
    :type body: dict | bytes

    """
    body = ImprovementProgramJson.from_dict(body)
    return web.Response(status=200)
