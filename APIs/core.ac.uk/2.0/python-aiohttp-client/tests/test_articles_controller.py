# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.article_history_response import ArticleHistoryResponse
from openapi_server.models.article_response import ArticleResponse
from openapi_server.models.article_search_response import ArticleSearchResponse
from openapi_server.models.article_similar_response import ArticleSimilarResponse
from openapi_server.models.search_request import SearchRequest
from openapi_server.models.similar_request import SimilarRequest


pytestmark = pytest.mark.asyncio

async def test_get_article_by_core_id(client):
    """Test case for get_article_by_core_id

    Get article by CORE ID
    """
    params = [('metadata', True),
                    ('fulltext', False),
                    ('citations', False),
                    ('similar', False),
                    ('duplicate', False),
                    ('urls', False),
                    ('faithfulMetadata', False)]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api-v2/articles/get/{core_id}'.format(core_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_get_article_by_core_id_batch(client):
    """Test case for get_article_by_core_id_batch

    Batch operation for retrieving articles by CORE ID
    """
    body = [56]
    params = [('metadata', True),
                    ('fulltext', False),
                    ('citations', False),
                    ('similar', False),
                    ('duplicate', False),
                    ('urls', False),
                    ('faithfulMetadata', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api-v2/articles/get',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_article_history_by_core_id(client):
    """Test case for get_article_history_by_core_id

    Get article history by CORE ID
    """
    params = [('page', 1),
                    ('pageSize', 10)]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api-v2/articles/get/{core_id}/history'.format(core_id='core_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_article_pdf_by_core_id(client):
    """Test case for get_article_pdf_by_core_id

    Get fulltext PDF by CORE ID
    """
    headers = { 
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api-v2/articles/get/{core_id}/download/pdf'.format(core_id='core_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_near_duplicate_articles(client):
    """Test case for near_duplicate_articles

    Get all near duplicate articles
    """
    params = [('doi', 'doi_example'),
                    ('title', 'title_example'),
                    ('year', 'year_example'),
                    ('description', 'description_example'),
                    ('fulltext', 'fulltext_example'),
                    ('identifier', 'identifier_example'),
                    ('repositoryId', 'repository_id_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api-v2/articles/dedup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_articles(client):
    """Test case for search_articles

    Search through all documents
    """
    params = [('page', 1),
                    ('pageSize', 10),
                    ('metadata', True),
                    ('fulltext', False),
                    ('citations', False),
                    ('similar', False),
                    ('duplicate', False),
                    ('urls', False),
                    ('faithfulMetadata', False)]
    headers = { 
        'Accept': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api-v2/articles/search/{query}'.format(query=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_search_articles_batch(client):
    """Test case for search_articles_batch

    Batch operation for search through articles
    """
    body = [openapi_server.SearchRequest()]
    params = [('metadata', True),
                    ('fulltext', False),
                    ('citations', False),
                    ('similar', False),
                    ('duplicate', False),
                    ('urls', False),
                    ('faithfulMetadata', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api-v2/articles/search',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_similar_articles(client):
    """Test case for similar_articles

    Get articles by similarity to a text
    """
    body = openapi_server.SimilarRequest()
    params = [('limit', 10),
                    ('metadata', True),
                    ('fulltext', False),
                    ('citations', False),
                    ('similar', False),
                    ('duplicate', False),
                    ('urls', False),
                    ('faithfulMetadata', False)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'apiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api-v2/articles/similar',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

