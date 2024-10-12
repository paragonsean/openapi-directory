from typing import List, Dict
from aiohttp import web

from openapi_server import util


async def adult_content_detection(request: web.Request, api_key, text=None) -> web.Response:
    """Classifies the Document as adult or noadult

    The Adult Content Detection function classifies the documents as adult or noadult based on their context. It can be used to detect whether a document contains content unsuitable for minors.

    :param api_key: Your API Key
    :type api_key: str
    :param text: The text that you want to analyze. It should not contain HTML tags.
    :type text: str

    """
    return web.Response(status=200)


async def commercial_detection(request: web.Request, api_key, text=None) -> web.Response:
    """Classifies the Document as commercial or nocommercial

    The Commercial Detection function labels the documents as commercial or non-commercial based on their keywords and expressions. It can be used to detect whether a website is commercial or not.

    :param api_key: Your API Key
    :type api_key: str
    :param text: The text that you want to analyze. It should not contain HTML tags.
    :type text: str

    """
    return web.Response(status=200)


async def educational_detection(request: web.Request, api_key, text=None) -> web.Response:
    """Classifies the Document as educational or noeducational

    The Educational Detection function classifies the documents as educational or non-educational based on their context. It can be used to detect whether a website is educational or not.

    :param api_key: Your API Key
    :type api_key: str
    :param text: The text that you want to analyze. It should not contain HTML tags.
    :type text: str

    """
    return web.Response(status=200)


async def gender_detection(request: web.Request, api_key, text=None) -> web.Response:
    """Gender Detection Service

    The Gender Detection function identifies if a particular document is written-by or targets-to a man or a woman based on the context, the words and the idioms found in the text.

    :param api_key: Your API Key
    :type api_key: str
    :param text: The text that you want to analyze. It should not contain HTML tags.
    :type text: str

    """
    return web.Response(status=200)


async def language_detection(request: web.Request, api_key, text=None) -> web.Response:
    """Identifies the Language of the Document

    The Language Detection function identifies the natural language of the given document based on its words and context. This classifier is able to detect 96 different languages.

    :param api_key: Your API Key
    :type api_key: str
    :param text: The text that you want to analyze. It should not contain HTML tags.
    :type text: str

    """
    return web.Response(status=200)


async def readability_assessment(request: web.Request, api_key, text=None) -> web.Response:
    """Evaluates the Readability of the Document

    The Readability Assessment function determines the degree of readability of a document based on its terms and idioms. The texts are classified as basic, intermediate and advanced depending their difficulty.

    :param api_key: Your API Key
    :type api_key: str
    :param text: The text that you want to analyze. It should not contain HTML tags.
    :type text: str

    """
    return web.Response(status=200)


async def sentiment_analysis(request: web.Request, api_key, text=None) -> web.Response:
    """Identifies the Sentiment of the Document

    The Sentiment Analysis function classifies documents as positive, negative or neutral (lack of sentiment) depending on whether they express a positive, negative or neutral opinion.

    :param api_key: Your API Key
    :type api_key: str
    :param text: The text that you want to analyze. It should not contain HTML tags.
    :type text: str

    """
    return web.Response(status=200)


async def spam_detection(request: web.Request, api_key, text=None) -> web.Response:
    """Classifies the Document as spam or nospam

    The Spam Detection function labels documents as spam or nospam by taking into account their context. It can be used to filter out spam emails and comments.

    :param api_key: Your API Key
    :type api_key: str
    :param text: The text that you want to analyze. It should not contain HTML tags.
    :type text: str

    """
    return web.Response(status=200)


async def subjectivity_analysis(request: web.Request, api_key, text=None) -> web.Response:
    """Classifies Document as Subjective or Objective

    The Subjectivity Analysis function categorizes documents as subjective or objective based on their writing style. Texts that express personal opinions are labeled as subjective and the others as objective.

    :param api_key: Your API Key
    :type api_key: str
    :param text: The text that you want to analyze. It should not contain HTML tags.
    :type text: str

    """
    return web.Response(status=200)


async def topic_classification(request: web.Request, api_key, text=None) -> web.Response:
    """Identifies the Topic of the Document

    The Topic Classification function assigns documents in 12 thematic categories based on their keywords, idioms and jargon. It can be used to identify the topic of the texts.

    :param api_key: Your API Key
    :type api_key: str
    :param text: The text that you want to analyze. It should not contain HTML tags.
    :type text: str

    """
    return web.Response(status=200)


async def twitter_sentiment_analysis(request: web.Request, api_key, text=None) -> web.Response:
    """Identifies the Sentiment of Twitter Messages

    The Twitter Sentiment Analysis function allows you to perform Sentiment Analysis on Twitter. It classifies the tweets as positive, negative or neutral depending on their context.

    :param api_key: Your API Key
    :type api_key: str
    :param text: The text of the tweet that we evaluate.
    :type text: str

    """
    return web.Response(status=200)
