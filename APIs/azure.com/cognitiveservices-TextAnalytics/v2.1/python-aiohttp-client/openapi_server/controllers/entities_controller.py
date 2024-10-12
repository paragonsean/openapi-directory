from typing import List, Dict
from aiohttp import web

from openapi_server.models.entities_batch_result import EntitiesBatchResult
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.multi_language_batch_input import MultiLanguageBatchInput
from openapi_server import util


async def entities(request: web.Request, show_stats=None, multi_language_batch_input=None) -> web.Response:
    """The API returns a list of recognized entities in a given document.

    To get even more information on each recognized entity we recommend using the Bing Entity Search API by querying for the recognized entities names. See the &lt;a href&#x3D;\&quot;https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/text-analytics-supported-languages\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages.

    :param show_stats: (optional) if set to true, response will contain input and document level statistics.
    :type show_stats: bool
    :param multi_language_batch_input: Collection of documents to analyze.
    :type multi_language_batch_input: dict | bytes

    """
    multi_language_batch_input = MultiLanguageBatchInput.from_dict(multi_language_batch_input)
    return web.Response(status=200)
