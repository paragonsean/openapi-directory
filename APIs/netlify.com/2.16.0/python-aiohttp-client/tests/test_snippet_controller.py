# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.snippet import Snippet


pytestmark = pytest.mark.asyncio

async def test_create_site_snippet(client):
    """Test case for create_site_snippet

    
    """
    snippet = openapi_server.Snippet()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/sites/{site_id}/snippets'.format(site_id='site_id_example'),
        headers=headers,
        json=snippet,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_site_snippet(client):
    """Test case for delete_site_snippet

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/sites/{site_id}/snippets/{snippet_id}'.format(site_id='site_id_example', snippet_id='snippet_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_site_snippet(client):
    """Test case for get_site_snippet

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{site_id}/snippets/{snippet_id}'.format(site_id='site_id_example', snippet_id='snippet_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_site_snippets(client):
    """Test case for list_site_snippets

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{site_id}/snippets'.format(site_id='site_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_site_snippet(client):
    """Test case for update_site_snippet

    
    """
    snippet = openapi_server.Snippet()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/sites/{site_id}/snippets/{snippet_id}'.format(site_id='site_id_example', snippet_id='snippet_id_example'),
        headers=headers,
        json=snippet,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

