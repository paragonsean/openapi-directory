# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.key_revoke200_response import KeyRevoke200Response
from openapi_server.models.key_revoke_nosecret200_response import KeyRevokeNosecret200Response


pytestmark = pytest.mark.asyncio

async def test_key_revoke_0(client):
    """Test case for key_revoke_0

    
    """
    params = [('secret', 'secret_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/key/{pk}'.format(pk='pk_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_key_revoke_nosecret_0(client):
    """Test case for key_revoke_nosecret_0

    
    """
    params = [('email', 'email_example'),
                    ('phone', 'phone_example'),
                    ('code', 'code_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/key',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sign_delete_0(client):
    """Test case for sign_delete_0

    
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

