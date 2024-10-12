# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.filters_api_response import FiltersAPIResponse
from openapi_server.models.meshery_filter import MesheryFilter


pytestmark = pytest.mark.asyncio

async def test_id_delete_meshery_filter(client):
    """Test case for id_delete_meshery_filter

    Handle Delete for a Meshery Filter
    """
    headers = { 
        'token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/filter/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_filter_file(client):
    """Test case for id_get_filter_file

    Handle GET request for all filters
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/filter',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_filter_files(client):
    """Test case for id_get_filter_files

    Handle GET request for filter file with given id
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/filter/file/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_get_meshery_filter(client):
    """Test case for id_get_meshery_filter

    Handle GET request for a Meshery Filter
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/filter/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_id_post_filter_file(client):
    """Test case for id_post_filter_file

    Handle POST requests for Meshery Filters
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/filter',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

