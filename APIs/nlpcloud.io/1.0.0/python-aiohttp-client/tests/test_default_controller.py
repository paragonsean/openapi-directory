# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dependencies_out import DependenciesOut
from openapi_server.models.entities_out import EntitiesOut
from openapi_server.models.http_validation_error import HTTPValidationError
from openapi_server.models.sentence_dependencies_out import SentenceDependenciesOut
from openapi_server.models.user_request_in import UserRequestIn
from openapi_server.models.version_out import VersionOut


pytestmark = pytest.mark.asyncio

async def test_read_dependencies_v1_en_core_web_sm_dependencies_post(client):
    """Test case for read_dependencies_v1_en_core_web_sm_dependencies_post

    Read Dependencies
    """
    body = {"text":"text"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/en_core_web_sm/dependencies',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_entities_v1_en_core_web_sm_entities_post(client):
    """Test case for read_entities_v1_en_core_web_sm_entities_post

    Read Entities
    """
    body = {"text":"text"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/en_core_web_sm/entities',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_root_v1_en_core_web_sm_get(client):
    """Test case for read_root_v1_en_core_web_sm_get

    Read Root
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/en_core_web_sm/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_sentence_dependencies_v1_en_core_web_sm_sentence_dependencies_post(client):
    """Test case for read_sentence_dependencies_v1_en_core_web_sm_sentence_dependencies_post

    Read Sentence Dependencies
    """
    body = {"text":"text"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/en_core_web_sm/sentence-dependencies',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_read_version_v1_en_core_web_sm_version_get(client):
    """Test case for read_version_v1_en_core_web_sm_version_get

    Read Version
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/en_core_web_sm/version',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

