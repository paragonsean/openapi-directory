# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.government_department import GovernmentDepartment
from openapi_server.models.government_opposition_post_item import GovernmentOppositionPostItem
from openapi_server.models.member_item import MemberItem
from openapi_server.models.post_type import PostType


pytestmark = pytest.mark.asyncio

async def test_api_posts_departments_type_get(client):
    """Test case for api_posts_departments_type_get

    Returns a list of departments.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Posts/Departments/{type}'.format(type=openapi_server.PostType()),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_posts_government_posts_get(client):
    """Test case for api_posts_government_posts_get

    Returns a list of government posts.
    """
    params = [('departmentId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Posts/GovernmentPosts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_posts_opposition_posts_get(client):
    """Test case for api_posts_opposition_posts_get

    Returns a list of opposition posts.
    """
    params = [('departmentId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Posts/OppositionPosts',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_posts_speaker_and_deputies_for_date_get(client):
    """Test case for api_posts_speaker_and_deputies_for_date_get

    Returns a list containing the speaker and deputy speakers.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Posts/SpeakerAndDeputies/{for_date}'.format(for_date='2013-10-20T19:20:30+01:00'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_posts_spokespersons_get(client):
    """Test case for api_posts_spokespersons_get

    Returns a list of spokespersons.
    """
    params = [('partyId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/Posts/Spokespersons',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

