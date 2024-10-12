from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def v1_verification_result_get(request: web.Request, tran_id, key, otp, format=None) -> web.Response:
    """v1_verification_result_get

    Verify that an OTP sent by the Send SMS Verification API is valid.

    :param tran_id: The unique ID that was returned by the Send Verification SMS API that triggered the OTP sms.
    :type tran_id: str
    :param key: FraudLabs Pro API key.
    :type key: str
    :param otp: The OTP that was sent to the recipient’s phone.
    :type otp: str
    :param format: Returns the API response in json (default) or xml format.
    :type format: str

    """
    return web.Response(status=200)


async def v1_verification_send_post(request: web.Request, tel, key, country_code=None, format=None, mesg=None) -> web.Response:
    """v1_verification_send_post

    Send an SMS with verification code and a custom message for authentication purpose.

    :param tel: The recipient mobile phone number in E164 format which is a plus followed by just numbers with no spaces or parentheses.
    :type tel: str
    :param key: FraudLabs Pro API key.
    :type key: str
    :param country_code: ISO 3166 country code for the recipient mobile phone number. If parameter is supplied, then some basic telephone number validation is done.
    :type country_code: str
    :param format: Returns the API response in json (default) or xml format.
    :type format: str
    :param mesg: The message template for the SMS. Add &lt;otp&gt; as placeholder for the actual OTP to be generated. Max length is 140 characters.
    :type mesg: str

    """
    return web.Response(status=200)
