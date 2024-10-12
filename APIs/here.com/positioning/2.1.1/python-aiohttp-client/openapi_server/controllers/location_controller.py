from typing import List, Dict
from aiohttp import web

from openapi_server.models.auth_error import AuthError
from openapi_server.models.error import Error
from openapi_server.models.locate import Locate
from openapi_server.models.post_locate200_response import PostLocate200Response
from openapi_server import util


async def post_locate(request: web.Request, body, confidence=None, content_encoding=None, fallback=None, desired=None, x_request_id=None, required=None) -> web.Response:
    """Location query

    Request WGS-84 compliant geocoordinates for a location based on 2G/3G/4G cell and/or WLAN measurements.

    :param body: Request body containing cell and/or WLAN measurement data. Cellular measurements are given in terms defined in 3GPP and 3GGP2 specifications, see the corresponsing documentation at http://www.3gpp.org. 
    :type body: dict | bytes
    :param confidence: Confidence level in percent for the accuracy/uncertainty in the location estimate response. If not specified, the default is 68 (this corresponds to a 68% probability that the true position is within the accuracy/uncertainty radius of the location estimate: the higher the number, the greater the confidence level). 
    :type confidence: int
    :param content_encoding: Indicates that the data in the body is gzip-encoded.
    :type content_encoding: str
    :param fallback: Acceptable fallback options for cell and WLAN positioning. Values &#x60;area&#x60; and &#x60;any&#x60; apply to cell based positioning, and value &#x60;singleWifi&#x60; applies to WLAN based positioning. Both cell and WLAN options may be specified in the same request. If both &#x60;area&#x60; and &#x60;any&#x60; are specified, then &#x60;area&#x60; is ignored.  By default, cell based positioning returns cell tower level location estimates only. If you allow a WGS-84 compliant geocoordinate location estimate based on LAC, RNC, TAC, NID, or RZ areas, use the &#x60;fallback&#x3D;area&#x60; setting. If you use the &#x60;fallback&#x3D;any&#x60; setting, the service uses all available cell fallback methods and therefore the location estimate in the response may be at the MNC, SID, or MCC level.  For privacy reasons, the precise positioning based on a single WLAN AP is not possible. You can use the &#x60;fallback&#x3D;singleWifi&#x60; setting to allow less accurate positioning based on a single WLAN AP. In that case, the center location of the position estimate will be deviated and the reported accuracy radius will be larger. 
    :type fallback: List[str]
    :param desired: Comma-separated list of additional data fields that the service should include in the response if data is available. The query parameter supports the value &#x60;altitude&#x60;. 
    :type desired: List[str]
    :param x_request_id: ID used for correlating customer requests within HERE services. Used for logging and error reporting. Can be any string, but UUID is recommended. It will be echoed in the response. 
    :type x_request_id: str
    :param required: Comma-separated list of additional data fields that the service should include in the response. If the data is not available, the response contains an error message. The query parameter supports the value &#x60;altitude&#x60;. 
    :type required: List[str]

    """
    body = Locate.from_dict(body)
    return web.Response(status=200)
