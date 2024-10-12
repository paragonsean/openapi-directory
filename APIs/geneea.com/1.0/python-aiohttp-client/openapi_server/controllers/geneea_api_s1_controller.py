from typing import List, Dict
from aiohttp import web

from openapi_server.models.entities_response import EntitiesResponse
from openapi_server.models.lemmatize_response import LemmatizeResponse
from openapi_server.models.request import Request
from openapi_server.models.sentiment_response import SentimentResponse
from openapi_server.models.topic_response import TopicResponse
from openapi_server import util


async def correction_get(request: web.Request, id=None, text=None, url=None, extractor=None, language=None, return_text_info=None) -> web.Response:
    """Performs text correction (diacritization) on the given document

    &lt;br/&gt;&lt;strong&gt;Possible options:&lt;/strong&gt;&lt;p class&#x3D;\&quot;markdown\&quot;&gt;An optional parameter &lt;code&gt;diacritize&lt;/code&gt; with values &lt;code&gt;yes&lt;/code&gt;, &lt;code&gt;no&lt;/code&gt; or &lt;code&gt;auto&lt;/code&gt; indicate whether the text diacritization will be performed. The default value is &lt;code&gt;auto&lt;/code&gt;.&lt;/p&gt;

    :param id: document ID
    :type id: str
    :param text: raw document text
    :type text: str
    :param url: document URL
    :type url: str
    :param extractor: document extractor
    :type extractor: str
    :param language: document language
    :type language: str
    :param return_text_info: 
    :type return_text_info: bool

    """
    return web.Response(status=200)


async def correction_post(request: web.Request, body=None) -> web.Response:
    """Performs text correction (diacritization) on the given document

    &lt;strong&gt;Notes:&lt;/strong&gt;&lt;br/&gt;Valid JSON cannot contain newline characters. These have to be escaped. (See also &lt;a href&#x3D;\&quot;https://geneea.atlassian.net/wiki/display/IPD/The+Interpretor+API+Public+Documentation#TheInterpretorAPIPublicDocumentation-Interactiveonlinedocumentation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Interpretor documentation&lt;/a&gt;)&lt;br/&gt;Fields &lt;code&gt;text&lt;/code&gt; and &lt;code&gt;url&lt;/code&gt; are mutually exclusive.&lt;br/&gt;&lt;strong&gt;Examples:&lt;/strong&gt;&lt;pre&gt;&lt;code&gt;{\&quot;text\&quot;: \&quot;Hello world!\&quot;}&lt;/code&gt;&lt;/pre&gt;&lt;pre&gt;&lt;code&gt;{\&quot;url\&quot;: \&quot;https://en.wikipedia.org/wiki/Pyrrhuloxia\&quot;}&lt;/code&gt;&lt;/pre&gt;&lt;br/&gt;&lt;strong&gt;Possible options:&lt;/strong&gt;&lt;p class&#x3D;\&quot;markdown\&quot;&gt;An optional parameter &lt;code&gt;diacritize&lt;/code&gt; with values &lt;code&gt;yes&lt;/code&gt;, &lt;code&gt;no&lt;/code&gt; or &lt;code&gt;auto&lt;/code&gt; indicate whether the text diacritization will be performed. The default value is &lt;code&gt;auto&lt;/code&gt;.&lt;/p&gt;

    :param body: request
    :type body: dict | bytes

    """
    body = Request.from_dict(body)
    return web.Response(status=200)


async def entities_get(request: web.Request, id=None, text=None, url=None, extractor=None, language=None, return_text_info=None) -> web.Response:
    """Performs named-entity recognition on the given document

    entitiesGet

    :param id: document ID
    :type id: str
    :param text: raw document text
    :type text: str
    :param url: document URL
    :type url: str
    :param extractor: document extractor
    :type extractor: str
    :param language: document language
    :type language: str
    :param return_text_info: 
    :type return_text_info: bool

    """
    return web.Response(status=200)


async def entities_post(request: web.Request, body=None) -> web.Response:
    """Performs named-entity recognition on the given document

    &lt;strong&gt;Notes:&lt;/strong&gt;&lt;br/&gt;Valid JSON cannot contain newline characters. These have to be escaped. (See also &lt;a href&#x3D;\&quot;https://geneea.atlassian.net/wiki/display/IPD/The+Interpretor+API+Public+Documentation#TheInterpretorAPIPublicDocumentation-Interactiveonlinedocumentation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Interpretor documentation&lt;/a&gt;)&lt;br/&gt;Fields &lt;code&gt;text&lt;/code&gt; and &lt;code&gt;url&lt;/code&gt; are mutually exclusive.&lt;br/&gt;&lt;strong&gt;Examples:&lt;/strong&gt;&lt;pre&gt;&lt;code&gt;{\&quot;text\&quot;: \&quot;Hello world!\&quot;}&lt;/code&gt;&lt;/pre&gt;&lt;pre&gt;&lt;code&gt;{\&quot;url\&quot;: \&quot;https://en.wikipedia.org/wiki/Pyrrhuloxia\&quot;}&lt;/code&gt;&lt;/pre&gt;

    :param body: request
    :type body: dict | bytes

    """
    body = Request.from_dict(body)
    return web.Response(status=200)


async def lemmatize_get(request: web.Request, id=None, text=None, url=None, extractor=None, language=None, return_text_info=None) -> web.Response:
    """Performs lemmatization on the given document

    lemmatizeGet

    :param id: document ID
    :type id: str
    :param text: raw document text
    :type text: str
    :param url: document URL
    :type url: str
    :param extractor: document extractor
    :type extractor: str
    :param language: document language
    :type language: str
    :param return_text_info: 
    :type return_text_info: bool

    """
    return web.Response(status=200)


async def lemmatize_post(request: web.Request, body=None) -> web.Response:
    """Performs lemmatization on the given document

    &lt;strong&gt;Notes:&lt;/strong&gt;&lt;br/&gt;Valid JSON cannot contain newline characters. These have to be escaped. (See also &lt;a href&#x3D;\&quot;https://geneea.atlassian.net/wiki/display/IPD/The+Interpretor+API+Public+Documentation#TheInterpretorAPIPublicDocumentation-Interactiveonlinedocumentation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Interpretor documentation&lt;/a&gt;)&lt;br/&gt;Fields &lt;code&gt;text&lt;/code&gt; and &lt;code&gt;url&lt;/code&gt; are mutually exclusive.&lt;br/&gt;&lt;strong&gt;Examples:&lt;/strong&gt;&lt;pre&gt;&lt;code&gt;{\&quot;text\&quot;: \&quot;Hello world!\&quot;}&lt;/code&gt;&lt;/pre&gt;&lt;pre&gt;&lt;code&gt;{\&quot;url\&quot;: \&quot;https://en.wikipedia.org/wiki/Pyrrhuloxia\&quot;}&lt;/code&gt;&lt;/pre&gt;

    :param body: request
    :type body: dict | bytes

    """
    body = Request.from_dict(body)
    return web.Response(status=200)


async def sentiment_get(request: web.Request, id=None, text=None, url=None, extractor=None, language=None, return_text_info=None) -> web.Response:
    """Performs sentiment analysis on the given document

    sentimentGet

    :param id: document ID
    :type id: str
    :param text: raw document text
    :type text: str
    :param url: document URL
    :type url: str
    :param extractor: document extractor
    :type extractor: str
    :param language: document language
    :type language: str
    :param return_text_info: 
    :type return_text_info: bool

    """
    return web.Response(status=200)


async def sentiment_post(request: web.Request, body=None) -> web.Response:
    """Performs sentiment analysis on the given document

    &lt;strong&gt;Notes:&lt;/strong&gt;&lt;br/&gt;Valid JSON cannot contain newline characters. These have to be escaped. (See also &lt;a href&#x3D;\&quot;https://geneea.atlassian.net/wiki/display/IPD/The+Interpretor+API+Public+Documentation#TheInterpretorAPIPublicDocumentation-Interactiveonlinedocumentation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Interpretor documentation&lt;/a&gt;)&lt;br/&gt;Fields &lt;code&gt;text&lt;/code&gt; and &lt;code&gt;url&lt;/code&gt; are mutually exclusive.&lt;br/&gt;&lt;strong&gt;Examples:&lt;/strong&gt;&lt;pre&gt;&lt;code&gt;{\&quot;text\&quot;: \&quot;Hello world!\&quot;}&lt;/code&gt;&lt;/pre&gt;&lt;pre&gt;&lt;code&gt;{\&quot;url\&quot;: \&quot;https://en.wikipedia.org/wiki/Pyrrhuloxia\&quot;}&lt;/code&gt;&lt;/pre&gt;

    :param body: request
    :type body: dict | bytes

    """
    body = Request.from_dict(body)
    return web.Response(status=200)


async def topic_get(request: web.Request, id=None, text=None, url=None, extractor=None, language=None, return_text_info=None) -> web.Response:
    """Performs topic detection on the given document

    topicGet

    :param id: document ID
    :type id: str
    :param text: raw document text
    :type text: str
    :param url: document URL
    :type url: str
    :param extractor: document extractor
    :type extractor: str
    :param language: document language
    :type language: str
    :param return_text_info: 
    :type return_text_info: bool

    """
    return web.Response(status=200)


async def topic_post(request: web.Request, body=None) -> web.Response:
    """Performs topic detection on the given document

    &lt;strong&gt;Notes:&lt;/strong&gt;&lt;br/&gt;Valid JSON cannot contain newline characters. These have to be escaped. (See also &lt;a href&#x3D;\&quot;https://geneea.atlassian.net/wiki/display/IPD/The+Interpretor+API+Public+Documentation#TheInterpretorAPIPublicDocumentation-Interactiveonlinedocumentation\&quot; target&#x3D;\&quot;_blank\&quot;&gt;Interpretor documentation&lt;/a&gt;)&lt;br/&gt;Fields &lt;code&gt;text&lt;/code&gt; and &lt;code&gt;url&lt;/code&gt; are mutually exclusive.&lt;br/&gt;&lt;strong&gt;Examples:&lt;/strong&gt;&lt;pre&gt;&lt;code&gt;{\&quot;text\&quot;: \&quot;Hello world!\&quot;}&lt;/code&gt;&lt;/pre&gt;&lt;pre&gt;&lt;code&gt;{\&quot;url\&quot;: \&quot;https://en.wikipedia.org/wiki/Pyrrhuloxia\&quot;}&lt;/code&gt;&lt;/pre&gt;

    :param body: request
    :type body: dict | bytes

    """
    body = Request.from_dict(body)
    return web.Response(status=200)
