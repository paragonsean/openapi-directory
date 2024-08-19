# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.rechnungsdruck_web_app_controllers_api_web_hook_api_model import RechnungsdruckWebAppControllersApiWebHookApiModel


pytestmark = pytest.mark.asyncio

async def test_web_hook_management_delete(client):
    """Test case for web_hook_management_delete

    Deletes an existing WebHook registration.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/webhooks/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_hook_management_delete_all(client):
    """Test case for web_hook_management_delete_all

    Deletes all existing WebHook registrations.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/webhooks',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_hook_management_get(client):
    """Test case for web_hook_management_get

    Gets all registered WebHooks for a given user.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/webhooks',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_hook_management_get_filters(client):
    """Test case for web_hook_management_get_filters

    Returns a list of all known filters you can use to register webhooks
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/webhooks/filters',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_hook_management_lookup(client):
    """Test case for web_hook_management_lookup

    Looks up a registered WebHook with the given {id} for a given user.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/webhooks/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_web_hook_management_post(client):
    """Test case for web_hook_management_post

    Registers a new WebHook for a given user.
    """
    body = openapi_server.RechnungsdruckWebAppControllersApiWebHookApiModel()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/webhooks',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_web_hook_management_put(client):
    """Test case for web_hook_management_put

    Updates an existing WebHook registration.
    """
    body = openapi_server.RechnungsdruckWebAppControllersApiWebHookApiModel()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/webhooks/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

