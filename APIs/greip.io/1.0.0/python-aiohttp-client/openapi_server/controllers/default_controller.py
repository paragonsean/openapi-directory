from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def a_sn_lookup_get(request: web.Request, key, asn, is_list=None, format=None) -> web.Response:
    """a_sn_lookup_get

    ASNLookup endpoint: This method helps you lookup any AS Number. It returns the type, organisation details, routes, etc.

    :param key: Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first.
    :type key: str
    :param asn: The AS Number you want to lookup
    :type asn: str
    :param is_list: Set this to true if you want to list all routes of both IPv4 and IPv6.
    :type is_list: str
    :param format: Sets the format of the API response. JSON is the default format.
    :type format: str

    """
    return web.Response(status=200)


async def b_in_lookup_get(request: web.Request, key, bin, format=None) -> web.Response:
    """b_in_lookup_get

    This method helps you validate any BIN/IIN number and retrieve the full details related to the bank, brand, type, scheme, country, etc.

    :param key: Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first.
    :type key: str
    :param bin: The BIN/IIN you want to lookup/validate.
    :type bin: str
    :param format: Sets the format of the API response. JSON is the default format.
    :type format: str

    """
    return web.Response(status=200)


async def bad_words_get(request: web.Request, key, text, list_bad_words=None, score_only=None, format=None) -> web.Response:
    """bad_words_get

    badWords endpoint: Detects whether user inputs contain profanity or not.

    :param key: Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first.
    :type key: str
    :param text: The text you want to check.
    :type text: str
    :param list_bad_words: Set to &#x60;yes&#x60; to list the bad-words as an Array.
    :type list_bad_words: str
    :param score_only: Set to &#x60;yes&#x60; to return only the score of the text and whether it&#39;s safe or not.
    :type score_only: str
    :param format: Sets the format of the API response. JSON is the default format.
    :type format: str

    """
    return web.Response(status=200)


async def bulk_lookup_get(request: web.Request, key, ips, params=None, lang=None, format=None) -> web.Response:
    """bulk_lookup_get

    BulkLookup endpoint: Returns the geolocation data of multiple IP Addresses.

    :param key: Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first.
    :type key: str
    :param ips: The IP Addresses you want to lookup. It&#39;s a CSV (Comma Separated Values)
    :type ips: str
    :param params: The modules you want to use of the request. It&#39;s a CSV (Comma Separated Values)
    :type params: str
    :param lang: Used to inform the API to retrieve the response in your native language.
    :type lang: str
    :param format: Sets the format of the API response. JSON is the default format.
    :type format: str

    """
    return web.Response(status=200)


async def country_get(request: web.Request, key, country_code, params=None, lang=None, format=None) -> web.Response:
    """country_get

    Country endpoint: Returns the information of a specific country by passing the &#x60;countrCode&#x60;.

    :param key: Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first.
    :type key: str
    :param country_code: The Country Code of the country you want to fetch it&#39;s data.
    :type country_code: str
    :param params: The modules you want to use of the request. It&#39;s a CSV (Comma Separated Values)
    :type params: str
    :param lang: Used to inform the API to retrieve the response in your native language.
    :type lang: str
    :param format: Sets the format of the API response. JSON is the default format.
    :type format: str

    """
    return web.Response(status=200)


async def geo_ipget(request: web.Request, key, params=None, lang=None, format=None) -> web.Response:
    """geo_ipget

    Returns the geolocation data of the visitor.

    :param key: Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first.
    :type key: str
    :param params: The modules you want to use of the request. It&#39;s a CSV (Comma Separated Values)
    :type params: str
    :param lang: Used to inform the API to retrieve the response in your native language.
    :type lang: str
    :param format: Sets the format of the API response. JSON is the default format.
    :type format: str

    """
    return web.Response(status=200)


async def i_p_lookup_get(request: web.Request, key, ip, params=None, lang=None, format=None) -> web.Response:
    """i_p_lookup_get

    Returns the geolocation data of a specific IP Address.

    :param key: Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first.
    :type key: str
    :param ip: The IP Address you want to lookup.
    :type ip: str
    :param params: The modules you want to use of the request. It&#39;s a CSV (Comma Separated Values)
    :type params: str
    :param lang: Used to inform the API to retrieve the response in your native language.
    :type lang: str
    :param format: Sets the format of the API response. JSON is the default format.
    :type format: str

    """
    return web.Response(status=200)


async def validate_email_get(request: web.Request, key, email, format=None) -> web.Response:
    """validate_email_get

    This method can be used as an extra-layer of your system for validating email addresses.

    :param key: Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first.
    :type key: str
    :param email: The Email Address you want to validate.
    :type email: str
    :param format: Sets the format of the API response. JSON is the default format.
    :type format: str

    """
    return web.Response(status=200)


async def validate_phone_get(request: web.Request, key, phone, country_code, format=None) -> web.Response:
    """validate_phone_get

    This method can be used as an extra-layer of your system for validating phone numbers.

    :param key: Your API Key. Each user has a unique API Key that can be used to access the API functions. If you don&#39;t have an account yet, please create new account first.
    :type key: str
    :param phone: The Phone Number you want to validate.
    :type phone: str
    :param country_code: The ISO 3166-1 alpha-2 format of the country code of the phone number.
    :type country_code: str
    :param format: Sets the format of the API response. JSON is the default format.
    :type format: str

    """
    return web.Response(status=200)
