# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_host201_response import CreateHost201Response
from openapi_server.models.create_token200_response_inner import CreateToken200ResponseInner


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_host(client):
    """Test case for create_host

    Creates a Host using the Host Factory.
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_request_id': 'test-id',
        'conjurAuth': 'special-key',
    }
    data = {
        'annotations': None,
        'id': 'id_example'
        }
    response = await client.request(
        method='POST',
        path='/host_factories/hosts',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-www-form-urlencoded not supported by Connexion")
async def test_create_token(client):
    """Test case for create_token

    Creates one or more host identity tokens.
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-www-form-urlencoded',
        'x_request_id': 'test-id',
        'conjurAuth': 'special-key',
    }
    data = {
        'cidr': ['cidr_example'],
        'count': 56,
        'expiration': 'expiration_example',
        'host_factory': 'host_factory_example'
        }
    response = await client.request(
        method='POST',
        path='/host_factory_tokens',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_revoke_token(client):
    """Test case for revoke_token

    Revokes a token, immediately disabling it.
    """
    headers = { 
        'x_request_id': 'test-id',
        'conjurAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/host_factory_tokens/{token}'.format(token='2c0vfj61pmah3efbgpcz2x9vzcy1ycskfkyqy0kgk1fv014880f4'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

