# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.collection_creation_result import CollectionCreationResult


pytestmark = pytest.mark.asyncio

async def test_add_to_collection(client):
    """Test case for add_to_collection

    Adds items to a collection.
    """
    params = [('ids', ['ids_example'])]
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Collections/{collection_id}/Items'.format(collection_id='collection_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_collection(client):
    """Test case for create_collection

    Creates a new collection.
    """
    params = [('name', 'name_example'),
                    ('ids', ['ids_example']),
                    ('parentId', 'parent_id_example'),
                    ('isLocked', False)]
    headers = { 
        'Accept': 'application/json',
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/Collections',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_from_collection(client):
    """Test case for remove_from_collection

    Removes items from a collection.
    """
    params = [('ids', ['ids_example'])]
    headers = { 
        'CustomAuthentication': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/Collections/{collection_id}/Items'.format(collection_id='collection_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

