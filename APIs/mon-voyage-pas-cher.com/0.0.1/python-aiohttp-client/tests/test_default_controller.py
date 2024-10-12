# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_airports_options(client):
    """Test case for airports_options

    CORS support
    """
    headers = { 
    }
    response = await client.request(
        method='OPTIONS',
        path='/airports',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cities_findcitiesfromlatlong_options(client):
    """Test case for cities_findcitiesfromlatlong_options

    CORS support
    """
    headers = { 
    }
    response = await client.request(
        method='OPTIONS',
        path='/cities/findcitiesfromlatlong',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cities_findcitiesfromtext_options(client):
    """Test case for cities_findcitiesfromtext_options

    CORS support
    """
    headers = { 
    }
    response = await client.request(
        method='OPTIONS',
        path='/cities/findcitiesfromtext',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cities_significant_options(client):
    """Test case for cities_significant_options

    CORS support
    """
    headers = { 
    }
    response = await client.request(
        method='OPTIONS',
        path='/cities/significant',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_continents_options(client):
    """Test case for continents_options

    CORS support
    """
    headers = { 
    }
    response = await client.request(
        method='OPTIONS',
        path='/continents',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_countries_options(client):
    """Test case for countries_options

    CORS support
    """
    headers = { 
    }
    response = await client.request(
        method='OPTIONS',
        path='/countries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_distance_options(client):
    """Test case for distance_options

    CORS support
    """
    headers = { 
    }
    response = await client.request(
        method='OPTIONS',
        path='/distance',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_elevation_options(client):
    """Test case for elevation_options

    CORS support
    """
    headers = { 
    }
    response = await client.request(
        method='OPTIONS',
        path='/elevation',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sun_positions_options(client):
    """Test case for sun_positions_options

    CORS support
    """
    headers = { 
    }
    response = await client.request(
        method='OPTIONS',
        path='/sun_positions',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_timezone_options(client):
    """Test case for timezone_options

    CORS support
    """
    headers = { 
    }
    response = await client.request(
        method='OPTIONS',
        path='/timezone',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

