# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_secret200_response import AddSecret200Response
from openapi_server.models.delete_secret200_response import DeleteSecret200Response
from openapi_server.models.get_all_secrets200_response import GetAllSecrets200Response
from openapi_server.models.get_secret200_response import GetSecret200Response
from openapi_server.models.secrets import Secrets
from openapi_server.models.update_secret200_response import UpdateSecret200Response


pytestmark = pytest.mark.asyncio

async def test_add_secret(client):
    """Test case for add_secret

    Create a secret
    """
    body = openapi_server.Secrets()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/rudder/api/latest/secret',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_secret(client):
    """Test case for delete_secret

    Delete a secret
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rudder/api/latest/secret/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_all_secrets(client):
    """Test case for get_all_secrets

    List all secrets
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/secret',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_secret(client):
    """Test case for get_secret

    Get one secret
    """
    headers = { 
        'Accept': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/rudder/api/latest/secret/{name}'.format(name='name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_secret(client):
    """Test case for update_secret

    Update a secret
    """
    body = openapi_server.Secrets()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'API-Tokens': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/rudder/api/latest/secret',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

