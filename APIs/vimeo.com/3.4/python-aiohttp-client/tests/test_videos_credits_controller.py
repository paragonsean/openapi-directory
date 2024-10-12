# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_video_credit_alt1_request import AddVideoCreditAlt1Request
from openapi_server.models.credit import Credit
from openapi_server.models.edit_video_credit_request import EditVideoCreditRequest
from openapi_server.models.legacy_error import LegacyError


pytestmark = pytest.mark.asyncio

async def test_add_video_credit(client):
    """Test case for add_video_credit

    Credit a user in a video
    """
    body = openapi_server.AddVideoCreditAlt1Request()
    headers = { 
        'Accept': 'application/vnd.vimeo.credit+json',
        'Content-Type': 'application/vnd.vimeo.credit+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/videos/{video_id}/credits'.format(video_id=258684937),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_video_credit_alt1(client):
    """Test case for add_video_credit_alt1

    Credit a user in a video
    """
    body = openapi_server.AddVideoCreditAlt1Request()
    headers = { 
        'Accept': 'application/vnd.vimeo.credit+json',
        'Content-Type': 'application/vnd.vimeo.credit+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/channels/{channel_id}/videos/{video_id}/credits'.format(channel_id=927, video_id=258684937),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_video_credit(client):
    """Test case for delete_video_credit

    Delete a credit for a user in a video
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/videos/{video_id}/credits/{credit_id}'.format(credit_id=12345, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_video_credit(client):
    """Test case for edit_video_credit

    Edit a credit for a user in a video
    """
    body = openapi_server.EditVideoCreditRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.credit+json',
        'Content-Type': 'application/vnd.vimeo.credit+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/videos/{video_id}/credits/{credit_id}'.format(credit_id=12345, video_id=258684937),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_video_credit(client):
    """Test case for get_video_credit

    Get a specific credited user in a video
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.credit+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/videos/{video_id}/credits/{credit_id}'.format(credit_id=12345, video_id=258684937),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_video_credits(client):
    """Test case for get_video_credits

    Get all the credited users in a video
    """
    params = [('direction', 'asc'),
                    ('page', 1),
                    ('per_page', 10),
                    ('query', 'Stop motion'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.credit+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/videos/{video_id}/credits'.format(video_id=258684937),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_video_credits_alt1(client):
    """Test case for get_video_credits_alt1

    Get all the credited users in a video
    """
    params = [('direction', 'asc'),
                    ('page', 1),
                    ('per_page', 10),
                    ('query', 'Stop motion'),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.credit+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/channels/{channel_id}/videos/{video_id}/credits'.format(channel_id=927, video_id=258684937),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

