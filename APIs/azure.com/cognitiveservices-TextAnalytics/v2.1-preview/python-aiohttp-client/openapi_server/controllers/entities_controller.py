from typing import List, Dict
from aiohttp import web

from openapi_server.models.entities_batch_result_v2dot1 import EntitiesBatchResultV2dot1
from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.multi_language_batch_input import MultiLanguageBatchInput
from openapi_server import util


async def entities(request: web.Request, input) -> web.Response:
    """The API returns a list of recognized entities in a given document.

    The API returns a list of recognized entities in a given document. To get even more information on each recognized entity we recommend using the Bing Entity Search API by querying for the recognized entities names. See the &lt;a href&#x3D;\&quot;https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/text-analytics-supported-languages\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages.The API returns a list of known entities and general named entities (\&quot;Person\&quot;, \&quot;Location\&quot;, \&quot;Organization\&quot; etc) in a given document. Known entities are returned with Wikipedia Id and Wikipedia link, and also Bing Id which can be used in Bing Entity Search API. General named entities are returned with entity types. If a general named entity is also a known entity, then all information regarding it (Wikipedia Id, Bing Id, entity type etc) will be returned. See the &lt;a href&#x3D;\&quot;https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/how-tos/text-analytics-how-to-entity-linking#supported-types-for-named-entity-recognition\&quot;&gt;Supported Entity Types in Text Analytics API&lt;/a&gt; for the list of supported Entity Types. See the &lt;a href&#x3D;\&quot;https://docs.microsoft.com/en-us/azure/cognitive-services/text-analytics/text-analytics-supported-languages\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages.

    :param input: Collection of documents to analyze.
    :type input: dict | bytes

    """
    input = MultiLanguageBatchInput.from_dict(input)
    return web.Response(status=200)
