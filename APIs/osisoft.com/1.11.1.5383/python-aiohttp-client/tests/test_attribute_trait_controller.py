# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.attribute_trait import AttributeTrait
from openapi_server.models.items_attribute_trait import ItemsAttributeTrait


pytestmark = pytest.mark.asyncio

async def test_attribute_trait_get(client):
    """Test case for attribute_trait_get

    Retrieve an attribute trait.
    """
    params = [('selectedFields', 'selected_fields_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/attributetraits/{name}'.format(name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_attribute_trait_get_by_category(client):
    """Test case for attribute_trait_get_by_category

    Retrieve all attribute traits of the specified category/categories.
    """
    params = [('category', ['category_example']),
                    ('selectedFields', 'selected_fields_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/piwebapi/attributetraits',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

