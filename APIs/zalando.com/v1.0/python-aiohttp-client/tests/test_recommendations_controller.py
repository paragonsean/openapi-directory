# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_message import ErrorMessage
from openapi_server.models.recommendations_article import RecommendationsArticle


pytestmark = pytest.mark.asyncio

async def test_recommendations_article_ids_get(client):
    """Test case for recommendations_article_ids_get

    Get Recommendations by articleId
    """
    params = [('maxResults', 'max_results_example'),
                    ('fields', ['fields_example'])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
    }
    response = await client.request(
        method='GET',
        path='/recommendations/{article_ids}'.format(article_ids=['article_ids_example']),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

