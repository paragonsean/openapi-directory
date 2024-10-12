# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.scu import Scu


pytestmark = pytest.mark.asyncio

async def test_scus_get(client):
    """Test case for scus_get

    
    """
    params = [('startindex', 0),
                    ('count', 20)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/scus',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scus_id_delete(client):
    """Test case for scus_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/scus/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_scus_id_send_post(client):
    """Test case for scus_id_send_post

    
    """
    imageids = [56]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/scus/{id}/send'.format(id=56),
        headers=headers,
        json=imageids,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_scus_post(client):
    """Test case for scus_post

    
    """
    scu = openapi_server.Scu()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/scus',
        headers=headers,
        json=scu,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

