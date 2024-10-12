from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_input import BatchInput
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.language_batch_result import LanguageBatchResult
from openapi_server import util


async def detect_language(request: web.Request, input) -> web.Response:
    """The API returns the detected language and a numeric score between 0 and 1.

    Scores close to 1 indicate 100% certainty that the identified language is true. A total of 120 languages are supported.

    :param input: Collection of documents to analyze.
    :type input: dict | bytes

    """
    input = BatchInput.from_dict(input)
    return web.Response(status=200)
