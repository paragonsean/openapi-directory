from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.multi_language_batch_input import MultiLanguageBatchInput
from openapi_server.models.sentiment_batch_result import SentimentBatchResult
from openapi_server import util


async def sentiment(request: web.Request, input) -> web.Response:
    """The API returns a numeric score between 0 and 1.

    Scores close to 1 indicate positive sentiment, while scores close to 0 indicate negative sentiment. A score of 0.5 indicates the lack of sentiment (e.g. a factoid statement). See the &lt;a href&#x3D;\&quot;https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/overview#supported-languages\&quot;&gt;Text Analytics Documentation&lt;/a&gt; for details about the languages that are supported by sentiment analysis.

    :param input: Collection of documents to analyze.
    :type input: dict | bytes

    """
    input = MultiLanguageBatchInput.from_dict(input)
    return web.Response(status=200)
