from typing import List, Dict
from aiohttp import web

from openapi_server.models.verify_check200_response import VerifyCheck200Response
from openapi_server.models.verify_control200_response import VerifyControl200Response
from openapi_server.models.verify_request_with_psd2200_response import VerifyRequestWithPSD2200Response
from openapi_server.models.verify_search200_response import VerifySearch200Response
from openapi_server import util


async def verify_check(request: web.Request, format, api_key, api_secret, code, request_id, ip_address=None) -> web.Response:
    """Verify Check

    Use Verify check to confirm that the PIN you received from your user matches the one sent by Vonage in your Verify request.  1. Send the verification &#x60;code&#x60; that your user supplied, with the corresponding &#x60;request_id&#x60; from the Verify request. 2. Check the &#x60;status&#x60; of the response to determine if the code the user supplied matches the one sent by Vonage.  *Note that this endpoint is available by &#x60;GET&#x60; request as well as &#x60;POST&#x60;.*

    :param format: The response format.
    :type format: str
    :param api_key: You can find your API key in your [account dashboard](https://dashboard.nexmo.com)
    :type api_key: str
    :param api_secret: You can find your API secret in your [account dashboard](https://dashboard.nexmo.com)
    :type api_secret: str
    :param code: The verification code entered by your user.
    :type code: str
    :param request_id: The Verify request to check. This is the &#x60;request_id&#x60; you received in the response to the Verify request.
    :type request_id: str
    :param ip_address: (This field is no longer used)
    :type ip_address: str

    """
    return web.Response(status=200)


async def verify_control(request: web.Request, format, api_key, api_secret, cmd, request_id) -> web.Response:
    """Verify Control

    Control the progress of your Verify requests. To cancel an existing Verify request, or to trigger the next verification event:   1. Send a Verify control request with the appropriate command (&#x60;cmd&#x60;) for what you want to achieve.  2. Check the &#x60;status&#x60; in the response.   *Note that this endpoint is available by &#x60;GET&#x60; request as well as &#x60;POST&#x60;.*

    :param format: The response format.
    :type format: str
    :param api_key: You can find your API key in your [account dashboard](https://dashboard.nexmo.com)
    :type api_key: str
    :param api_secret: You can find your API secret in your [account dashboard](https://dashboard.nexmo.com)
    :type api_secret: str
    :param cmd: The possible commands are &#x60;cancel&#x60; to request cancellation of the verification process, or &#x60;trigger_next_event&#x60; to advance  to the next verification event (if any). Cancellation is only possible 30 seconds after the start of the verification request and before the second event (either TTS or SMS) has taken place.
    :type cmd: str
    :param request_id: The &#x60;request_id&#x60; you received in the response to the Verify request.
    :type request_id: str

    """
    return web.Response(status=200)


async def verify_request_with_psd2(request: web.Request, format, amount, api_key, api_secret, number, payee, code_length=None, country=None, lg=None, next_event_wait=None, pin_expiry=None, workflow_id=None) -> web.Response:
    """PSD2 (Payment Services Directive 2) Request

    Use Verify request to generate and send a PIN to your user to authorize a payment: 1. Create a request to send a verification code to your user. 2. Check the &#x60;status&#x60; field in the response to ensure that your request was successful (zero is success). 3. Use the &#x60;request_id&#x60; field in the response for the Verify check. (Please note that XML format is not supported for the Payment Services Directive endpoint at this time.)

    :param format: The response format.
    :type format: str
    :param amount: The decimal amount of the payment to be confirmed, in Euros
    :type amount: float
    :param api_key: You can find your API key in your [account dashboard](https://dashboard.nexmo.com)
    :type api_key: str
    :param api_secret: You can find your API secret in your [account dashboard](https://dashboard.nexmo.com)
    :type api_secret: str
    :param number: The mobile or landline phone number to verify. Unless you are setting &#x60;country&#x60; explicitly, this number must be in [E.164](https://en.wikipedia.org/wiki/E.164) format.
    :type number: str
    :param payee: An alphanumeric string to indicate to the user the name of the recipient that they are confirming a payment to.
    :type payee: str
    :param code_length: The length of the verification code.
    :type code_length: int
    :param country: If you do not provide &#x60;number&#x60; in international format or you are not sure if &#x60;number&#x60; is correctly formatted, specify the two-character country code in &#x60;country&#x60;. Verify will then format the number for you.
    :type country: str
    :param lg: By default, the SMS or text-to-speech (TTS) message is generated in the locale that matches the &#x60;number&#x60;. For example, the text message or TTS message for a &#x60;33*&#x60; number is sent in French. Use this parameter to explicitly control the language used. *Note: Voice calls in English for &#x60;bg-bg&#x60;, &#x60;ee-et&#x60;, &#x60;ga-ie&#x60;, &#x60;lv-lv&#x60;, &#x60;lt-lt&#x60;, &#x60;mt-mt&#x60;, &#x60;sk-sk&#x60;, &#x60;sk-si&#x60;
    :type lg: str
    :param next_event_wait: Specifies the wait time in seconds between attempts to deliver the verification code.
    :type next_event_wait: int
    :param pin_expiry: How long the generated verification code is valid for, in seconds. When you specify both &#x60;pin_expiry&#x60; and &#x60;next_event_wait&#x60; then &#x60;pin_expiry&#x60; must be an integer multiple of &#x60;next_event_wait&#x60; otherwise &#x60;pin_expiry&#x60; is defaulted to equal next_event_wait. See [changing the event timings](https://developer.nexmo.com/verify/guides/changing-default-timings).
    :type pin_expiry: int
    :param workflow_id: Selects the predefined sequence of SMS and TTS (Text To Speech) actions to use in order to convey the PIN to your user. For example, an id of 1 identifies the workflow SMS - TTS - TTS. For a list of all workflows and their associated ids, please visit the [developer portal](https://developer.nexmo.com/verify/guides/workflows-and-events).
    :type workflow_id: int

    """
    return web.Response(status=200)


async def verify_search(request: web.Request, format, api_key, api_secret, request_id, request_ids=None) -> web.Response:
    """Verify Search

    Use Verify search to check the status of past or current verification requests:  1. Send a Verify search request containing the &#x60;request_id&#x60;s of the verification requests you are interested in. 2. Use the &#x60;status&#x60; of each verification request in the &#x60;checks&#x60; array of the response object to determine the outcome.  *Note that this endpoint is available by &#x60;POST&#x60; request as well as &#x60;GET&#x60;.*

    :param format: The response format.
    :type format: str
    :param api_key: 
    :type api_key: str
    :param api_secret: 
    :type api_secret: str
    :param request_id: The &#x60;request_id&#x60; you received in the Verify Request Response. Required if &#x60;request_ids&#x60; not provided.
    :type request_id: str
    :param request_ids: More than one &#x60;request_id&#x60;. Each &#x60;request_id&#x60; is a new parameter in the Verify Search request. Required if &#x60;request_id&#x60; not provided.
    :type request_ids: List[str]

    """
    return web.Response(status=200)
