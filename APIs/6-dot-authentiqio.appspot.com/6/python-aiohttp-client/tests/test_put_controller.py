# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.authentiq_id import AuthentiqID
from openapi_server.models.error import Error
from openapi_server.models.key_bind200_response import KeyBind200Response
from openapi_server.models.sign_update200_response import SignUpdate200Response


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/jwt not supported by Connexion")
async def test_key_bind_0(client):
    """Test case for key_bind_0

    
    """
    body = openapi_server.AuthentiqID()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/jwt',
    }
    response = await client.request(
        method='PUT',
        path='/key/{pk}'.format(pk='pk_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sign_update_0(client):
    """Test case for sign_update_0

    
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

