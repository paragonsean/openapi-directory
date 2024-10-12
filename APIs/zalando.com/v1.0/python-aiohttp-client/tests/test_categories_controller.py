# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.categories import Categories
from openapi_server.models.category import Category
from openapi_server.models.error_message import ErrorMessage


pytestmark = pytest.mark.asyncio

async def test_categories_get(client):
    """Test case for categories_get

    Shop Categories
    """
    params = [('name', ['name_example']),
                    ('type', 'type_example'),
                    ('outlet', 'outlet_example'),
                    ('hidden', 'hidden_example'),
                    ('targetGroup', 'target_group_example'),
                    ('key', ['key_example']),
                    ('parentKey', ['parent_key_example']),
                    ('childKey', ['child_key_example']),
                    ('suggestedFilter', ['suggested_filter_example']),
                    ('page', 'page_example'),
                    ('pageSize', 'page_size_example'),
                    ('fields', ['fields_example'])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
    }
    response = await client.request(
        method='GET',
        path='/categories',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_categories_key_get(client):
    """Test case for categories_key_get

    Get Single Category by Key
    """
    params = [('fields', ['fields_example'])]
    headers = { 
        'Accept': 'application/json',
        'accept_language': 'accept_language_example',
    }
    response = await client.request(
        method='GET',
        path='/categories/{key}'.format(key=['key_example']),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

