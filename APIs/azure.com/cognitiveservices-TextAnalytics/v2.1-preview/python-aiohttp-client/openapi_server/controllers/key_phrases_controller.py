from typing import List, Dict
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.key_phrase_batch_result import KeyPhraseBatchResult
from openapi_server.models.multi_language_batch_input import MultiLanguageBatchInput
from openapi_server import util


async def key_phrases(request: web.Request, input) -> web.Response:
    """The API returns a list of strings denoting the key talking points in the input text.

    See the &lt;a href&#x3D;\&quot;https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/overview#supported-languages\&quot;&gt;Text Analytics Documentation&lt;/a&gt; for details about the languages that are supported by key phrase extraction.

    :param input: Collection of documents to analyze. Documents can now contain a language field to indicate the text language
    :type input: dict | bytes

    """
    input = MultiLanguageBatchInput.from_dict(input)
    return web.Response(status=200)
