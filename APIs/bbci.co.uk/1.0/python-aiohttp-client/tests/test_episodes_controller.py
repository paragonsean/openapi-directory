# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_clips(client):
    """Test case for get_clips

    Get Clips
    """
    params = [('rights', web),
                    ('availability', available)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/clips/{pid}'.format(pid='pid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_episodes_by_category(client):
    """Test case for get_episodes_by_category

    List all the episodes for a category.
    """
    params = [('lang', 'lang_example'),
                    ('rights', web),
                    ('availability', available),
                    ('page', 56),
                    ('per_page', 56),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/categories/{category}/episodes'.format(category='category_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_episodes_by_group(client):
    """Test case for get_episodes_by_group

    Get episodes by group, brand or series
    """
    params = [('rights', web),
                    ('page', 56),
                    ('per_page', 56),
                    ('initial_child_count', 4),
                    ('sort', 'sort_example'),
                    ('sort_direction', 'sort_direction_example'),
                    ('availability', available),
                    ('mixin', ['mixin_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/groups/{pid}/episodes'.format(pid='pid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_episodes_by_parent_pid(client):
    """Test case for get_episodes_by_parent_pid

    Child episodes for a given programme pid.
    """
    params = [('rights', web),
                    ('availability', available),
                    ('initial_child_count', 4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/programmes/{pid}/episodes'.format(pid='pid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_onward_journey(client):
    """Test case for get_onward_journey

    Get Onward Journey
    """
    params = [('rights', web),
                    ('availability', available)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/episodes/{pid}/next'.format(pid='pid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_post_rolls(client):
    """Test case for get_post_rolls

    Get Follow-ups (post-rolls)
    """
    params = [('rights', web),
                    ('availability', available)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/episodes/{pid}/postrolls'.format(pid='pid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_programme_by_pid(client):
    """Test case for get_programme_by_pid

    Episode for a given pid.
    """
    params = [('rights', web),
                    ('availability', available),
                    ('mixin', ['mixin_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/episodes/{pid}'.format(pid='pid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_programme_recommendations(client):
    """Test case for get_programme_recommendations

    Get programme recommendations
    """
    params = [('rights', web),
                    ('availability', available),
                    ('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/episodes/{pid}/recommendations'.format(pid='pid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_programmes_popular(client):
    """Test case for get_programmes_popular

    Get programmes popular
    """
    params = [('rights', web),
                    ('page', 56),
                    ('per_page', 56),
                    ('initial_child_count', 4),
                    ('sort', 'sort_example'),
                    ('sort_direction', 'sort_direction_example'),
                    ('availability', available),
                    ('mixin', ['mixin_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/groups/popular/episodes',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_trailers_pre_rolls(client):
    """Test case for get_trailers_pre_rolls

    Get Trailers (pre-rolls)
    """
    params = [('rights', web),
                    ('availability', available)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/episodes/{pid}/prerolls'.format(pid='pid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

