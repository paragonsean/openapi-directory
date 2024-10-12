# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.image import Image
from openapi_server.models.images_post_request import ImagesPostRequest
from openapi_server.models.import_session import ImportSession


pytestmark = pytest.mark.asyncio

async def test_import_sessions_get(client):
    """Test case for import_sessions_get

    
    """
    params = [('startindex', 0),
                    ('count', 20)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/import/sessions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_import_sessions_id_delete(client):
    """Test case for import_sessions_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/import/sessions/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_import_sessions_id_get(client):
    """Test case for import_sessions_id_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/import/sessions/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_import_sessions_id_images_get(client):
    """Test case for import_sessions_id_images_get

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/import/sessions/{id}/images'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_import_sessions_id_images_post(client):
    """Test case for import_sessions_id_images_post

    
    """
    body = openapi_server.ImagesPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/import/sessions/{id}/images'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_import_sessions_post(client):
    """Test case for import_sessions_post

    
    """
    import_session = openapi_server.ImportSession()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/import/sessions',
        headers=headers,
        json=import_session,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

