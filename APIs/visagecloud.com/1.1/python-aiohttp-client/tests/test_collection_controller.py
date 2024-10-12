# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rest_response import RestResponse


pytestmark = pytest.mark.asyncio

async def test_add_collection2_using_post(client):
    """Test case for add_collection2_using_post

    Create new empty collection with given name
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('collectionName', 'collection_name_example'),
                    ('preload', False),
                    ('evictable', True),
                    ('purposes', ['purposes_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/v1.1/collection/collection',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_add_collection_using_post(client):
    """Test case for add_collection_using_post

    Create new empty collection with given name
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
    }
    data = {
        'access_key': 'access_key_example',
        'secret_key': 'secret_key_example',
        'name': 'name_example',
        'preload': False,
        'evictable': True,
        'purposes': ['purposes_example']
        }
    response = await client.request(
        method='POST',
        path='/rest/v1.1/collection/',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_collection2_using_delete(client):
    """Test case for delete_collection2_using_delete

    Delete existing collection with associated profiles and faces.
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('collectionId', 'collection_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/v1.1/collection/collection',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_collection_using_delete(client):
    """Test case for delete_collection_using_delete

    Delete existing collection with associated profiles and faces.
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/rest/v1.1/collection/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_csv_using_get(client):
    """Test case for export_csv_using_get

    Retrieve collection content for data analysis.
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('collectionId', 'collection_id_example')]
    headers = { 
        'Accept': 'text/plain',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1.1/collection/export/csv',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_collection_profiles_using_get(client):
    """Test case for get_all_collection_profiles_using_get

    Gets all the profiles associated to a collection
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1.1/collection/{id}/profile'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_collections2_using_get(client):
    """Test case for get_all_collections2_using_get

    Retrieve all collections
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1.1/collection/all',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_collections_using_get(client):
    """Test case for get_all_collections_using_get

    Retrieve all collections
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1.1/collection/',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_collection2_using_get(client):
    """Test case for get_collection2_using_get

    Retrieve existing collection content
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('collectionId', 'collection_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1.1/collection/collection',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_collection_using_get(client):
    """Test case for get_collection_using_get

    Retrieve existing collection content
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/v1.1/collection/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_repurpose_collection_using_put(client):
    """Test case for repurpose_collection_using_put

    Change purpose of existing collection
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('collectionId', 'collection_id_example'),
                    ('purposes', ['purposes_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/rest/v1.1/collection/purpose',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_collection2_using_post(client):
    """Test case for update_collection2_using_post

    Update an existing collection with a given id
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('name', 'name_example'),
                    ('purposes', ['purposes_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/rest/v1.1/collection/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_collection_using_patch(client):
    """Test case for update_collection_using_patch

    Update an existing collection with a given id
    """
    params = [('accessKey', 'access_key_example'),
                    ('secretKey', 'secret_key_example'),
                    ('name', 'name_example'),
                    ('purposes', ['purposes_example'])]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/rest/v1.1/collection/{id}'.format(id='id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

