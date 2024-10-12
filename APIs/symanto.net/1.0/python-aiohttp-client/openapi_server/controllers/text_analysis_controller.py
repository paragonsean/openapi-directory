from typing import List, Dict
from aiohttp import web

from openapi_server.models.language_detection import LanguageDetection
from openapi_server.models.language_predicted import LanguagePredicted
from openapi_server.models.post import Post
from openapi_server.models.post_predicted import PostPredicted
from openapi_server.models.topic_sentiment_output import TopicSentimentOutput
from openapi_server.models.validation_errors import ValidationErrors
from openapi_server import util


async def communication(request: web.Request, all=None, body=None) -> web.Response:
    """Communication &amp; Tonality

    Identify the purpose and writing style of a written text.  Supported Languages: [&#x60;ar&#x60;, &#x60;de&#x60;, &#x60;en&#x60;, &#x60;es&#x60;, &#x60;fr&#x60;, &#x60;it&#x60;, &#x60;nl&#x60;, &#x60;pt&#x60;, &#x60;ru&#x60;, &#x60;tr&#x60;, &#x60;zh&#x60;]  Returned labels: * action-seeking * fact-oriented * information-seeking * self-revealing

    :param all: 
    :type all: bool
    :param body: 
    :type body: list | bytes

    """
    body = [Post.from_dict(d) for d in body]
    return web.Response(status=200)


async def ekman_emotion(request: web.Request, all=None, body=None) -> web.Response:
    """Emotion Analysis

    Detect the emotions of the text based on Ekman.  Supported Langauges: [&#x60;en&#x60;, &#x60;de&#x60;, &#x60;es&#x60;]  Returned labels: * anger * disgust * fear * joy * sadness * surprise * no-emotion

    :param all: 
    :type all: bool
    :param body: 
    :type body: list | bytes

    """
    body = [Post.from_dict(d) for d in body]
    return web.Response(status=200)


async def emotion(request: web.Request, all=None, body=None) -> web.Response:
    """Emotion Analysis

    Detect the emotions of the text.  Supported Langauges: [&#x60;en&#x60;, &#x60;de&#x60;, &#x60;es&#x60;]  Returned labels: * anger * joy * love * sadness * surprise * uncategorized

    :param all: 
    :type all: bool
    :param body: 
    :type body: list | bytes

    """
    body = [Post.from_dict(d) for d in body]
    return web.Response(status=200)


async def language_detection(request: web.Request, body=None) -> web.Response:
    """Language Detection

    Identifies what language a text is written in. Only languages that our API supports can be analyzed.  Returned labels: * language_code of the detected language

    :param body: 
    :type body: list | bytes

    """
    body = [LanguageDetection.from_dict(d) for d in body]
    return web.Response(status=200)


async def personality(request: web.Request, all=None, body=None) -> web.Response:
    """Personality Traits

    Predict the personality trait of author of any written text.  Supported Languages: [&#x60;ar&#x60;, &#x60;de&#x60;, &#x60;en&#x60;, &#x60;es&#x60;, &#x60;fr&#x60;, &#x60;it&#x60;, &#x60;nl&#x60;, &#x60;pt&#x60;, &#x60;ru&#x60;, &#x60;tr&#x60;, &#x60;zh&#x60;]  Returned labels:  * emotional * rational

    :param all: 
    :type all: bool
    :param body: 
    :type body: list | bytes

    """
    body = [Post.from_dict(d) for d in body]
    return web.Response(status=200)


async def sentiment(request: web.Request, all=None, body=None) -> web.Response:
    """Sentiment Analysis

    Evaluate the overall tonality of the text.  Supported Languages: [&#x60;en&#x60;, &#x60;de&#x60;, &#x60;es&#x60;]  Returned labels: * positive * negative

    :param all: 
    :type all: bool
    :param body: 
    :type body: list | bytes

    """
    body = [Post.from_dict(d) for d in body]
    return web.Response(status=200)


async def topic_sentiment(request: web.Request, domain=None, body=None) -> web.Response:
    """Extracts topics and sentiments and relates them.

    

    :param domain: Provide analysis domain for better extraction (optional)
    :type domain: str
    :param body: 
    :type body: list | bytes

    """
    body = [Post.from_dict(d) for d in body]
    return web.Response(status=200)
