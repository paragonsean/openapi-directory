from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_v2010_account_validation_request import ApiV2010AccountValidationRequest
from openapi_server import util


async def create_validation_request(request: web.Request, account_sid, phone_number, call_delay=None, extension=None, friendly_name=None, status_callback=None, status_callback_method=None) -> web.Response:
    """create_validation_request

    

    :param account_sid: The SID of the [Account](https://www.twilio.com/docs/iam/api/account) responsible for the new caller ID resource.
    :type account_sid: str
    :param phone_number: The phone number to verify in [E.164](https://www.twilio.com/docs/glossary/what-e164) format, which consists of a + followed by the country code and subscriber number.
    :type phone_number: str
    :param call_delay: The number of seconds to delay before initiating the verification call. Can be an integer between &#x60;0&#x60; and &#x60;60&#x60;, inclusive. The default is &#x60;0&#x60;.
    :type call_delay: int
    :param extension: The digits to dial after connecting the verification call.
    :type extension: str
    :param friendly_name: A descriptive string that you create to describe the new caller ID resource. It can be up to 64 characters long. The default value is a formatted version of the phone number.
    :type friendly_name: str
    :param status_callback: The URL we should call using the &#x60;status_callback_method&#x60; to send status information about the verification process to your application.
    :type status_callback: str
    :param status_callback_method: The HTTP method we should use to call &#x60;status_callback&#x60;. Can be: &#x60;GET&#x60; or &#x60;POST&#x60;, and the default is &#x60;POST&#x60;.
    :type status_callback_method: str

    """
    return web.Response(status=200)
