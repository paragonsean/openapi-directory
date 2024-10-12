from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.language_batch_input import LanguageBatchInput
from openapi_server.models.language_batch_result import LanguageBatchResult
from openapi_server import util


async def detect_language(request: web.Request, show_stats=None, language_batch_input=None) -> web.Response:
    """The API returns the detected language and a numeric score between 0 and 1.

    Scores close to 1 indicate 100% certainty that the identified language is true. A total of 120 languages are supported.

    :param show_stats: (optional) if set to true, response will contain input and document level statistics.
    :type show_stats: bool
    :param language_batch_input: Collection of documents to analyze.
    :type language_batch_input: dict | bytes

    """
    language_batch_input = LanguageBatchInput.from_dict(language_batch_input)
    return web.Response(status=200)
