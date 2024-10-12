# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.document import Document
from openapi_server.models.document_list import DocumentList
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_get_document(client):
    """Test case for get_document

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/documents/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_documents(client):
    """Test case for list_documents

    
    """
    params = [('page', 1),
                    ('per_page', 20)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/v1/documents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

