# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_get_broadcasts_by_channel(client):
    """Test case for get_broadcasts_by_channel

    Get broadcasts by channel
    """
    params = [('lang', 'lang_example'),
                    ('rights', web),
                    ('availability', available),
                    ('mixin', ['mixin_example']),
                    ('per_page', 56),
                    ('from', '_from_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/channels/{channel}/broadcasts'.format(channel='channel_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_highlights_by_category(client):
    """Test case for get_highlights_by_category

    List the highlights for a category.
    """
    params = [('lang', 'lang_example'),
                    ('rights', web),
                    ('availability', available),
                    ('mixin', ['mixin_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/categories/{category}/highlights'.format(category='category_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_programme_highlights(client):
    """Test case for get_programme_highlights

    Get programme highlights
    """
    params = [('lang', 'lang_example'),
                    ('rights', web),
                    ('availability', available),
                    ('mixin', ['mixin_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/home/highlights',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_programmes_by_category(client):
    """Test case for get_programmes_by_category

    List all the programmes for a category.
    """
    params = [('lang', 'lang_example'),
                    ('rights', web),
                    ('availability', available),
                    ('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/categories/{category}/programmes'.format(category='category_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_programmes_by_channel(client):
    """Test case for get_programmes_by_channel

    Get programmes by channel
    """
    params = [('lang', 'lang_example'),
                    ('rights', web),
                    ('availability', available),
                    ('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/channels/{channel}/programmes'.format(channel='channel_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_programmes_by_parent_pid(client):
    """Test case for get_programmes_by_parent_pid

    Programme for a given pid.
    """
    params = [('rights', web),
                    ('availability', available),
                    ('initial_child_count', 4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ibl/v1/programmes/{pid}'.format(pid='pid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

