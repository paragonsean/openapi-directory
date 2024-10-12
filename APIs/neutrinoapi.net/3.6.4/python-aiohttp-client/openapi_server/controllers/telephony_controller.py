from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.hlr_lookup_response import HLRLookupResponse
from openapi_server.models.phone_playback_response import PhonePlaybackResponse
from openapi_server.models.phone_verify_response import PhoneVerifyResponse
from openapi_server.models.sms_verify_response import SMSVerifyResponse
from openapi_server.models.verify_security_code_response import VerifySecurityCodeResponse
from openapi_server import util


async def h_lr_lookup(request: web.Request, number, country_code=None) -> web.Response:
    """HLR Lookup

    Connect to the global mobile cellular network and retrieve the status of a mobile device

    :param number: A phone number
    :type number: str
    :param country_code: ISO 2-letter country code, assume numbers are based in this country. &lt;br&gt;If not set numbers are assumed to be in international format (with or without the leading + sign)
    :type country_code: str

    """
    return web.Response(status=200)


async def phone_playback(request: web.Request, audio_url, number, limit=None, limit_ttl=None) -> web.Response:
    """Phone Playback

    Make an automated call to any valid phone number and playback an audio message

    :param audio_url: A URL to a valid audio file. Accepted audio formats are: &lt;ul&gt; &lt;li&gt;MP3&lt;/li&gt; &lt;li&gt;WAV&lt;/li&gt; &lt;li&gt;OGG&lt;/li&gt; &lt;/ul&gt;You can use the following MP3 URL for testing: &lt;br&gt;https://www.neutrinoapi.com/test-files/test1.mp3
    :type audio_url: str
    :param number: The phone number to call. Must be in valid international format
    :type number: str
    :param limit: Limit the total number of calls allowed to the supplied phone number, if the limit is reached within the TTL then error code 14 will be returned
    :type limit: int
    :param limit_ttl: Set the TTL in number of days that the &#39;limit&#39; option will remember a phone number (the default is 1 day and the maximum is 365 days)
    :type limit_ttl: int

    """
    return web.Response(status=200)


async def phone_verify(request: web.Request, number, code_length=None, country_code=None, language_code=None, limit=None, limit_ttl=None, playback_delay=None, security_code=None) -> web.Response:
    """Phone Verify

    Make an automated call to any valid phone number and playback a unique security code

    :param number: The phone number to send the verification code to
    :type number: str
    :param code_length: The number of digits to use in the security code (between 4 and 12)
    :type code_length: int
    :param country_code: ISO 2-letter country code, assume numbers are based in this country. &lt;br&gt;If not set numbers are assumed to be in international format (with or without the leading + sign)
    :type country_code: str
    :param language_code: The language to playback the verification code in, available languages are: &lt;ul&gt; &lt;li&gt;de - German&lt;/li&gt; &lt;li&gt;en - English&lt;/li&gt; &lt;li&gt;es - Spanish&lt;/li&gt; &lt;li&gt;fr - French&lt;/li&gt; &lt;li&gt;it - Italian&lt;/li&gt; &lt;li&gt;pt - Portuguese&lt;/li&gt; &lt;li&gt;ru - Russian&lt;/li&gt; &lt;/ul&gt;
    :type language_code: str
    :param limit: Limit the total number of calls allowed to the supplied phone number, if the limit is reached within the TTL then error code 14 will be returned
    :type limit: int
    :param limit_ttl: Set the TTL in number of days that the &#39;limit&#39; option will remember a phone number (the default is 1 day and the maximum is 365 days)
    :type limit_ttl: int
    :param playback_delay: The delay in milliseconds between the playback of each security code
    :type playback_delay: int
    :param security_code: Pass in your own security code. This is useful if you have implemented TOTP or similar 2FA methods. If not set then we will generate a secure random code
    :type security_code: int

    """
    return web.Response(status=200)


async def s_ms_verify(request: web.Request, number, code_length=None, country_code=None, language_code=None, limit=None, limit_ttl=None, security_code=None) -> web.Response:
    """SMS Verify

    Send a unique security code to any mobile device via SMS

    :param number: The phone number to send a verification code to
    :type number: str
    :param code_length: The number of digits to use in the security code (must be between 4 and 12)
    :type code_length: int
    :param country_code: ISO 2-letter country code, assume numbers are based in this country. &lt;br&gt;If not set numbers are assumed to be in international format (with or without the leading + sign)
    :type country_code: str
    :param language_code: The language to send the verification code in, available languages are: &lt;ul&gt; &lt;li&gt;de - German&lt;/li&gt; &lt;li&gt;en - English&lt;/li&gt; &lt;li&gt;es - Spanish&lt;/li&gt; &lt;li&gt;fr - French&lt;/li&gt; &lt;li&gt;it - Italian&lt;/li&gt; &lt;li&gt;pt - Portuguese&lt;/li&gt; &lt;li&gt;ru - Russian&lt;/li&gt; &lt;/ul&gt;
    :type language_code: str
    :param limit: Limit the total number of SMS allowed to the supplied phone number, if the limit is reached within the TTL then error code 14 will be returned
    :type limit: int
    :param limit_ttl: Set the TTL in number of days that the &#39;limit&#39; option will remember a phone number (the default is 1 day and the maximum is 365 days)
    :type limit_ttl: int
    :param security_code: Pass in your own security code. This is useful if you have implemented TOTP or similar 2FA methods. If not set then we will generate a secure random code
    :type security_code: int

    """
    return web.Response(status=200)


async def verify_security_code(request: web.Request, security_code, limit_by=None) -> web.Response:
    """Verify Security Code

    Check if a security code sent via SMS Verify or Phone Verify is valid

    :param security_code: The security code to verify
    :type security_code: str
    :param limit_by: If set then enable additional brute-force protection by limiting the number of attempts by the supplied value. This can be set to any unique identifier you would like to limit by, for example a hash of the users email, phone number or IP address. Requests to this API will be ignored after approximately 10 failed verification attempts
    :type limit_by: str

    """
    return web.Response(status=200)
