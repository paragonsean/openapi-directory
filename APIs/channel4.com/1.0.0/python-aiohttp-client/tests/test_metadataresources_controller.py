# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.atom import Atom


pytestmark = pytest.mark.asyncio

async def test_brand_epg_atom_feed(client):
    """Test case for brand_epg_atom_feed

    Brand EPG Atom Feed
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/{brand_web_safe_title}/epg.atom'.format(brand_web_safe_title='brand_web_safe_title_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_call4o_d_feed(client):
    """Test case for call4o_d_feed

    4oD Feed
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/{brand_web_safe_title}/4od.atom'.format(brand_web_safe_title='brand_web_safe_title_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clip_detail_atom_feed(client):
    """Test case for clip_detail_atom_feed

    Clip Detail Atom Feed
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/{brand_web_safe_title}/videos/{clip_asset_id_ato}'.format(brand_web_safe_title='brand_web_safe_title_example', clip_asset_id='clip_asset_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clips_landing_feed_brand_series_and_episode_levels(client):
    """Test case for clips_landing_feed_brand_series_and_episode_levels

    Clips Landing Feed Brand Series and Episode Levels
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/{brand_web_safe_title}/videos/all.atom'.format(brand_web_safe_title='brand_web_safe_title_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clips_landing_feed_brand_series_and_episode_levels2(client):
    """Test case for clips_landing_feed_brand_series_and_episode_levels2

    Clips Landing Feed Brand Series and Episode Levels(2)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/{brand_web_safe_title}/videos/series-{series_number}.atom'.format(brand_web_safe_title='brand_web_safe_title_example', series_number='series_number_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_clips_landing_feed_brand_series_and_episode_levels3(client):
    """Test case for clips_landing_feed_brand_series_and_episode_levels3

    Clips Landing Feed Brand Series and Episode Levels(3)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/{brand_web_safe_title}/videos/series-{series_number}/episode-{episode_number}.atom'.format(brand_web_safe_title='brand_web_safe_title_example', series_number='series_number_example', episode_number='episode_number_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_coming_soon_feed(client):
    """Test case for coming_soon_feed

    Coming Soon feed
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/coming-soon.atom',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_coming_soon_feed2(client):
    """Test case for coming_soon_feed2

    Coming Soon feed(2)
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/coming-soon/{category_ato}'.format(category='category_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_episode_guide_feed_episode_detail(client):
    """Test case for episode_guide_feed_episode_detail

    Episode Guide Feed Episode Detail
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/{brand_web_safe_title}/episode-guide/series-{series_number}/episode-{episode_number}.atom'.format(brand_web_safe_title='brand_web_safe_title_example', series_number='series_number_example', episode_number='episode_number_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_episode_guide_feed_series_detail(client):
    """Test case for episode_guide_feed_series_detail

    Episode Guide Feed Series Detail
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/{brand_web_safe_title}/episode-guide/series-{series_number}.atom'.format(brand_web_safe_title='brand_web_safe_title_example', series_number='series_number_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_episode_guide_feed_series_landing(client):
    """Test case for episode_guide_feed_series_landing

    Episode Guide Feed Series Landing
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/{brand_web_safe_title}/episode-guide.atom'.format(brand_web_safe_title='brand_web_safe_title_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_hub_feed(client):
    """Test case for hub_feed

    Hub Feed
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/{brand_web_safe_title_ato}'.format(brand_web_safe_title='brand_web_safe_title_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_programme_feed(client):
    """Test case for programme_feed

    Programme Feed
    """
    params = [('platform', 'platform_example')]
    headers = { 
        'Accept': 'application/xml',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/pmlsd/programme/{programme_id_ato}'.format(programme_id='programme_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

