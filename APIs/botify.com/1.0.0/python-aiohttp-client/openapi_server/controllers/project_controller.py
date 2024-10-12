from typing import List, Dict
from aiohttp import web

from openapi_server.models.default_payload import DefaultPayload
from openapi_server.models.get_project_analyses200_response import GetProjectAnalyses200Response
from openapi_server.models.get_saved_filters200_response import GetSavedFilters200Response
from openapi_server.models.project_saved_filter import ProjectSavedFilter
from openapi_server.models.url_rewriting_rules_serializer import URLRewritingRulesSerializer
from openapi_server.models.urls_aggs_query import UrlsAggsQuery
from openapi_server import util


async def get_project_analyses(request: web.Request, username, project_slug, page=None, size=None) -> web.Response:
    """List all analyses for a project

    List all analyses for a project

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str
    :param page: Page Number
    :type page: int
    :param size: Page Size
    :type size: int

    """
    return web.Response(status=200)


async def get_project_urls_aggs(request: web.Request, username, project_slug, area=None, last_analysis_slug=None, nb_analyses=None, body=None) -> web.Response:
    """Project Query aggregator

    Project Query aggregator. It accepts multiple queries that will be executed on all completed analyses in the project

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str
    :param area: Analysis context to execute the queries
    :type area: str
    :param last_analysis_slug: Last analysis on the trend
    :type last_analysis_slug: str
    :param nb_analyses: Max number of analysis to return
    :type nb_analyses: int
    :param body: 
    :type body: list | bytes

    """
    body = [UrlsAggsQuery.from_dict(d) for d in body]
    return web.Response(status=200)


async def get_saved_filter(request: web.Request, username, project_slug, identifier) -> web.Response:
    """Retrieves a specific saved filter&#39;s name, ID and filter value

    Retrieves a specific saved filter&#39;s name, ID and filter value

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str
    :param identifier: Saved Filter&#39;s identifier
    :type identifier: str

    """
    return web.Response(status=200)


async def get_saved_filters(request: web.Request, username, project_slug, page=None, size=None) -> web.Response:
    """List all the project&#39;s saved filters (each filter&#39;s name, ID and filter value)

    List all the project&#39;s saved filters (each filter&#39;s name, ID and filter value)

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str
    :param page: Page Number
    :type page: int
    :param size: Page Size
    :type size: int

    """
    return web.Response(status=200)


async def test_url_rewriting_rules(request: web.Request, username, project_slug) -> web.Response:
    """Match and replace parts of a URL based on rules passed in POST data

    Match and replace parts of a URL based on rules passed in POST data.

    :param username: User&#39;s identifier
    :type username: str
    :param project_slug: Project&#39;s identifier
    :type project_slug: str

    """
    return web.Response(status=200)
