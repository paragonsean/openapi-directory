from typing import List, Dict
from aiohttp import web

from openapi_server.models.news_articles_summary_search_result import NewsArticlesSummarySearchResult
from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def get_news_articles(request: web.Request, bill_id, skip=None, take=None) -> web.Response:
    """Returns a list of news articles for a Bill.

    

    :param bill_id: 
    :type bill_id: int
    :param skip: 
    :type skip: int
    :param take: 
    :type take: int

    """
    return web.Response(status=200)
