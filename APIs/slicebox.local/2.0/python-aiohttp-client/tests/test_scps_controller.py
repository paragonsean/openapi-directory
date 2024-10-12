# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.scp import Scp


pytestmark = pytest.mark.asyncio

async def test_scps_get(client):
    """Test case for scps_get

    
    """
    params = [('startindex', 0),
                    ('count', 20)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/scps',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_scps_id_delete(client):
    """Test case for scps_id_delete

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/api/scps/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_scps_post(client):
    """Test case for scps_post

    
    """
    scp = openapi_server.Scp()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/scps',
        headers=headers,
        json=scp,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

