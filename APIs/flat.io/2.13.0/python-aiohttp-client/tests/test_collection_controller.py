# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.collection import Collection
from openapi_server.models.collection_creation import CollectionCreation
from openapi_server.models.collection_modification import CollectionModification
from openapi_server.models.flat_error_response import FlatErrorResponse
from openapi_server.models.score_details import ScoreDetails


pytestmark = pytest.mark.asyncio

async def test_add_score_to_collection(client):
    """Test case for add_score_to_collection

    Add a score to the collection
    """
    params = [('sharingKey', 'sharing_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/collections/{collection}/scores/{score}'.format(collection='collection_example', score='score_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_collection(client):
    """Test case for create_collection

    Create a new collection
    """
    body = {"privacy":"private","title":"Jazz scores"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/collections',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_collection(client):
    """Test case for delete_collection

    Delete the collection
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/collections/{collection}'.format(collection='collection_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_score_from_collection(client):
    """Test case for delete_score_from_collection

    Delete a score from the collection
    """
    params = [('sharingKey', 'sharing_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v2/collections/{collection}/scores/{score}'.format(collection='collection_example', score='score_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_collection(client):
    """Test case for edit_collection

    Update a collection's metadata
    """
    body = {"privacy":"private","title":"title"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v2/collections/{collection}'.format(collection='collection_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_collection(client):
    """Test case for get_collection

    Get collection details
    """
    params = [('sharingKey', 'sharing_key_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/collections/{collection}'.format(collection='collection_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_collection_scores(client):
    """Test case for list_collection_scores

    List the scores contained in a collection
    """
    params = [('sharingKey', 'sharing_key_example'),
                    ('sort', 'sort_example'),
                    ('direction', 'direction_example'),
                    ('limit', 25),
                    ('next', 'next_example'),
                    ('previous', 'previous_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/collections/{collection}/scores'.format(collection='collection_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_collections(client):
    """Test case for list_collections

    List the collections
    """
    params = [('parent', 'root'),
                    ('sort', 'sort_example'),
                    ('direction', 'direction_example'),
                    ('limit', 25),
                    ('next', 'next_example'),
                    ('previous', 'previous_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/collections',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_untrash_collection(client):
    """Test case for untrash_collection

    Untrash a collection
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/collections/{collection}/untrash'.format(collection='collection_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

