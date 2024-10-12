from typing import List, Dict
from aiohttp import web

from openapi_server.models.analysis_request import AnalysisRequest
from openapi_server.models.analysis_response import AnalysisResponse
from openapi_server.models.error_model import ErrorModel
from openapi_server import util


async def ink_recognizer_recognize(request: web.Request, body, x_ms_client_request_id=None) -> web.Response:
    """ink_recognizer_recognize

    Ink Recognition operation is used to perform ink layout and recognition of written words and shapes. It allows passing the ink strokes to the service to get the recognition results in the response.

    :param body: The collection of stroke objects to send for analysis
    :type body: dict | bytes
    :param x_ms_client_request_id: The request id used to uniquely identify each request during troubleshooting. This is an optional parameter useful for correlating logs and other artifacts.
    :type x_ms_client_request_id: str

    """
    body = AnalysisRequest.from_dict(body)
    return web.Response(status=200)
