from typing import List, Dict
from aiohttp import web

from openapi_server.models.generate_new_device_codes_request import GenerateNewDeviceCodesRequest
from openapi_server.models.poll_for_the_access_token_request import PollForTheAccessTokenRequest
from openapi_server import util


async def generate_new_device_codes(request: web.Request, body=None) -> web.Response:
    """Generate new device codes

    Generate new codes to start the device authentication process. The &#x60;device_code&#x60; and &#x60;interval&#x60; will be used later to poll for the &#x60;access_token&#x60;. The &#x60;user_code&#x60; and &#x60;verification_url&#x60; should be presented to the user as mentioned in the flow steps above.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;client_id&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | Get this from your app settings. |

    :param body: 
    :type body: dict | bytes

    """
    body = GenerateNewDeviceCodesRequest.from_dict(body)
    return web.Response(status=200)


async def poll_for_the_access_token(request: web.Request, body=None) -> web.Response:
    """Poll for the access_token

    Use the &#x60;device_code&#x60; and poll at the &#x60;interval&#x60; (in seconds) to check if the user has authorized you app. Use &#x60;expires_in&#x60; to stop polling after that many seconds, and gracefully instruct the user to restart the process. **It is important to poll at the correct interval and also stop polling when expired.**  When you receive a &#x60;200&#x60; success response, save the &#x60;access_token&#x60; so your app can authenticate the user in methods that require it. The &#x60;access_token&#x60; is valid for 3 months. Save and use the &#x60;refresh_token&#x60; to get a new &#x60;access_token&#x60; without asking the user to re-authenticate. Check below for all the error codes that you should handle.  #### JSON POST Data  | Key | Type | Value | |---|---|---| | &#x60;code&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | &#x60;device_code&#x60; from the initial method. | | &#x60;client_id&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | Get this from your app settings. | | &#x60;client_secret&#x60; &lt;span style&#x3D;\&quot;color:red;\&quot;&gt;*&lt;/a&gt; | string | Get this from your app settings. |  ####  Status Codes  This method will send various HTTP status codes that you should handle accordingly.  | Code | Description | |---|---| | &#x60;200&#x60; | Success - *save the &#x60;access_token&#x60;* | &#x60;400&#x60; | Pending - *waiting for the user to authorize your app* | &#x60;404&#x60; | Not Found - *invalid &#x60;device_code&#x60;* | &#x60;409&#x60; | Already Used - *user already approved this code* | &#x60;410&#x60; | Expired - *the tokens have expired, restart the process* | &#x60;418&#x60; | Denied - *user explicitly denied this code* | &#x60;429&#x60; | Slow Down - *your app is polling too quickly*

    :param body: 
    :type body: dict | bytes

    """
    body = PollForTheAccessTokenRequest.from_dict(body)
    return web.Response(status=200)
