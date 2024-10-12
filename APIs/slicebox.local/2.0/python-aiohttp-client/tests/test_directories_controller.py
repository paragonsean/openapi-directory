# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.watched_directory import WatchedDirectory


pytestmark = pytest.mark.asyncio

async def test_directorywatches_get(client):
    """Test case for directorywatches_get

    
    """
    params = [('startindex', 0),
                    ('count', 20)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/directorywatches',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_directorywatches_id_delete(client):
    """Test case for directorywatches_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/directorywatches/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_directorywatches_post(client):
    """Test case for directorywatches_post

    
    """
    watched_directory = openapi_server.WatchedDirectory()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/directorywatches',
        headers=headers,
        json=watched_directory,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

