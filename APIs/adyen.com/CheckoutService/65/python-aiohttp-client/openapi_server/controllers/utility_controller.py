from typing import List, Dict
from aiohttp import web

from openapi_server.models.apple_pay_session_request import ApplePaySessionRequest
from openapi_server.models.apple_pay_session_response import ApplePaySessionResponse
from openapi_server.models.service_error import ServiceError
from openapi_server.models.utility_request import UtilityRequest
from openapi_server.models.utility_response import UtilityResponse
from openapi_server import util


async def post_apple_pay_sessions(request: web.Request, idempotency_key=None, body=None) -> web.Response:
    """Get an Apple Pay session

    You need to use this endpoint if you have an API-only integration with Apple Pay which uses Adyen&#39;s Apple Pay certificate.  The endpoint returns the Apple Pay session data which you need to complete the [Apple Pay session validation](https://docs.adyen.com/payment-methods/apple-pay/api-only?tab&#x3D;adyen-certificate-validation_1#complete-apple-pay-session-validation).

    :param idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    :type idempotency_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = ApplePaySessionRequest.from_dict(body)
    return web.Response(status=200)


async def post_origin_keys(request: web.Request, idempotency_key=None, body=None) -> web.Response:
    """Create originKey values for domains

    This operation takes the origin domains and returns a JSON object containing the corresponding origin keys for the domains.  &gt; If you&#39;re still using origin key for your Web Drop-in or Components integration, we recommend [switching to client key](https://docs.adyen.com/development-resources/client-side-authentication/migrate-from-origin-key-to-client-key). This allows you to use a single key for all origins, add or remove origins without generating a new key, and detect the card type from the number entered in your payment form. 

    :param idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
    :type idempotency_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = UtilityRequest.from_dict(body)
    return web.Response(status=200)
