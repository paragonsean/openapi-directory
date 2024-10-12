# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData

from openapi_server.models.file_upload200_response import FileUpload200Response
from openapi_server.models.file_upload400_response import FileUpload400Response
from openapi_server.models.googlerpc_status import GooglerpcStatus
from openapi_server.models.vectara_delete_document_request import VectaraDeleteDocumentRequest
from openapi_server.models.vectara_index_document_request import VectaraIndexDocumentRequest
from openapi_server.models.vectara_index_document_response import VectaraIndexDocumentResponse


pytestmark = pytest.mark.asyncio

async def test_delete(client):
    """Test case for delete

    
    """
    body = openapi_server.VectaraDeleteDocumentRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'customer_id': 56,
        'ApiKeyAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/delete-doc',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_file_upload(client):
    """Test case for file_upload

    
    """
    params = [('c', 56),
                    ('o', 56),
                    ('d', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'ApiKeyAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    data = FormData()
    data.add_field('doc_metadata', 'doc_metadata_example')
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/v1/upload',
        headers=headers,
        data=data,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_index(client):
    """Test case for index

    
    """
    body = openapi_server.VectaraIndexDocumentRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'customer_id': 56,
        'ApiKeyAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/index',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

