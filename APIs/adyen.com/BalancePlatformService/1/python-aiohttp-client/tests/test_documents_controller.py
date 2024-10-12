# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.document import Document
from openapi_server.models.service_error import ServiceError


pytestmark = pytest.mark.asyncio

async def test_delete_documents_id(client):
    """Test case for delete_documents_id

    Delete a document
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/bcl/v1/documents/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_documents_id(client):
    """Test case for get_documents_id

    Get a document
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/bcl/v1/documents/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_documents_id(client):
    """Test case for patch_documents_id

    Update a document
    """
    body = {"issuerState":"issuerState","owner":{"id":"id","type":"type"},"fileName":"fileName","attachments":[{"filename":"filename","pageType":"pageType","contentType":"contentType","content":"content"},{"filename":"filename","pageType":"pageType","contentType":"contentType","content":"content"}],"description":"description","creationDate":"2000-01-23T04:56:07.000+00:00","type":"bankStatement","expiryDate":"expiryDate","issuerCountry":"issuerCountry","number":"number","modificationDate":"2000-01-23T04:56:07.000+00:00","attachment":{"filename":"filename","pageType":"pageType","contentType":"contentType","content":"content"},"id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/bcl/v1/documents/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_post_documents(client):
    """Test case for post_documents

    Upload a document for verification checks
    """
    body = {"issuerState":"issuerState","owner":{"id":"id","type":"type"},"fileName":"fileName","attachments":[{"filename":"filename","pageType":"pageType","contentType":"contentType","content":"content"},{"filename":"filename","pageType":"pageType","contentType":"contentType","content":"content"}],"description":"description","creationDate":"2000-01-23T04:56:07.000+00:00","type":"bankStatement","expiryDate":"expiryDate","issuerCountry":"issuerCountry","number":"number","modificationDate":"2000-01-23T04:56:07.000+00:00","attachment":{"filename":"filename","pageType":"pageType","contentType":"contentType","content":"content"},"id":"id"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/bcl/v1/documents',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

