# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.admin_mappings_find_by_metadata_post_request import AdminMappingsFindByMetadataPostRequest
from openapi_server.models.admin_mappings_get200_response import AdminMappingsGet200Response
from openapi_server.models.admin_mappings_get200_response_mappings_inner import AdminMappingsGet200ResponseMappingsInner


pytestmark = pytest.mark.asyncio

async def test_admin_mappings_delete(client):
    """Test case for admin_mappings_delete

    Delete all stub mappings
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/__admin/mappings',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_mappings_find_by_metadata_post(client):
    """Test case for admin_mappings_find_by_metadata_post

    
    """
    body = {"matchesJsonPath":{"equalToJson":"{ \"inner\": 42 }","expression":"$.outer"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/__admin/mappings/find-by-metadata',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_mappings_get(client):
    """Test case for admin_mappings_get

    Get all stub mappings
    """
    params = [('limit', 10),
                    ('offset', 0)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/__admin/mappings',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_mappings_import_post(client):
    """Test case for admin_mappings_import_post

    Import stub mappings
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/__admin/mappings/import',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_mappings_post(client):
    """Test case for admin_mappings_post

    Create a new stub mapping
    """
    body = {"request":{"method":"GET","url":"/some/thing"},"response":{"body":"Hello world!","headers":{"Content-Type":"text/plain"},"status":200}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/__admin/mappings',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_mappings_remove_by_metadata_post(client):
    """Test case for admin_mappings_remove_by_metadata_post

    Delete stub mappings matching metadata
    """
    body = {"matchesJsonPath":{"equalToJson":"{ \"inner\": 42 }","expression":"$.outer"}}
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/__admin/mappings/remove-by-metadata',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_mappings_reset_post(client):
    """Test case for admin_mappings_reset_post

    Reset stub mappings
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/__admin/mappings/reset',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_mappings_save_post(client):
    """Test case for admin_mappings_save_post

    Persist stub mappings
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/__admin/mappings/save',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_mappings_stub_mapping_id_delete(client):
    """Test case for admin_mappings_stub_mapping_id_delete

    Delete a stub mapping
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/__admin/mappings/{stub_mapping_id}'.format(stub_mapping_id='730d3e32-d098-4169-a20c-554c3bedce58'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_mappings_stub_mapping_id_get(client):
    """Test case for admin_mappings_stub_mapping_id_get

    Get stub mapping by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/__admin/mappings/{stub_mapping_id}'.format(stub_mapping_id='730d3e32-d098-4169-a20c-554c3bedce58'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_mappings_stub_mapping_id_put(client):
    """Test case for admin_mappings_stub_mapping_id_put

    Update a stub mapping
    """
    body = {"request":{"method":"GET","url":"/some/thing"},"response":{"body":"Hello world!","headers":{"Content-Type":"text/plain"},"status":200}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/__admin/mappings/{stub_mapping_id}'.format(stub_mapping_id='730d3e32-d098-4169-a20c-554c3bedce58'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

