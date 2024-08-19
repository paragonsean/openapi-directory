# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.claims import Claims
from openapi_server.models.error import Error
from openapi_server.models.jwt1 import JWT1
from openapi_server.models.key_bind200_response import KeyBind200Response
from openapi_server.models.key_revoke200_response import KeyRevoke200Response
from openapi_server.models.sign_request201_response import SignRequest201Response
from openapi_server.models.sign_update200_response import SignUpdate200Response


pytestmark = pytest.mark.asyncio

async def test_sign_confirm(client):
    """Test case for sign_confirm

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/scope/{job}'.format(job='job_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sign_delete(client):
    """Test case for sign_delete

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/scope/{job}'.format(job='job_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/jwt not supported by Connexion")
async def test_sign_request(client):
    """Test case for sign_request

    
    """
    body = openapi_server.Claims()
    params = [('test', 56)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/jwt',
    }
    response = await client.request(
        method='POST',
        path='/scope',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sign_retrieve(client):
    """Test case for sign_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/scope/{job}'.format(job='job_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sign_retrieve_head(client):
    """Test case for sign_retrieve_head

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='HEAD',
        path='/scope/{job}'.format(job='job_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sign_update(client):
    """Test case for sign_update

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='PUT',
        path='/scope/{job}'.format(job='job_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

