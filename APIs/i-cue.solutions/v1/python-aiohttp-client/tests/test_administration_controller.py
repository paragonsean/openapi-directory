# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.entity_response import EntityResponse
from openapi_server.models.json_forecast_response import JsonForecastResponse
from openapi_server.models.method_dto import MethodDto
from openapi_server.models.new_entity_request import NewEntityRequest
from openapi_server.models.new_model_request import NewModelRequest
from openapi_server.models.new_token_request import NewTokenRequest
from openapi_server.models.new_user_request import NewUserRequest
from openapi_server.models.toggle_request import ToggleRequest
from openapi_server.models.toggle_user_request import ToggleUserRequest


pytestmark = pytest.mark.asyncio

async def test_administration_entity_get(client):
    """Test case for administration_entity_get

    Get all organizations
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
    }
    response = await client.request(
        method='GET',
        path='/administration/entity',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_administration_entity_id_delete(client):
    """Test case for administration_entity_id_delete

    Delete organization
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='DELETE',
        path='/administration/entity/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_administration_entity_post(client):
    """Test case for administration_entity_post

    Create organization
    """
    body = {"address":"address","name":"name","email":"email"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/administration/entity',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_administration_entity_put(client):
    """Test case for administration_entity_put

    Pause organization
    """
    body = {"id":0,"isActive":True}
    headers = { 
        'Content-Type': 'application/*+json',
        'token': 'token_example',
    }
    response = await client.request(
        method='PUT',
        path='/administration/entity',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_administration_file_to_json_post(client):
    """Test case for administration_file_to_json_post

    Transform data file to JSON format
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'token': 'token_example',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('periodicity', 56)
    response = await client.request(
        method='POST',
        path='/administration/file-to-json',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_administration_model_entity_id_get(client):
    """Test case for administration_model_entity_id_get

    Get Models for Organization
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
    }
    response = await client.request(
        method='GET',
        path='/administration/model/{entity_id}'.format(entity_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_administration_model_entity_id_post(client):
    """Test case for administration_model_entity_id_post

    Register new forecasting model
    """
    body = {"name":"name","key":"key"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/administration/model/{entity_id}'.format(entity_id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_administration_model_get(client):
    """Test case for administration_model_get

    Get all common Models
    """
    headers = { 
        'Accept': 'application/json',
        'token': 'token_example',
    }
    response = await client.request(
        method='GET',
        path='/administration/model',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_administration_model_post(client):
    """Test case for administration_model_post

    Register new forecasting model
    """
    body = {"name":"name","key":"key"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/administration/model',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_administration_planning_level_entity_id_id_delete(client):
    """Test case for administration_planning_level_entity_id_id_delete

    Delete planning level
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='DELETE',
        path='/administration/planning-level/{entity_id}/{id}'.format(entity_id=56, id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_administration_planning_level_lock_post(client):
    """Test case for administration_planning_level_lock_post

    Lock planning level
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/administration/planning-level/lock',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_administration_token_post(client):
    """Test case for administration_token_post

    Issue a token
    """
    body = {"entityToken":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","userToken":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","expirationDate":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/administration/token',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_administration_user_entity_id_get(client):
    """Test case for administration_user_entity_id_get

    Get all users
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='GET',
        path='/administration/user/{entity_id}'.format(entity_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_administration_user_entity_id_id_delete(client):
    """Test case for administration_user_entity_id_id_delete

    Delete user
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='DELETE',
        path='/administration/user/{entity_id}/{id}'.format(entity_id=56, id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_administration_user_lock_put(client):
    """Test case for administration_user_lock_put

    Lock user
    """
    body = {"entityId":0,"id":6,"isActive":True}
    headers = { 
        'Content-Type': 'application/*+json',
        'token': 'token_example',
    }
    response = await client.request(
        method='PUT',
        path='/administration/user/lock',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_administration_user_post(client):
    """Test case for administration_user_post

    Create user
    """
    body = {"entityToken":"046b6c7f-0b8a-43b9-b35d-6489e6daee91","firstname":"firstname","phone":"phone","isActive":True,"email":"email","lastname":"lastname"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/*+json',
        'token': 'token_example',
    }
    response = await client.request(
        method='POST',
        path='/administration/user',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_administration_user_put(client):
    """Test case for administration_user_put

    Update user
    """
    headers = { 
        'token': 'token_example',
    }
    response = await client.request(
        method='PUT',
        path='/administration/user',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

