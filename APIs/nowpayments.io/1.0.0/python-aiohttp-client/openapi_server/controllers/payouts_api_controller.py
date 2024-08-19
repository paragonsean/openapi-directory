from typing import List, Dict
from aiohttp import web

from openapi_server.models.verify_payout_request import VerifyPayoutRequest
from openapi_server import util


async def verify_payout(request: web.Request, withdrawals_id, x_api_key=None, body=None) -> web.Response:
    """Verify payout

    This method is required to verify payouts by using your 2fa code.   You’ll have 10 attempts to verify the payout. If it is not verified after 10 attempts, the payout will remain in ‘creating’ status.   Payout will be processed only when it is verified.  Make sure to have your 2fa authentication enabled in your NOWPayments Account (in Account Settings).   When 2fa is disabled, the code automatically goes to your registration email.   The code sent by email is valid for one hour.  Next is a description of the required request fields:  - :batch-withdrawal-id - payout id you received in &#x60;2. Create payout&#x60; method - verification_code - 2fa code you received with your Google Auth app or via email       In order to establish an automatic verification of payouts, you should switch 2FA through the application.   There are several libraries for different frameworks aimed on generating a 2FA codes based on a secret key from your account settings.   e.g: Speakeasy for JavaScript.   We do not recommend to change any default settings.    &#x60;&#x60;&#x60; const 2faVerificationCode &#x3D; speakeasy.totp({       your_2fa_secret_key,       encoding: &#39;base32&#39;, }) &#x60;&#x60;&#x60;

    :param withdrawals_id: 
    :type withdrawals_id: str
    :param x_api_key: 
    :type x_api_key: str
    :param body: 
    :type body: dict | bytes

    """
    body = VerifyPayoutRequest.from_dict(body)
    return web.Response(status=200)
