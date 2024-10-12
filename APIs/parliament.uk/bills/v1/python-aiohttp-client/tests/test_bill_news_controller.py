# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.news_articles_summary_search_result import NewsArticlesSummarySearchResult
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_get_news_articles(client):
    """Test case for get_news_articles

    Returns a list of news articles for a Bill.
    """
    params = [('Skip', 56),
                    ('Take', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/Bills/{bill_id}/NewsArticles'.format(bill_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

