# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_document_with_web_hook200_response import GetDocumentWithWebHook200Response
from openapi_server.models.model400 import Model400
from openapi_server.models.model404 import Model404
from openapi_server.models.patches_schema_inner import PatchesSchemaInner


pytestmark = pytest.mark.asyncio

async def test_delete_document(client):
    """Test case for delete_document

    Delete a document
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/data/{path}'.format(path='opa/examples/public_servers'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_document(client):
    """Test case for get_document

    Get a document
    """
    params = [('input', {'key': {"input":{"example":{"flag":true}}}}),
                    ('pretty', true),
                    ('provenance', false),
                    ('explain', 'full'),
                    ('metrics', false),
                    ('instrument', false)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/data/{path}'.format(path='opa/examples/public_servers'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-yaml not supported by Connexion")
async def test_get_document_with_path(client):
    """Test case for get_document_with_path

    Get a document (with input)
    """
    body = None
    params = [('pretty', true),
                    ('provenance', false),
                    ('explain', 'full'),
                    ('metrics', false),
                    ('instrument', false)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-yaml',
    }
    response = await client.request(
        method='POST',
        path='/v1/data/{path}'.format(path='opa/examples/public_servers'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/x-yaml not supported by Connexion")
async def test_get_document_with_web_hook(client):
    """Test case for get_document_with_web_hook

    Get a document (with webhook)
    """
    body = None
    params = [('pretty', true)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/x-yaml',
    }
    response = await client.request(
        method='POST',
        path='/v0/data/{path}'.format(path='opa/examples/allow_request'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_document(client):
    """Test case for patch_document

    Update a document
    """
    body = [openapi_server.PatchesSchemaInner()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/data/{path}'.format(path='opa/examples/public_servers'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_put_document(client):
    """Test case for put_document

    Create or overwrite a document
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_none_match': '*',
    }
    response = await client.request(
        method='PUT',
        path='/v1/data/{path}'.format(path='opa/examples/public_servers'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

