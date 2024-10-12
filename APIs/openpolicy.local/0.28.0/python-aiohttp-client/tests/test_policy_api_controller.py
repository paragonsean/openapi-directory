# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_document_with_web_hook200_response import GetDocumentWithWebHook200Response
from openapi_server.models.model200_result import Model200Result
from openapi_server.models.model400 import Model400
from openapi_server.models.model404 import Model404


pytestmark = pytest.mark.asyncio

async def test_delete_policy_module(client):
    """Test case for delete_policy_module

    Delete a policy module
    """
    params = [('pretty', true)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/policies/{id}'.format(id='example1'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_policies(client):
    """Test case for get_policies

    List policies
    """
    params = [('pretty', true)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/policies',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_policy_module(client):
    """Test case for get_policy_module

    Get a policy module
    """
    params = [('pretty', true)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/policies/{id}'.format(id='example1'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_put_policy_module(client):
    """Test case for put_policy_module

    Create or update a policy module
    """
    body = 'body_example'
    params = [('pretty', true),
                    ('metrics', false)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/plain',
    }
    response = await client.request(
        method='PUT',
        path='/v1/policies/{id}'.format(id='example1'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

