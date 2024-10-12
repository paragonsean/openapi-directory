# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.block import Block
from openapi_server.models.create_block_request import CreateBlockRequest


pytestmark = pytest.mark.asyncio

async def test_all_blocks(client):
    """Test case for all_blocks

    All blocks for current user
    """
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{username}/dashboards/{dashboard_id}/blocks'.format(username='username_example', dashboard_id='dashboard_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_block(client):
    """Test case for create_block

    Create a new Block
    """
    block = openapi_server.CreateBlockRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/{username}/dashboards/{dashboard_id}/blocks'.format(username='username_example', dashboard_id='dashboard_id_example'),
        headers=headers,
        json=block,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_destroy_block(client):
    """Test case for destroy_block

    Delete an existing Block
    """
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v2/{username}/dashboards/{dashboard_id}/blocks/{id}'.format(username='username_example', dashboard_id='dashboard_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_block(client):
    """Test case for get_block

    Returns Block based on ID
    """
    headers = { 
        'Accept': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/{username}/dashboards/{dashboard_id}/blocks/{id}'.format(username='username_example', dashboard_id='dashboard_id_example', id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_replace_block(client):
    """Test case for replace_block

    Replace an existing Block
    """
    block = openapi_server.CreateBlockRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v2/{username}/dashboards/{dashboard_id}/blocks/{id}'.format(username='username_example', dashboard_id='dashboard_id_example', id='id_example'),
        headers=headers,
        json=block,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_block(client):
    """Test case for update_block

    Update properties of an existing Block
    """
    block = openapi_server.CreateBlockRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'HeaderSignature': 'special-key',
        'QueryKey': 'special-key',
        'HeaderKey': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/api/v2/{username}/dashboards/{dashboard_id}/blocks/{id}'.format(username='username_example', dashboard_id='dashboard_id_example', id='id_example'),
        headers=headers,
        json=block,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

