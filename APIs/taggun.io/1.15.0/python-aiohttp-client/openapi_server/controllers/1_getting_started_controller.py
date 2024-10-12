from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_error import BadRequestError
from openapi_server.models.receipt_result import ReceiptResult
from openapi_server.models.receipt_verbose_result import ReceiptVerboseResult
from openapi_server import util


async def post_api_receipt_v1_simple_file(request: web.Request, apikey, file=None, refresh=None, incognito=None, ip_address=None, near=None, ignore_merchant_name=None, language=None, extract_time=None, sub_account_id=None, reference_id=None) -> web.Response:
    """transcribe a receipt by uploading an image file

    

    :param apikey: API authentication key.
    :type apikey: str
    :param file: file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF, HEIC
    :type file: str
    :param refresh: Set true to force re-process image transcription if the receipt is already in storage
    :type refresh: bool
    :param incognito: Set true to avoid saving the receipt in storage
    :type incognito: bool
    :param ip_address: IP Address of the end user
    :type ip_address: str
    :param near: A geo location to search for merchant. Typically in the format of city, state, country.
    :type near: str
    :param ignore_merchant_name: Ignore this merchant name if detected on the receipt. Use this field to avoid detecting the customer name as the merchant name.
    :type ignore_merchant_name: str
    :param language: Set language as a hint. Leave empty for auto detect. Supported languages: , en, es, fr, jp, he, iw, et, lv, lt, fi, el, zh 
    :type language: str
    :param extract_time: Set true to return time if found on the receipt. Otherwise, the time is always set to 12:00:00.000.
    :type extract_time: bool
    :param sub_account_id: Tag a request with sub-account ID for billing purposes
    :type sub_account_id: str
    :param reference_id: Tag a request with a unique reference ID for feedback and training purposes
    :type reference_id: str

    """
    return web.Response(status=200)


async def post_api_receipt_v1_verbose_file(request: web.Request, apikey, file=None, refresh=None, incognito=None, ip_address=None, near=None, ignore_merchant_name=None, language=None, extract_time=None, sub_account_id=None, reference_id=None) -> web.Response:
    """transcribe a receipt by uploading an image file and return detailed result

    

    :param apikey: API authentication key.
    :type apikey: str
    :param file: file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF, HEIC
    :type file: str
    :param refresh: Set true to force re-process image transcription if the receipt is already in storage
    :type refresh: bool
    :param incognito: Set true to avoid saving the receipt in storage
    :type incognito: bool
    :param ip_address: IP Address of the end user
    :type ip_address: str
    :param near: A geo location to search for merchant. Typically in the format of city, state, country.
    :type near: str
    :param ignore_merchant_name: Ignore this merchant name if detected on the receipt. Use this field to avoid detecting the customer name as the merchant name.
    :type ignore_merchant_name: str
    :param language: Set language as a hint. Leave empty for auto detect. Supported languages: , en, es, fr, jp, he, iw, et, lv, lt, fi, el, zh 
    :type language: str
    :param extract_time: Set true to return time if found on the receipt. Otherwise, the time is always set to 12:00:00.000.
    :type extract_time: bool
    :param sub_account_id: Tag a request with sub-account ID for billing purposes
    :type sub_account_id: str
    :param reference_id: Tag a request with a unique reference ID for feedback and training purposes
    :type reference_id: str

    """
    return web.Response(status=200)
