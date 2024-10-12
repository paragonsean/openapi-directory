from typing import List, Dict
from aiohttp import web

from openapi_server.models.availability_request import AvailabilityRequest
from openapi_server.models.availability_results import AvailabilityResults
from openapi_server.models.error import Error
from openapi_server import util


async def wayback_v1_available_get(request: web.Request, url, timestamp=None, param_callback=None, timeout=None, closest=None, status_code=None, tag=None) -> web.Response:
    """wayback_v1_available_get

    

    :param url: A single URL to query.
    :type url: str
    :param timestamp: Timestamp requested in ISO 8601 format. The following formats are acceptable:  - YYYY  - YYYY-MM  - YYYY-MM-DD  - YYYY-MM-DDTHH:mm:SSz  - YYYY-MM-DD:HH:mm+00:00 
    :type timestamp: str
    :param param_callback: Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as &#x60;callback(data)&#x60;, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument. 
    :type param_callback: str
    :param timeout: Timeout is the maximum number of seconds to wait for the availability API to get its underlying results from the CDX server. The default value is 5.0. 
    :type timeout: 
    :param closest: The direction specifies whether to match archived timestamps that are before the provided one, after, or the default either (closest in either direction). Must be before, after, or either. May be overidden by individual requests. 
    :type closest: str
    :param status_code: HTTP status codes to filter by. Only results with these codes will be returned 
    :type status_code: int
    :param tag: The optional tag can have any value, and is returned with the results; it can be used to help collate input and output values. 
    :type tag: str

    """
    return web.Response(status=200)


async def wayback_v1_available_post(request: web.Request, url, timestamp=None, param_callback=None, timeout=None, closest=None, status_code=None, tag=None, body=None) -> web.Response:
    """wayback_v1_available_post

    

    :param url: A single URL to query.
    :type url: str
    :param timestamp: Timestamp requested in ISO 8601 format. The following formats are acceptable:  - YYYY  - YYYY-MM  - YYYY-MM-DD  - YYYY-MM-DDTHH:mm:SSz  - YYYY-MM-DD:HH:mm+00:00 
    :type timestamp: str
    :param param_callback: Specifies a JavaScript function func, for a JSON-P response. When provided, results are wrapped as &#x60;callback(data)&#x60;, and the returned MIME type is application/javascript. This causes the caller to automatically run the func with the JSON results as its argument. 
    :type param_callback: str
    :param timeout: Timeout is the maximum number of seconds to wait for the availability API to get its underlying results from the CDX server. The default value is 5.0. 
    :type timeout: 
    :param closest: The direction specifies whether to match archived timestamps that are before the provided one, after, or the default either (closest in either direction). Must be before, after, or either. May be overidden by individual requests. 
    :type closest: str
    :param status_code: HTTP status codes to filter by. Only results with these codes will be returned 
    :type status_code: int
    :param tag: The optional tag can have any value, and is returned with the results; it can be used to help collate input and output values. 
    :type tag: str
    :param body: 
    :type body: list | bytes

    """
    body = [AvailabilityRequest.from_dict(d) for d in body]
    return web.Response(status=200)
