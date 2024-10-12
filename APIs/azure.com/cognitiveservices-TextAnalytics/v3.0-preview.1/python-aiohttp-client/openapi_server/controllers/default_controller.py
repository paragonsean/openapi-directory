from typing import List, Dict
from aiohttp import web

from openapi_server.models.entities_result import EntitiesResult
from openapi_server.models.entity_linking_result import EntityLinkingResult
from openapi_server.models.key_phrase_result import KeyPhraseResult
from openapi_server.models.language_batch_input import LanguageBatchInput
from openapi_server.models.language_result import LanguageResult
from openapi_server.models.multi_language_batch_input import MultiLanguageBatchInput
from openapi_server.models.sentiment_response import SentimentResponse
from openapi_server.models.text_analytics_error import TextAnalyticsError
from openapi_server import util


async def entities_linking(request: web.Request, input, model_version=None, show_stats=None) -> web.Response:
    """Linked entities from a well-known knowledge base

    The API returns a list of recognized entities with links to a well-known knowledge base. See the &lt;a href&#x3D;\&quot;https://aka.ms/talangs\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages.

    :param input: Collection of documents to analyze.
    :type input: dict | bytes
    :param model_version: (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version. 
    :type model_version: str
    :param show_stats: (Optional) if set to true, response will contain input and document level statistics.
    :type show_stats: bool

    """
    input = MultiLanguageBatchInput.from_dict(input)
    return web.Response(status=200)


async def entities_recognition_general(request: web.Request, input, model_version=None, show_stats=None) -> web.Response:
    """Named Entity Recognition

    The API returns a list of general named entities in a given document. For the list of supported entity types, check &lt;a href&#x3D;\&quot;https://aka.ms/taner\&quot;&gt;Supported Entity Types in Text Analytics API&lt;/a&gt;. See the &lt;a href&#x3D;\&quot;https://aka.ms/talangs\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages.

    :param input: Collection of documents to analyze.
    :type input: dict | bytes
    :param model_version: (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version. 
    :type model_version: str
    :param show_stats: (Optional) if set to true, response will contain input and document level statistics.
    :type show_stats: bool

    """
    input = MultiLanguageBatchInput.from_dict(input)
    return web.Response(status=200)


async def entities_recognition_pii(request: web.Request, input, model_version=None, show_stats=None) -> web.Response:
    """Entities containing personal information

    The API returns a list of entities with personal information (\\\&quot;SSN\\\&quot;, \\\&quot;Bank Account\\\&quot; etc) in the document. For the list of supported entity types, check &lt;a href&#x3D;\&quot;https://aka.ms/tanerpii\&quot;&gt;Supported Entity Types in Text Analytics API&lt;/a&gt;. See the &lt;a href&#x3D;\&quot;https://aka.ms/talangs\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages. 

    :param input: Collection of documents to analyze.
    :type input: dict | bytes
    :param model_version: (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version. 
    :type model_version: str
    :param show_stats: (Optional) if set to true, response will contain input and document level statistics.
    :type show_stats: bool

    """
    input = MultiLanguageBatchInput.from_dict(input)
    return web.Response(status=200)


async def key_phrases(request: web.Request, input, model_version=None, show_stats=None) -> web.Response:
    """Key Phrases

    The API returns a list of strings denoting the key phrases in the input text. See the &lt;a href&#x3D;\&quot;https://aka.ms/talangs\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages.

    :param input: Collection of documents to analyze. Documents can now contain a language field to indicate the text language
    :type input: dict | bytes
    :param model_version: (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version. 
    :type model_version: str
    :param show_stats: (Optional) if set to true, response will contain input and document level statistics.
    :type show_stats: bool

    """
    input = MultiLanguageBatchInput.from_dict(input)
    return web.Response(status=200)


async def languages(request: web.Request, input, model_version=None, show_stats=None) -> web.Response:
    """Detect Language

    The API returns the detected language and a numeric score between 0 and 1. Scores close to 1 indicate 100% certainty that the identified language is true. See the &lt;a href&#x3D;\&quot;https://aka.ms/talangs\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages.

    :param input: Collection of documents to analyze.
    :type input: dict | bytes
    :param model_version: (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version. 
    :type model_version: str
    :param show_stats: (Optional) if set to true, response will contain input and document level statistics.
    :type show_stats: bool

    """
    input = LanguageBatchInput.from_dict(input)
    return web.Response(status=200)


async def sentiment(request: web.Request, input, model_version=None, show_stats=None) -> web.Response:
    """Sentiment

    The API returns a sentiment prediction, as well as sentiment scores for each sentiment class (Positive, Negative, and Neutral) for the document and each sentence within it. See the &lt;a href&#x3D;\&quot;https://aka.ms/talangs\&quot;&gt;Supported languages in Text Analytics API&lt;/a&gt; for the list of enabled languages.

    :param input: Collection of documents to analyze.
    :type input: dict | bytes
    :param model_version: (Optional) This value indicates which model will be used for scoring. If a model-version is not specified, the API should default to the latest, non-preview version. 
    :type model_version: str
    :param show_stats: (Optional) if set to true, response will contain input and document level statistics.
    :type show_stats: bool

    """
    input = MultiLanguageBatchInput.from_dict(input)
    return web.Response(status=200)
