from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_short_code import ApiV2010AccountShortCode
from openapi_server.models.list_short_code_response import ListShortCodeResponse
from openapi_server import util


async def fetch_short_code(request: web.Request, account_sid, sid) -> web.Response:
    """fetch_short_code

    Fetch an instance of a short code

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource(s) to fetch.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the ShortCode resource to fetch
    :type sid: str

    """
    return web.Response(status=200)


async def list_short_code(request: web.Request, account_sid, friendly_name=None, short_code=None, page_size=None, page=None, page_token=None) -> web.Response:
    """list_short_code

    Retrieve a list of short-codes belonging to the account used to make the request

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource(s) to read.
    :type account_sid: str
    :param friendly_name: The string that identifies the ShortCode resources to read.
    :type friendly_name: str
    :param short_code: Only show the ShortCode resources that match this pattern. You can specify partial numbers and use &#39;*&#39; as a wildcard for any digit.
    :type short_code: str
    :param page_size: How many resources to return in each list page. The default is 50, and the maximum is 1000.
    :type page_size: int
    :param page: The page index. This value is simply for client state.
    :type page: int
    :param page_token: The page token. This is provided by the API.
    :type page_token: str

    """
    return web.Response(status=200)


async def update_short_code(request: web.Request, account_sid, sid, api_version=None, friendly_name=None, sms_fallback_method=None, sms_fallback_url=None, sms_method=None, sms_url=None) -> web.Response:
    """update_short_code

    Update a short code with the following parameters

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) that created the ShortCode resource(s) to update.
    :type account_sid: str
    :param sid: The Twilio-provided string that uniquely identifies the ShortCode resource to update
    :type sid: str
    :param api_version: The API version to use to start a new TwiML session. Can be: &#x60;2010-04-01&#x60; or &#x60;2008-08-01&#x60;.
    :type api_version: str
    :param friendly_name: A descriptive string that you created to describe this resource. It can be up to 64 characters long. By default, the &#x60;FriendlyName&#x60; is the short code.
    :type friendly_name: str
    :param sms_fallback_method: The HTTP method that we should use to call the &#x60;sms_fallback_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type sms_fallback_method: str
    :param sms_fallback_url: The URL that we should call if an error occurs while retrieving or executing the TwiML from &#x60;sms_url&#x60;.
    :type sms_fallback_url: str
    :param sms_method: The HTTP method we should use when calling the &#x60;sms_url&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;.
    :type sms_method: str
    :param sms_url: The URL we should call when receiving an incoming SMS message to this short code.
    :type sms_url: str

    """
    return web.Response(status=200)
