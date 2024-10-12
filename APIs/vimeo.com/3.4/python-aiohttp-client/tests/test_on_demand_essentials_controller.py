# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_vod_alt1_request import CreateVodAlt1Request
from openapi_server.models.edit_vod_request import EditVodRequest
from openapi_server.models.legacy_error import LegacyError
from openapi_server.models.on_demand_page import OnDemandPage


pytestmark = pytest.mark.asyncio

async def test_create_vod(client):
    """Test case for create_vod

    Create an On Demand page
    """
    body = openapi_server.CreateVodAlt1Request()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/{user_id}/ondemand/pages'.format(user_id=152184),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_vod_alt1(client):
    """Test case for create_vod_alt1

    Create an On Demand page
    """
    body = openapi_server.CreateVodAlt1Request()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/me/ondemand/pages',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_vod_draft(client):
    """Test case for delete_vod_draft

    Delete a draft of an On Demand page
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.page+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/ondemand/pages/{ondemand_id}'.format(ondemand_id=61326),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_edit_vod(client):
    """Test case for edit_vod

    Edit an On Demand page
    """
    body = openapi_server.EditVodRequest()
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.page+json',
        'Content-Type': 'application/vnd.vimeo.ondemand.page+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/ondemand/pages/{ondemand_id}'.format(ondemand_id=61326),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_vods(client):
    """Test case for get_user_vods

    Get all the On Demand pages of a user
    """
    params = [('direction', 'asc'),
                    ('filter', 'filter_example'),
                    ('page', 1),
                    ('per_page', 10),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.page+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/users/{user_id}/ondemand/pages'.format(user_id=152184),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_user_vods_alt1(client):
    """Test case for get_user_vods_alt1

    Get all the On Demand pages of a user
    """
    params = [('direction', 'asc'),
                    ('filter', 'filter_example'),
                    ('page', 1),
                    ('per_page', 10),
                    ('sort', 'sort_example')]
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.page+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/me/ondemand/pages',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_vod(client):
    """Test case for get_vod

    Get a specific On Demand page
    """
    headers = { 
        'Accept': 'application/vnd.vimeo.ondemand.page+json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/ondemand/pages/{ondemand_id}'.format(ondemand_id=61326),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

