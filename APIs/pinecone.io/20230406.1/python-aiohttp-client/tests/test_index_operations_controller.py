# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.collection import Collection
from openapi_server.models.collection_definition import CollectionDefinition
from openapi_server.models.index import Index
from openapi_server.models.index_configuration import IndexConfiguration
from openapi_server.models.index_definition import IndexDefinition


pytestmark = pytest.mark.asyncio

async def test_configure_index(client):
    """Test case for configure_index

    Configure index
    """
    body = {"replicas":1,"pod_type":"s1.x1"}
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/databases/{index_name}'.format(index_name='index_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_collection(client):
    """Test case for create_collection

    Create collection
    """
    body = {"name":"example","source":"example"}
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/collections',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_index(client):
    """Test case for create_index

    Create index
    """
    body = {"metric":"euclidean","replicas":1,"name":"example","pod_type":"s1.x1","metadata_config":{"indexed":["hello"]},"pods":1,"dimension":1602,"source_collection":"example"}
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/databases',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_collection(client):
    """Test case for delete_collection

    Delete Collection
    """
    headers = { 
        'Accept': 'text/plain',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/collections/{collection_name}'.format(collection_name='collection_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_index(client):
    """Test case for delete_index

    Delete Index
    """
    headers = { 
        'Accept': 'text/plain',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/databases/{index_name}'.format(index_name='index_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_collection(client):
    """Test case for describe_collection

    Describe collection
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/collections/{collection_name}'.format(collection_name='collection_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_describe_index(client):
    """Test case for describe_index

    Describe index
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/databases/{index_name}'.format(index_name='index_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_collections(client):
    """Test case for list_collections

    List collections
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/collections',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_indexes(client):
    """Test case for list_indexes

    List indexes
    """
    headers = { 
        'Accept': 'application/json',
        'ApiKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/databases',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

