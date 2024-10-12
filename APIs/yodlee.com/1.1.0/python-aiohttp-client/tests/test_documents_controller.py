# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.document_download_response import DocumentDownloadResponse
from openapi_server.models.document_response import DocumentResponse
from openapi_server.models.yodlee_error import YodleeError


pytestmark = pytest.mark.asyncio

async def test_delete_document(client):
    """Test case for delete_document

    Delete Document
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='DELETE',
        path='/documents/{document_id}'.format(document_id='document_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_download_document(client):
    """Test case for download_document

    Download a Document
    """
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/documents/{document_id}'.format(document_id='document_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_documents(client):
    """Test case for get_documents

    Get Documents
    """
    params = [('Keyword', 'keyword_example'),
                    ('accountId', 'account_id_example'),
                    ('docType', 'doc_type_example'),
                    ('fromDate', 'from_date_example'),
                    ('toDate', 'to_date_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
    }
    response = await client.request(
        method='GET',
        path='/documents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

