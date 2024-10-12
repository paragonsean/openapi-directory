# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.flat_error_response import FlatErrorResponse
from openapi_server.models.group_details import GroupDetails
from openapi_server.models.score_details import ScoreDetails
from openapi_server.models.user_public import UserPublic


pytestmark = pytest.mark.asyncio

async def test_get_group_details(client):
    """Test case for get_group_details

    Get group information
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/groups/{group}'.format(group='group_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_group_scores(client):
    """Test case for get_group_scores

    List group's scores
    """
    params = [('parent', 'parent_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/groups/{group}/scores'.format(group='group_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_group_users(client):
    """Test case for list_group_users

    List group's users
    """
    params = [('source', 'source_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/groups/{group}/users'.format(group='group_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

