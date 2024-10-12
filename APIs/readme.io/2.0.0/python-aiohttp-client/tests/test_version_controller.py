# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.version import Version


pytestmark = pytest.mark.asyncio

async def test_create_version(client):
    """Test case for create_version

    Create version
    """
    body = {"is_beta":True,"is_deprecated":True,"is_stable":True,"codename":"codename","is_hidden":True,"from":"from","version":"version"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/version',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_version(client):
    """Test case for delete_version

    Delete version
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/version/{version_id}'.format(version_id='version_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_version(client):
    """Test case for get_version

    Get version
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/version/{version_id}'.format(version_id='version_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_versions(client):
    """Test case for get_versions

    Get versions
    """
    headers = { 
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/version',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_version(client):
    """Test case for update_version

    Update version
    """
    body = {"is_beta":True,"is_deprecated":True,"is_stable":True,"codename":"codename","is_hidden":True,"from":"from","version":"version"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/version/{version_id}'.format(version_id='version_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

