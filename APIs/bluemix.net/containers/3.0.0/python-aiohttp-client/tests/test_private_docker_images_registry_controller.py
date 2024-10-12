# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.namespace import Namespace


pytestmark = pytest.mark.asyncio

async def test_registry_namespaces_get(client):
    """Test case for registry_namespaces_get

    Retrieve the namespace of an organization.
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='GET',
        path='/v3/registry/namespaces',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_namespaces_namespace_get(client):
    """Test case for registry_namespaces_namespace_get

    Check the availability of a namespace
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='GET',
        path='/v3/registry/namespaces/{namespace}'.format(namespace='namespace_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_registry_namespaces_namespace_put(client):
    """Test case for registry_namespaces_namespace_put

    Set a namespace for your private Bluemix registry.
    """
    headers = { 
        'Accept': 'application/json',
        'x_auth_token': 'x_auth_token_example',
        'x_auth_project_id': 'x_auth_project_id_example',
    }
    response = await client.request(
        method='PUT',
        path='/v3/registry/namespaces/{namespace}'.format(namespace='namespace_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

