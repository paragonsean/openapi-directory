# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_current_release_dvds_dvd_lists(client):
    """Test case for current_release_dvds_dvd_lists

    
    """
    params = [('page_limit', '16'),
                    ('page', '1'),
                    ('country', 'us')]
    headers = { 
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/public/v1.0/lists/dvds/current_releases.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_new_release_dvds_dvd_lists(client):
    """Test case for new_release_dvds_dvd_lists

    
    """
    params = [('page_limit', '16'),
                    ('page', '1'),
                    ('country', 'us')]
    headers = { 
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/public/v1.0/lists/dvds/new_releases.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_top_rentals_dvd_lists(client):
    """Test case for top_rentals_dvd_lists

    
    """
    params = [('limit', '10'),
                    ('country', 'us')]
    headers = { 
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/public/v1.0/lists/dvds/top_rentals.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_upcoming_dvds_dvd_lists(client):
    """Test case for upcoming_dvds_dvd_lists

    
    """
    params = [('page_limit', '16'),
                    ('page', '1'),
                    ('country', 'us')]
    headers = { 
        'key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/public/v1.0/lists/dvds/upcoming.json',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

