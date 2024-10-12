# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.admin_mappings_find_by_metadata_post_request import AdminMappingsFindByMetadataPostRequest
from openapi_server.models.admin_mappings_get200_response_mappings_inner_request import AdminMappingsGet200ResponseMappingsInnerRequest
from openapi_server.models.admin_requests_count_post200_response import AdminRequestsCountPost200Response


pytestmark = pytest.mark.asyncio

async def test_admin_requests_count_post(client):
    """Test case for admin_requests_count_post

    Count requests by criteria
    """
    body = {"headers":{"Content-Type":{"matches":".*/xml"}},"method":"POST","url":"/resource"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/__admin/requests/count',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_requests_delete(client):
    """Test case for admin_requests_delete

    Delete all requests in journal
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/__admin/requests',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_requests_find_post(client):
    """Test case for admin_requests_find_post

    Find requests by criteria
    """
    body = {"headers":{"Content-Type":{"matches":".*/xml"}},"method":"POST","url":"/resource"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/__admin/requests/find',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_requests_get(client):
    """Test case for admin_requests_get

    Get all requests in journal
    """
    params = [('limit', '10'),
                    ('since', '2016-10-05T12:33:01.000Z')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/__admin/requests',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_requests_remove_by_metadata_post(client):
    """Test case for admin_requests_remove_by_metadata_post

    Delete requests mappings matching metadata
    """
    body = {"matchesJsonPath":{"equalToJson":"{ \"inner\": 42 }","expression":"$.outer"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/__admin/requests/remove-by-metadata',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_requests_remove_post(client):
    """Test case for admin_requests_remove_post

    Remove requests by criteria
    """
    body = {"headers":{"Content-Type":{"matches":".*/xml"}},"method":"POST","url":"/resource"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/__admin/requests/remove',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_requests_request_id_delete(client):
    """Test case for admin_requests_request_id_delete

    Delete request by ID
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/__admin/requests/{request_id}'.format(request_id='12fb14bb-600e-4bfa-bd8d-be7f12562c99'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_requests_request_id_get(client):
    """Test case for admin_requests_request_id_get

    Get request by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/__admin/requests/{request_id}'.format(request_id='12fb14bb-600e-4bfa-bd8d-be7f12562c99'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_requests_reset_post(client):
    """Test case for admin_requests_reset_post

    Empty the request journal
    """
    headers = { 
    }
    response = await client.request(
        method='POST',
        path='/__admin/requests/reset',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_admin_requests_unmatched_get(client):
    """Test case for admin_requests_unmatched_get

    Find unmatched requests
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/__admin/requests/unmatched',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

