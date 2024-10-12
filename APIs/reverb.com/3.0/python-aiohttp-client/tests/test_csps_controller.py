# coding: utf-8

import pytest
import json
from aiohttp import web



pytestmark = pytest.mark.asyncio

async def test_csps_categories_get(client):
    """Test case for csps_categories_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/csps/categories',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_csps_find_get(client):
    """Test case for csps_find_get

    Show comparison shopping page
    """
    params = [('id', 'id_example'),
                    ('slug', 'slug_example')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/csps/find',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_csps_get(client):
    """Test case for csps_get

    Returns a set of comparison shopping pages based on the current params
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/csps',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_csps_id_get(client):
    """Test case for csps_id_get

    
    """
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/api/csps/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

