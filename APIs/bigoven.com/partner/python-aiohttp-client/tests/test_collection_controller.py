# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.big_oven_model_api2_collection_info import BigOvenModelAPI2CollectionInfo
from openapi_server.models.big_oven_model_api2_recipe_search_result import BigOvenModelAPI2RecipeSearchResult


pytestmark = pytest.mark.asyncio

async def test_collection_collections(client):
    """Test case for collection_collections

    Get the list of current, seasonal recipe collections. From here, you can use the /collection/{id} endpoint to retrieve the recipes in those collections.
    """
    params = [('test', 'test_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/collections',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_get_collection(client):
    """Test case for collection_get_collection

    Gets a recipe collection. A recipe collection is a curated set of recipes.
    """
    params = [('rpp', 56),
                    ('pg', 56),
                    ('test', True),
                    ('sessionForLogging', 'session_for_logging_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/collection/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collection_get_collection_meta(client):
    """Test case for collection_get_collection_meta

    Gets a recipe collection metadata. A recipe collection is a curated set of recipes.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/collection/{id}/meta'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

