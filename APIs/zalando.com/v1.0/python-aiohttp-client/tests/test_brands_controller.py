# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.brand import Brand
from openapi_server.models.brands import Brands
from openapi_server.models.error_message import ErrorMessage


pytestmark = pytest.mark.asyncio

async def test_brands_get(client):
    """Test case for brands_get

    Shop Brands
    """
    params = [('key', ['key_example']),
                    ('name', ['name_example']),
                    ('brandFamilyName', ['brand_family_name_example']),
                    ('brandFamilyKey', ['brand_family_key_example']),
                    ('page', 'page_example'),
                    ('pageSize', 'page_size_example'),
                    ('fields', ['fields_example'])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
    }
    response = await client.request(
        method='GET',
        path='/brands',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_brands_key_get(client):
    """Test case for brands_key_get

    Get Single Brand by Key
    """
    params = [('fields', ['fields_example'])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
    }
    response = await client.request(
        method='GET',
        path='/brands/{key}'.format(key='key_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

