# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.collection import Collection
from openapi_server.models.collection_data_list import CollectionDataList
from openapi_server.models.collection_item_data_list import CollectionItemDataList
from openapi_server.models.contributor_profile import ContributorProfile
from openapi_server.models.contributor_profile_data_list import ContributorProfileDataList


pytestmark = pytest.mark.asyncio

async def test_get_contributor(client):
    """Test case for get_contributor

    Get details about a single contributor
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/contributors/{contributor_id}'.format(contributor_id='1653538'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contributor_collection_items(client):
    """Test case for get_contributor_collection_items

    Get the items in contributors' collections
    """
    params = [('page', 1),
                    ('per_page', 20),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/contributors/{contributor_id}/collections/{id}/items'.format(contributor_id='800506', id='1991678'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contributor_collections(client):
    """Test case for get_contributor_collections

    Get details about contributors' collections
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/contributors/{contributor_id}/collections/{id}'.format(contributor_id='800506', id='1991678'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contributor_collections_list(client):
    """Test case for get_contributor_collections_list

    List contributors' collections
    """
    params = [('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/contributors/{contributor_id}/collections'.format(contributor_id='800506'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_contributor_list(client):
    """Test case for get_contributor_list

    Get details about multiple contributors
    """
    params = [('id', ['[800506,1653538]'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/contributors',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

