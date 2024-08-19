# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_trigger_request import CreateTriggerRequest
from openapi_server.models.trigger import Trigger


pytestmark = pytest.mark.asyncio

async def test_all_triggers(client):
    """Test case for all_triggers

    All triggers for current user
    """
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{username}/triggers'.format(username='username_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_trigger(client):
    """Test case for create_trigger

    Create a new Trigger
    """
    trigger = openapi_server.CreateTriggerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/{username}/triggers'.format(username='username_example'),
        headers=headers,
        json=trigger,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destroy_trigger(client):
    """Test case for destroy_trigger

    Delete an existing Trigger
    """
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/{username}/triggers/{id}'.format(username='username_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_trigger(client):
    """Test case for get_trigger

    Returns Trigger based on ID
    """
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{username}/triggers/{id}'.format(username='username_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_replace_trigger(client):
    """Test case for replace_trigger

    Replace an existing Trigger
    """
    trigger = openapi_server.CreateTriggerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/{username}/triggers/{id}'.format(username='username_example', id='id_example'),
        headers=headers,
        json=trigger,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_trigger(client):
    """Test case for update_trigger

    Update properties of an existing Trigger
    """
    trigger = openapi_server.CreateTriggerRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/{username}/triggers/{id}'.format(username='username_example', id='id_example'),
        headers=headers,
        json=trigger,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

