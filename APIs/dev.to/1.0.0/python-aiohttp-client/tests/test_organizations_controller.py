# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.article_index import ArticleIndex
from openapi_server.models.organization import Organization
from openapi_server.models.user import User


pytestmark = pytest.mark.asyncio

async def test_get_org_articles(client):
    """Test case for get_org_articles

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

async def test_get_org_users(client):
    """Test case for get_org_users

    Organization's users
    """
    params = [('page', 1),
                    ('per_page', 30)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/api/organizations/{username}/users'.format(username='username_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_organization(client):
    """Test case for get_organization

    An organization
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/api/organizations/{username}'.format(username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

