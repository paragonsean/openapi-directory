# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.request_entity import RequestEntity


pytestmark = pytest.mark.asyncio

async def test_delete_requests_id(client):
    """Test case for delete_requests_id

    Delete Request
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/rest/v1/requests/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_requests(client):
    """Test case for get_requests

    List Requests
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('mine', True),
                    ('path', 'path_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/requests',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_requests_folders_path(client):
    """Test case for get_requests_folders_path

    List Requests
    """
    params = [('cursor', 'cursor_example'),
                    ('per_page', 56),
                    ('sort_by', None),
                    ('mine', True)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/rest/v1/requests/folders/{path}'.format(path='path_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_post_requests(client):
    """Test case for post_requests

    Create Request
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
    }
    data = FormData()
    data.add_field('destination', 'destination_example')
    data.add_field('group_ids', 'group_ids_example')
    data.add_field('path', 'path_example')
    data.add_field('user_ids', 'user_ids_example')
    response = await client.request(
        method='POST',
        path='/api/rest/v1/requests',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

