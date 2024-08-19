# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.authentiq_id import AuthentiqID
from openapi_server.models.error import Error
from openapi_server.models.jwt import JWT
from openapi_server.models.key_bind200_response import KeyBind200Response
from openapi_server.models.key_register201_response import KeyRegister201Response
from openapi_server.models.key_revoke200_response import KeyRevoke200Response
from openapi_server.models.key_revoke_nosecret200_response import KeyRevokeNosecret200Response


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/jwt not supported by Connexion")
async def test_key_bind(client):
    """Test case for key_bind

    
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

async def test_key_pkhead(client):
    """Test case for key_pkhead

    
    """
    headers = { 
        'Accept': '*/*',
    }
    response = await client.request(
        method='HEAD',
        path='/key/{pk}'.format(pk='pk_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/jwt not supported by Connexion")
async def test_key_register(client):
    """Test case for key_register

    
    """
    body = openapi_server.AuthentiqID()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/jwt',
    }
    response = await client.request(
        method='POST',
        path='/key',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_key_retrieve(client):
    """Test case for key_retrieve

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/key/{pk}'.format(pk='pk_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_key_revoke(client):
    """Test case for key_revoke

    
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

async def test_key_revoke_nosecret(client):
    """Test case for key_revoke_nosecret

    
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

@pytest.mark.skip("application/jwt not supported by Connexion")
async def test_key_update(client):
    """Test case for key_update

    
    """
    body = openapi_server.AuthentiqID()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/jwt',
    }
    response = await client.request(
        method='POST',
        path='/key/{pk}'.format(pk='pk_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

