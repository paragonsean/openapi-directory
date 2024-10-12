# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.document import Document
from openapi_server.models.document_list import DocumentList
from openapi_server.models.document_updates import DocumentUpdates
from openapi_server.models.document_upload_request import DocumentUploadRequest
from openapi_server.models.error import Error
from openapi_server.models.operation_status import OperationStatus


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_create_project_document(client):
    """Test case for create_project_document

    Upload a new document
    """
    body = {"schemes[]":"schemes[]","documents[]":["",""],"source-links[]":[{"size":0,"name":"name","source":"dropbox","url":"https://openapi-generator.tech"},{"size":0,"name":"name","source":"dropbox","url":"https://openapi-generator.tech"}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/projects/{project_id}/documents'.format(project_id=74),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_project_document(client):
    """Test case for delete_project_document

    Delete the document
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/projects/{project_id}/documents/{document_id}'.format(project_id=74, document_id=179469),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_project_document(client):
    """Test case for download_project_document

    Download a project source document
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{project_id}/documents/{document_id}/download'.format(project_id=74, document_id=179469),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_translated_document_for_language(client):
    """Test case for download_translated_document_for_language

    Download translated document
    """
    params = [('certified', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{project_id}/documents/{document_id}/translations/download/{language}'.format(project_id=74, document_id=179469, language='en-US'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_document(client):
    """Test case for get_project_document

    View a project source document
    """
    params = [('with[]', ['_with_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{project_id}/documents/{document_id}'.format(project_id=74, document_id=179469),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_project_documents(client):
    """Test case for get_project_documents

    View project source documents
    """
    params = [('with[]', ['_with_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/projects/{project_id}/documents'.format(project_id=74),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_update_project_document(client):
    """Test case for update_project_document

    Update the document.
    """
    body = {"documents":"","schemes":"schemes","source-link":{"size":0,"name":"name","source":"dropbox","url":"https://openapi-generator.tech"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/projects/{project_id}/documents/{document_id}'.format(project_id=74, document_id=179469),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

