# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_calendars_all_dvd_start_date_days_get(client):
    """Test case for calendars_all_dvd_start_date_days_get

    Get DVD releases
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/calendars/all/dvd/{start_date}/{days}'.format(start_date='2014-09-01', days=7),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendars_all_movies_start_date_days_get(client):
    """Test case for calendars_all_movies_start_date_days_get

    Get movies
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/calendars/all/movies/{start_date}/{days}'.format(start_date='2014-09-01', days=7),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendars_all_shows_new_start_date_days_get(client):
    """Test case for calendars_all_shows_new_start_date_days_get

    Get new shows
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/calendars/all/shows/new/{start_date}/{days}'.format(start_date='2014-09-01', days=7),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendars_all_shows_premieres_start_date_days_get(client):
    """Test case for calendars_all_shows_premieres_start_date_days_get

    Get season premieres
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/calendars/all/shows/premieres/{start_date}/{days}'.format(start_date='2014-09-01', days=7),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_calendars_all_shows_start_date_days_get(client):
    """Test case for calendars_all_shows_start_date_days_get

    Get shows
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
    }
    response = await client.request(
        method='GET',
        path='/calendars/all/shows/{start_date}/{days}'.format(start_date='2014-09-01', days=7),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_dvd_releases(client):
    """Test case for get_dvd_releases

    Get DVD releases
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/calendars/my/dvd/{start_date}/{days}'.format(start_date='2014-09-01', days=7),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_movies(client):
    """Test case for get_movies

    Get movies
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/calendars/my/movies/{start_date}/{days}'.format(start_date='2014-09-01', days=7),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_new_shows(client):
    """Test case for get_new_shows

    Get new shows
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/calendars/my/shows/new/{start_date}/{days}'.format(start_date='2014-09-01', days=7),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_season_premieres(client):
    """Test case for get_season_premieres

    Get season premieres
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/calendars/my/shows/premieres/{start_date}/{days}'.format(start_date='2014-09-01', days=7),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_shows(client):
    """Test case for get_shows

    Get shows
    """
    headers = { 
        'Accept': 'application/json',
        'trakt_api_version': '2',
        'trakt_api_key': '[client_id]',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/calendars/my/shows/{start_date}/{days}'.format(start_date='2014-09-01', days=7),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

