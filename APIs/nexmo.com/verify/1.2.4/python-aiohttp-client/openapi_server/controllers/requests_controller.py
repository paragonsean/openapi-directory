from typing import List, Dict
from aiohttp import web

from openapi_server.models.verify_request_with_psd2200_response import VerifyRequestWithPSD2200Response
from openapi_server import util


async def verify_request(request: web.Request, format, api_key, api_secret, brand, number, code_length=None, country=None, lg=None, next_event_wait=None, pin_code=None, pin_expiry=None, sender_id=None, workflow_id=None) -> web.Response:
    """Request a Verification

    Use Verify request to generate and send a PIN to your user:  1. Create a request to send a verification code to your user.  2. Check the &#x60;status&#x60; field in the response to ensure that your request was successful (zero is success).  3. Use the &#x60;request_id&#x60; field in the response for the Verify check.  *Note that this endpoint is available by &#x60;GET&#x60; request as well as &#x60;POST&#x60;.*

    :param format: The response format.
    :type format: str
    :param api_key: You can find your API key in your [account dashboard](https://dashboard.nexmo.com)
    :type api_key: str
    :param api_secret: You can find your API secret in your [account dashboard](https://dashboard.nexmo.com)
    :type api_secret: str
    :param brand: An 18-character alphanumeric string you can use to personalize the verification request SMS body, to help users identify your company or application name. For example: \\\&quot;Your &#x60;Acme Inc&#x60; PIN is ...\\\&quot;
    :type brand: str
    :param number: The mobile or landline phone number to verify. Unless you are setting &#x60;country&#x60; explicitly, this number must be in [E.164](https://en.wikipedia.org/wiki/E.164) format.
    :type number: str
    :param code_length: The length of the verification code.
    :type code_length: int
    :param country: If you do not provide &#x60;number&#x60; in international format or you are not sure if &#x60;number&#x60; is correctly formatted, specify the two-character country code in &#x60;country&#x60;. Verify will then format the number for you.
    :type country: str
    :param lg: By default, the SMS or text-to-speech (TTS) message is generated in the locale that matches the &#x60;number&#x60;. For example, the text message or TTS message for a &#x60;33*&#x60; number is sent in French. Use this parameter to explicitly control the language used for the Verify request. A list of languages is available: &lt;https://developer.nexmo.com/verify/guides/verify-languages&gt;
    :type lg: str
    :param next_event_wait: Specifies the wait time in seconds between attempts to deliver the verification code.
    :type next_event_wait: int
    :param pin_code: A custom PIN to send to the user. If a PIN is not provided, Verify will generate a random PIN for you. &lt;b&gt;This feature is not enabled by default&lt;/b&gt; - please discuss with your Account Manager if you would like it enabled. If this feature is not enabled on your account, error status &#x60;20&#x60; will be returned.
    :type pin_code: str
    :param pin_expiry: How long the generated verification code is valid for, in seconds. When you specify both &#x60;pin_expiry&#x60; and &#x60;next_event_wait&#x60; then &#x60;pin_expiry&#x60; must be an integer multiple of &#x60;next_event_wait&#x60; otherwise &#x60;pin_expiry&#x60; is defaulted to equal next_event_wait. See [changing the event timings](https://developer.nexmo.com/verify/guides/changing-default-timings).
    :type pin_expiry: int
    :param sender_id: An 11-character alphanumeric string that represents the [identity of the sender](https://developer.nexmo.com/messaging/sms/guides/custom-sender-id) of the verification request. Depending on the destination of the phone number you are sending the verification SMS to, restrictions might apply.
    :type sender_id: str
    :param workflow_id: Selects the predefined sequence of SMS and TTS (Text To Speech) actions to use in order to convey the PIN to your user. For example, an id of 1 identifies the workflow SMS - TTS - TTS. For a list of all workflows and their associated ids, please visit the [developer portal](https://developer.nexmo.com/verify/guides/workflows-and-events).
    :type workflow_id: int

    """
    return web.Response(status=200)
