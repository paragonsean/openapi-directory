from typing import List, Dict
from aiohttp import web

from openapi_server.models.bad_request_error import BadRequestError
from openapi_server.models.receipt_match_result import ReceiptMatchResult
from openapi_server.models.receipt_result import ReceiptResult
from openapi_server.models.receipt_verbose_result import ReceiptVerboseResult
from openapi_server.models.storage_payload import StoragePayload
from openapi_server import util


async def post_api_receipt_v1_match_file(request: web.Request, apikey, file=None, refresh=None, incognito=None, ip_address=None, primary_keywords=None, secondary_keywords=None, stop_words=None, language=None) -> web.Response:
    """detect and match a receipt against keywords and metadata by uploading an image file

    

    :param apikey: API authentication key.
    :type apikey: str
    :param file: file less than 20MB. Accepted file types: PDF, JPG, PNG, GIF
    :type file: str
    :param refresh: Set true to force re-process image transcription if the receipt is already in storage
    :type refresh: bool
    :param incognito: Set true to avoid saving the receipt in storage
    :type incognito: bool
    :param ip_address: IP Address of the end user
    :type ip_address: str
    :param primary_keywords: An array of primary keywords to match
    :type primary_keywords: List[str]
    :param secondary_keywords: An array of secondary keywords to match (lower confidence level than primaryKeywords)
    :type secondary_keywords: List[str]
    :param stop_words: An array of stop words that negate the result to be UNLIKELY
    :type stop_words: List[str]
    :param language: Set language as a hint. Leave empty for auto detect. Supported languages: , en, es, fr, jp, he, iw, et, lv, lt, fi, el, zh 
    :type language: str

    """
    return web.Response(status=200)


async def post_api_receipt_v1_simple_storage(request: web.Request, apikey, body=None) -> web.Response:
    """transcribe a receipt in storage

    

    :param apikey: API authentication key.
    :type apikey: str
    :param body: 
    :type body: dict | bytes

    """
    body = StoragePayload.from_dict(body)
    return web.Response(status=200)


async def post_api_receipt_v1_verbose_storage(request: web.Request, apikey, body=None) -> web.Response:
    """transcribe a receipt in storage and return detailed result

    

    :param apikey: API authentication key.
    :type apikey: str
    :param body: 
    :type body: dict | bytes

    """
    body = StoragePayload.from_dict(body)
    return web.Response(status=200)
