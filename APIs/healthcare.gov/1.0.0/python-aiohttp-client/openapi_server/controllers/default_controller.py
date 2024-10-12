from typing import List, Dict
from aiohttp import web

from openapi_server.models.articles_list import ArticlesList
from openapi_server.models.blog_list import BlogList
from openapi_server.models.blog_page import BlogPage
from openapi_server.models.glossary_list import GlossaryList
from openapi_server.models.glossary_page import GlossaryPage
from openapi_server.models.page import Page
from openapi_server.models.question_page import QuestionPage
from openapi_server.models.questions_list import QuestionsList
from openapi_server.models.state_page import StatePage
from openapi_server.models.states_list import StatesList
from openapi_server.models.topics_list import TopicsList
from openapi_server import util


async def api_articlesmedia_type_extension_get(request: web.Request, media_type_extension) -> web.Response:
    """api_articlesmedia_type_extension_get

    Returns pages content.

    :param media_type_extension: Omiting the param causes html to be returned.
    :type media_type_extension: str

    """
    return web.Response(status=200)


async def api_blogmedia_type_extension_get(request: web.Request, media_type_extension) -> web.Response:
    """api_blogmedia_type_extension_get

    Returns pages content.

    :param media_type_extension: Omiting the param causes html to be returned.
    :type media_type_extension: str

    """
    return web.Response(status=200)


async def api_glossarymedia_type_extension_get(request: web.Request, media_type_extension) -> web.Response:
    """api_glossarymedia_type_extension_get

    Returns pages content.

    :param media_type_extension: Omiting the param causes html to be returned.
    :type media_type_extension: str

    """
    return web.Response(status=200)


async def api_questionsmedia_type_extension_get(request: web.Request, media_type_extension) -> web.Response:
    """api_questionsmedia_type_extension_get

    Returns pages content.

    :param media_type_extension: Omiting the param causes html to be returned.
    :type media_type_extension: str

    """
    return web.Response(status=200)


async def api_statesmedia_type_extension_get(request: web.Request, media_type_extension) -> web.Response:
    """api_statesmedia_type_extension_get

    Returns pages content.

    :param media_type_extension: Omiting the param causes html to be returned.
    :type media_type_extension: str

    """
    return web.Response(status=200)


async def api_topicsmedia_type_extension_get(request: web.Request, media_type_extension) -> web.Response:
    """api_topicsmedia_type_extension_get

    Returns pages content.

    :param media_type_extension: Omiting the param causes html to be returned.
    :type media_type_extension: str

    """
    return web.Response(status=200)


async def blog_page_namemedia_type_extension_get(request: web.Request, media_type_extension, page_name) -> web.Response:
    """blog_page_namemedia_type_extension_get

    Returns pages content.

    :param media_type_extension: Omiting the param causes html to be returned.
    :type media_type_extension: str
    :param page_name: 
    :type page_name: str

    """
    return web.Response(status=200)


async def es_blog_page_namemedia_type_extension_get(request: web.Request, media_type_extension, page_name) -> web.Response:
    """es_blog_page_namemedia_type_extension_get

    Returns pages content.

    :param media_type_extension: Omiting the param causes html to be returned.
    :type media_type_extension: str
    :param page_name: 
    :type page_name: str

    """
    return web.Response(status=200)


async def es_glossary_page_namemedia_type_extension_get(request: web.Request, media_type_extension, page_name) -> web.Response:
    """es_glossary_page_namemedia_type_extension_get

    Returns pages content.

    :param media_type_extension: Omiting the param causes html to be returned.
    :type media_type_extension: str
    :param page_name: 
    :type page_name: str

    """
    return web.Response(status=200)


async def es_page_namemedia_type_extension_get(request: web.Request, media_type_extension, page_name) -> web.Response:
    """es_page_namemedia_type_extension_get

    Returns pages content.

    :param media_type_extension: Omiting the param causes html to be returned.
    :type media_type_extension: str
    :param page_name: 
    :type page_name: str

    """
    return web.Response(status=200)


async def es_question_page_namemedia_type_extension_get(request: web.Request, media_type_extension, page_name) -> web.Response:
    """es_question_page_namemedia_type_extension_get

    Returns pages content.

    :param media_type_extension: Omiting the param causes html to be returned.
    :type media_type_extension: str
    :param page_name: 
    :type page_name: str

    """
    return web.Response(status=200)


async def es_state_namemedia_type_extension_get(request: web.Request, media_type_extension, state_name) -> web.Response:
    """es_state_namemedia_type_extension_get

    Returns pages content.

    :param media_type_extension: Omiting the param causes html to be returned.
    :type media_type_extension: str
    :param state_name: 
    :type state_name: str

    """
    return web.Response(status=200)


async def glossary_page_namemedia_type_extension_get(request: web.Request, media_type_extension, page_name) -> web.Response:
    """glossary_page_namemedia_type_extension_get

    Returns pages content.

    :param media_type_extension: Omiting the param causes html to be returned.
    :type media_type_extension: str
    :param page_name: 
    :type page_name: str

    """
    return web.Response(status=200)


async def page_namemedia_type_extension_get(request: web.Request, media_type_extension, page_name) -> web.Response:
    """page_namemedia_type_extension_get

    Returns pages content.

    :param media_type_extension: Omiting the param causes html to be returned.
    :type media_type_extension: str
    :param page_name: 
    :type page_name: str

    """
    return web.Response(status=200)


async def question_page_namemedia_type_extension_get(request: web.Request, media_type_extension, page_name) -> web.Response:
    """question_page_namemedia_type_extension_get

    Returns pages content.

    :param media_type_extension: Omiting the param causes html to be returned.
    :type media_type_extension: str
    :param page_name: 
    :type page_name: str

    """
    return web.Response(status=200)


async def state_namemedia_type_extension_get(request: web.Request, media_type_extension, state_name) -> web.Response:
    """state_namemedia_type_extension_get

    Returns pages content.

    :param media_type_extension: Omiting the param causes html to be returned.
    :type media_type_extension: str
    :param state_name: 
    :type state_name: str

    """
    return web.Response(status=200)
