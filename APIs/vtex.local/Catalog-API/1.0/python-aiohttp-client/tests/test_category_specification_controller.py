# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.category_specification_inner import CategorySpecificationInner


pytestmark = pytest.mark.asyncio

async def test_specifications_by_category_id(client):
    """Test case for specifications_by_category_id

    Get Specifications By Category ID
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pub/specification/field/listByCategoryId/{category_id}'.format(category_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_specifications_tree_by_category_id(client):
    """Test case for specifications_tree_by_category_id

    Get Specifications Tree By Category ID
    """
    headers = { 
        'Accept': 'application/json',
        'content_type': 'application/json',
        'accept': 'application/json',
        'appToken': 'special-key',
        'appKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/catalog_system/pub/specification/field/listTreeByCategoryId/{category_id}'.format(category_id=1),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

