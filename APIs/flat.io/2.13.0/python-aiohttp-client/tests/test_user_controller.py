# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.flat_error_response import FlatErrorResponse
from openapi_server.models.score_details import ScoreDetails
from openapi_server.models.user_public import UserPublic


pytestmark = pytest.mark.asyncio

async def test_ger_user_likes(client):
    """Test case for ger_user_likes

    List liked scores
    """
    params = [('ids', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/users/{user}/likes'.format(user='user_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user(client):
    """Test case for get_user

    Get a public user profile
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/users/{user}'.format(user='user_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_scores(client):
    """Test case for get_user_scores

    List user's scores
    """
    params = [('parent', 'parent_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/users/{user}/scores'.format(user='user_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

