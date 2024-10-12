# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.changelog import Changelog


pytestmark = pytest.mark.asyncio

async def test_create_changelog(client):
    """Test case for create_changelog

    Create changelog
    """
    body = {"hidden":True,"body":"body","title":"title","type":""}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/changelogs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_changelog(client):
    """Test case for delete_changelog

    Delete changelog
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/changelogs/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_changelog(client):
    """Test case for get_changelog

    Get changelog
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/changelogs/{slug}'.format(slug='slug_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_changelogs(client):
    """Test case for get_changelogs

    Get changelogs
    """
    params = [('perPage', 10),
                    ('page', 1)]
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/changelogs',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_changelog(client):
    """Test case for update_changelog

    Update changelog
    """
    body = {"hidden":True,"body":"body","title":"title","type":""}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/changelogs/{slug}'.format(slug='slug_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

