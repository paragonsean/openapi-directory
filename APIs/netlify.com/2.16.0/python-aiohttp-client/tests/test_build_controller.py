# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.build import Build
from openapi_server.models.build_setup import BuildSetup
from openapi_server.models.build_status import BuildStatus
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_create_site_build(client):
    """Test case for create_site_build

    
    """
    build = openapi_server.BuildSetup()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sites/{site_id}/builds'.format(site_id='site_id_example'),
        headers=headers,
        json=build,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_account_build_status(client):
    """Test case for get_account_build_status

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/{account_id}/builds/status'.format(account_id='account_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_site_build(client):
    """Test case for get_site_build

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/builds/{build_id}'.format(build_id='build_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_site_builds(client):
    """Test case for list_site_builds

    
    """
    params = [('page', 56),
                    ('per_page', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{site_id}/builds'.format(site_id='site_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_notify_build_start(client):
    """Test case for notify_build_start

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/builds/{build_id}/start'.format(build_id='build_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

