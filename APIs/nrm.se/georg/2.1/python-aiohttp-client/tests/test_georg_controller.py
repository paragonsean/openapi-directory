# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.input_part import InputPart


pytestmark = pytest.mark.asyncio

async def test_auto_complete(client):
    """Test case for auto_complete

    Search
    """
    params = [('text', 'text_example'),
                    ('sources', 'sources_example'),
                    ('layers', 'layers_example'),
                    ('countryCode', 'country_code_example'),
                    ('size', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/autocomplete',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_reverse_geo_code(client):
    """Test case for get_reverse_geo_code

    Get reverse geocoding
    """
    params = [('lat', 3.4),
                    ('lng', 3.4)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/reverse',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search(client):
    """Test case for search

    Get geocoding
    """
    params = [('text', 'text_example'),
                    ('sources', 'sources_example'),
                    ('layers', 'layers_example'),
                    ('countryCode', 'country_code_example'),
                    ('size', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/search',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_search_coordinates(client):
    """Test case for search_coordinates

    Search coordinates in different formate
    """
    params = [('coordinates', 'coordinates_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/coordinates',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_file(client):
    """Test case for upload_file

    Batch upload
    """
    params = [('type', 'type_example')]
    headers = { 
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('form_data', None)
    data.add_field('form_data_map', None)
    data.add_field('parts', [openapi_server.InputPart()])
    data.add_field('preamble', 'preamble_example')
    response = await client.request(
        method='POST',
        path='/api/upload',
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

