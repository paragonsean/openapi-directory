# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deleted import Deleted
from openapi_server.models.patch_inner import PatchInner
from openapi_server.models.validation_authority import ValidationAuthority


pytestmark = pytest.mark.asyncio

async def test_create_client_validator(client):
    """Test case for create_client_validator

    Create one validation authorities
    """
    body = {"headers":{"key":"value"},"method":"a string value","badTtl":123,"description":"a string value","timeout":123,"url":"a string value","alwaysValid":True,"path":"a string value","noCache":True,"host":"a string value","name":"a string value","goodTtl":123,"id":"a string value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/client-validators',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_client_validator(client):
    """Test case for delete_client_validator

    Delete one validation authorities by id
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/client-validators/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_all_client_validators(client):
    """Test case for find_all_client_validators

    Get all validation authoritiess
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/client-validators',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_client_validator_by_id(client):
    """Test case for find_client_validator_by_id

    Get one validation authorities by id
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/client-validators/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_client_validator(client):
    """Test case for patch_client_validator

    Update one validation authorities by id
    """
    body = [openapi_server.PatchInner()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PATCH',
        path='/api/client-validators/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_client_validator(client):
    """Test case for update_client_validator

    Update one validation authorities by id
    """
    body = {"headers":{"key":"value"},"method":"a string value","badTtl":123,"description":"a string value","timeout":123,"url":"a string value","alwaysValid":True,"path":"a string value","noCache":True,"host":"a string value","name":"a string value","goodTtl":123,"id":"a string value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/client-validators/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

