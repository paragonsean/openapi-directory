from typing import List, Dict
from aiohttp import web

from openapi_server.models.api_error import APIError
from openapi_server.models.bad_word_filter_response import BadWordFilterResponse
from openapi_server.models.email_validate_response import EmailValidateResponse
from openapi_server.models.phone_validate_response import PhoneValidateResponse
from openapi_server.models.ua_lookup_response import UALookupResponse
from openapi_server import util


async def bad_word_filter(request: web.Request, content, catalog=None, censor_character=None) -> web.Response:
    """Bad Word Filter

    Detect bad words, swear words and profanity in a given text

    :param content: The content to scan. This can be either a URL to load from, a file upload (multipart/form-data) or an HTML content string
    :type content: str
    :param catalog: Which catalog of bad words to use, we currently maintain two bad word catalogs: &lt;br&gt; &lt;ul&gt; &lt;li&gt;strict - the largest database of bad words which includes profanity, obscenity, sexual, rude, cuss, dirty, swear and objectionable words and phrases. This catalog is suitable for environments of all ages including educational or children&#39;s content&lt;/li&gt; &lt;li&gt;obscene - like the strict catalog but does not include any mild profanities, idiomatic phrases or words which are considered formal terminology. This catalog is suitable for adult environments where certain types of bad words are considered OK&lt;/li&gt; &lt;/ul&gt;
    :type catalog: str
    :param censor_character: The character to use to censor out the bad words found
    :type censor_character: str

    """
    return web.Response(status=200)


async def email_validate(request: web.Request, email, fix_typos=None) -> web.Response:
    """Email Validate

    Parse, validate and clean an email address

    :param email: An email address
    :type email: str
    :param fix_typos: Automatically attempt to fix typos in the address
    :type fix_typos: bool

    """
    return web.Response(status=200)


async def phone_validate(request: web.Request, number, country_code=None, ip=None) -> web.Response:
    """Phone Validate

    Parse, validate and get location information about a phone number

    :param number: A phone number. This can be in international format (E.164) or local format. If passing local format you must also set either the &#39;country-code&#39; OR &#39;ip&#39; options as well
    :type number: str
    :param country_code: ISO 2-letter country code, assume numbers are based in this country. If not set numbers are assumed to be in international format (with or without the leading + sign)
    :type country_code: str
    :param ip: Pass in a users IP address and we will assume numbers are based in the country of the IP address
    :type ip: str

    """
    return web.Response(status=200)


async def u_a_lookup(request: web.Request, ua, ua_version=None, ua_platform=None, ua_platform_version=None, ua_mobile=None, device_model=None, device_brand=None) -> web.Response:
    """UA Lookup

    Parse, validate and get detailed user-agent information from a user agent string or from client hints

    :param ua: The user-agent string to lookup. For client hints use the &#39;UA&#39; header or the JSON data directly from &#39;navigator.userAgentData.brands&#39; or &#39;navigator.userAgentData.getHighEntropyValues()&#39;
    :type ua: str
    :param ua_version: For client hints this corresponds to the &#39;UA-Full-Version&#39; header or &#39;uaFullVersion&#39; from NavigatorUAData
    :type ua_version: str
    :param ua_platform: For client hints this corresponds to the &#39;UA-Platform&#39; header or &#39;platform&#39; from NavigatorUAData
    :type ua_platform: str
    :param ua_platform_version: For client hints this corresponds to the &#39;UA-Platform-Version&#39; header or &#39;platformVersion&#39; from NavigatorUAData
    :type ua_platform_version: str
    :param ua_mobile: For client hints this corresponds to the &#39;UA-Mobile&#39; header or &#39;mobile&#39; from NavigatorUAData
    :type ua_mobile: str
    :param device_model: For client hints this corresponds to the &#39;UA-Model&#39; header or &#39;model&#39; from NavigatorUAData. &lt;br&gt;You can also use this parameter to lookup a device directly by its model name, model code or hardware code, on android you can get the model name from: https://developer.android.com/reference/android/os/Build.html#MODEL
    :type device_model: str
    :param device_brand: This parameter is only used in combination with &#39;device-model&#39; when doing direct device lookups without any user-agent data. Set this to the brand or manufacturer name, this is required for accurate device detection with ambiguous model names. On android you can get the device brand from: https://developer.android.com/reference/android/os/Build#MANUFACTURER
    :type device_brand: str

    """
    return web.Response(status=200)
