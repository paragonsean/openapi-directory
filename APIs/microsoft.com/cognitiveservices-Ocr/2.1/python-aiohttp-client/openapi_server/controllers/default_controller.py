from typing import List, Dict
from aiohttp import web

from openapi_server.models.computer_vision_error import ComputerVisionError
from openapi_server.models.image_url import ImageUrl
from openapi_server.models.read_operation_result import ReadOperationResult
from openapi_server.models.text_operation_result import TextOperationResult
from openapi_server import util


async def batch_read_file(request: web.Request, body) -> web.Response:
    """batch_read_file

    Use this interface to get the result of a Read operation, employing the state-of-the-art Optical Character Recognition (OCR) algorithms optimized for text-heavy documents. When you use the Read File interface, the response contains a field called &#39;Operation-Location&#39;. The &#39;Operation-Location&#39; field contains the URL that you must use for your &#39;GetReadOperationResult&#39; operation to access OCR results.​

    :param body: A JSON document with a URL pointing to the image that is to be analyzed.
    :type body: dict | bytes

    """
    body = ImageUrl.from_dict(body)
    return web.Response(status=200)


async def get_read_operation_result(request: web.Request, operation_id) -> web.Response:
    """get_read_operation_result

    This interface is used for getting OCR results of Read operation. The URL to this interface should be retrieved from &#39;Operation-Location&#39; field returned from Batch Read File interface.

    :param operation_id: Id of read operation returned in the response of the &#39;Batch Read File&#39; interface.
    :type operation_id: str

    """
    return web.Response(status=200)


async def get_text_operation_result(request: web.Request, operation_id) -> web.Response:
    """get_text_operation_result

    This interface is used for getting text operation result. The URL to this interface should be retrieved from &#39;Operation-Location&#39; field returned from Recognize Text interface.

    :param operation_id: Id of the text operation returned in the response of the &#39;Recognize Text&#39;
    :type operation_id: str

    """
    return web.Response(status=200)


async def recognize_text(request: web.Request, mode, body) -> web.Response:
    """recognize_text

    Recognize Text operation. When you use the Recognize Text interface, the response contains a field called &#39;Operation-Location&#39;. The &#39;Operation-Location&#39; field contains the URL that you must use for your Get Recognize Text Operation Result operation.

    :param mode: Type of text to recognize.
    :type mode: str
    :param body: A JSON document with a URL pointing to the image that is to be analyzed.
    :type body: dict | bytes

    """
    body = ImageUrl.from_dict(body)
    return web.Response(status=200)
