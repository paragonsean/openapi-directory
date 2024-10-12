# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deleted import Deleted
from openapi_server.models.global_jwt_verifier import GlobalJwtVerifier
from openapi_server.models.patch_inner import PatchInner


pytestmark = pytest.mark.asyncio

async def test_create_global_jwt_verifier(client):
    """Test case for create_global_jwt_verifier

    Create one global JWT verifiers
    """
    body = {"algoSettings":{"size":123123,"secret":"a string value","type":"a string value"},"name":"a string value","id":"a string value","source":{"name":"a string value","type":"a string value"},"strategy":{"verificationSettings":{"mappingSettings":{"values":{"key":"value"},"map":{"key":"value"},"remove":["a string value","a string value"]},"fields":{"key":"value"}},"type":"a string value"},"strict":True,"enabled":True,"desc":"a string value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/verifiers',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_global_jwt_verifier(client):
    """Test case for delete_global_jwt_verifier

    Delete one global JWT verifiers
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/verifiers/{verifier_id}'.format(verifier_id='verifier_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_all_global_jwt_verifiers(client):
    """Test case for find_all_global_jwt_verifiers

    Get all global JWT verifiers
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/verifiers',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_global_jwt_verifiers_by_id(client):
    """Test case for find_global_jwt_verifiers_by_id

    Get one global JWT verifiers
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/verifiers/{verifier_id}'.format(verifier_id='verifier_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_global_jwt_verifier(client):
    """Test case for patch_global_jwt_verifier

    Update one global JWT verifiers
    """
    body = [openapi_server.PatchInner()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PATCH',
        path='/api/verifiers/{verifier_id}'.format(verifier_id='verifier_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_global_jwt_verifier(client):
    """Test case for update_global_jwt_verifier

    Update one global JWT verifiers
    """
    body = {"algoSettings":{"size":123123,"secret":"a string value","type":"a string value"},"name":"a string value","id":"a string value","source":{"name":"a string value","type":"a string value"},"strategy":{"verificationSettings":{"mappingSettings":{"values":{"key":"value"},"map":{"key":"value"},"remove":["a string value","a string value"]},"fields":{"key":"value"}},"type":"a string value"},"strict":True,"enabled":True,"desc":"a string value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/verifiers/{verifier_id}'.format(verifier_id='verifier_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

