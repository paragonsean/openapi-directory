# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_collection_response import GetCollectionResponse
from openapi_server.models.get_collections_response import GetCollectionsResponse
from openapi_server.models.get_listings_response import GetListingsResponse


pytestmark = pytest.mark.asyncio

async def test_collection_listings_all(client):
    """Test case for collection_listings_all

    List collection listings
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 50)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ecosystems/{ecosystem_id}/collections/{id}/listings'.format(ecosystem_id='ecosystem_id_example', id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_all(client):
    """Test case for collections_all

    List collections
    """
    params = [('cursor', 'cursor_example'),
                    ('limit', 50)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ecosystems/{ecosystem_id}/collections'.format(ecosystem_id='ecosystem_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_collections_one(client):
    """Test case for collections_one

    Get collection
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ecosystems/{ecosystem_id}/collections/{id}'.format(ecosystem_id='ecosystem_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

