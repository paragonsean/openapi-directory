from typing import List, Dict
from aiohttp import web

from openapi_server.models.errors_response import ErrorsResponse
from openapi_server.models.token_resend_activation_code_request_schema import TokenResendActivationCodeRequestSchema
from openapi_server.models.token_resend_activation_code_response_schema import TokenResendActivationCodeResponseSchema
from openapi_server import util


async def token_resendactivationcode_post(request: web.Request, token_resend_activation_code_request_schema=None) -> web.Response:
    """token_resendactivationcode_post

    Used to trigger the process of generating and sending a new Activation Code (for a specific token) to the cardholder via the requested Activation Method. When successful, a new Activation Code Expiration Date Time period will begin, and a new Activation Code will be sent to the issuer using the Activation Code Notification (ACN) pre-digitization network message. It can only be used to do this for Activation Methods that involve the external distribution of an Activation Code to the cardholder. For example, via email or SMS. It cannot be used to send a new activation code via the \&quot;Mobile Application\&quot; activation method, for instance. A new Activation Code can be sent even if the previous code has not expired. A new Activation Code can also be sent even after the previous code has expired; however, it can only be done up to 30 days after the token was created  (the number of days is subject to change at the discretion of Mastercard). 

    :param token_resend_activation_code_request_schema: Contains the details of the request message.
    :type token_resend_activation_code_request_schema: dict | bytes

    """
    token_resend_activation_code_request_schema = TokenResendActivationCodeRequestSchema.from_dict(token_resend_activation_code_request_schema)
    return web.Response(status=200)
