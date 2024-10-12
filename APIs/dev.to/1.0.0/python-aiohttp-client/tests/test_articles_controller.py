# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.article import Article
from openapi_server.models.article_index import ArticleIndex
from openapi_server.models.video_article import VideoArticle


pytestmark = pytest.mark.asyncio

async def test_create_article(client):
    """Test case for create_article

    Publish article
    """
    body = {"article":{"body_markdown":"body_markdown","main_image":"main_image","series":"series","organization_id":0,"description":"description","published":False,"canonical_url":"canonical_url","title":"title","tags":"tags"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/api/articles',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_article_by_id(client):
    """Test case for get_article_by_id

    Published article by id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/api/articles/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_article_by_path(client):
    """Test case for get_article_by_path

    Published article by path
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/api/articles/{username}/{slug}'.format(username='username_example', slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_articles(client):
    """Test case for get_articles

    Published articles
    """
    params = [('page', 1),
                    ('per_page', 30),
                    ('tag', 'discuss'),
                    ('tags', 'javascript, css'),
                    ('tags_exclude', 'node, java'),
                    ('username', 'ben'),
                    ('state', 'fresh'),
                    ('top', 2),
                    ('collection_id', 99)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/api/articles',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_latest_articles(client):
    """Test case for get_latest_articles

    Published articles sorted by published date
    """
    params = [('page', 1),
                    ('per_page', 30)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/api/articles/latest',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_org_articles_0(client):
    """Test case for get_org_articles_0

    Organization's Articles
    """
    params = [('page', 1),
                    ('per_page', 30)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/api/organizations/{username}/articles'.format(username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_all_articles(client):
    """Test case for get_user_all_articles

    User's all articles
    """
    params = [('page', 1),
                    ('per_page', 30)]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/api/articles/me/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_articles(client):
    """Test case for get_user_articles

    User's articles
    """
    params = [('page', 1),
                    ('per_page', 30)]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/api/articles/me',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_published_articles(client):
    """Test case for get_user_published_articles

    User's published articles
    """
    params = [('page', 1),
                    ('per_page', 30)]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/api/articles/me/published',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_unpublished_articles(client):
    """Test case for get_user_unpublished_articles

    User's unpublished articles
    """
    params = [('page', 1),
                    ('per_page', 30)]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/api/articles/me/unpublished',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_unpublish_article(client):
    """Test case for unpublish_article

    Unpublish an article
    """
    params = [('note', 'Admin requested unpublishing all articles via API')]
    headers = { 
        'Accept': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/api/articles/{id}/unpublish'.format(id=1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_article(client):
    """Test case for update_article

    Update an article by id
    """
    body = {"article":{"body_markdown":"body_markdown","main_image":"main_image","series":"series","organization_id":0,"description":"description","published":False,"canonical_url":"canonical_url","title":"title","tags":"tags"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api-key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/api/articles/{id}'.format(id=123),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_videos_0(client):
    """Test case for videos_0

    Articles with a video
    """
    params = [('page', 1),
                    ('per_page', 24)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/api/videos',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

