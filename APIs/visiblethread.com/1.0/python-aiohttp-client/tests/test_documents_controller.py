# coding: utf-8

import pytest
import json
from aiohttp import web
from aiohttp import FormData
from aiohttp import FormData

from openapi_server.models.document_list_summary import DocumentListSummary
from openapi_server.models.document_response_detailed import DocumentResponseDetailed
from openapi_server.models.document_response_not_ready import DocumentResponseNotReady
from openapi_server.models.new_document_response import NewDocumentResponse
from openapi_server.models.search import Search


pytestmark = pytest.mark.asyncio

async def test_dictionaries_get(client):
    """Test case for dictionaries_get

    Get your list of dictionaries
    """
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/dictionaries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_get(client):
    """Test case for documents_get

    Get your list of documents
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/documents',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_doc_by_id(client):
    """Test case for get_doc_by_id

    Get data from a previously submitted document
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/documents/{doc_id}'.format(doc_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_search_results(client):
    """Test case for get_search_results

    Gets search results for a particular document/dictionary
    """
    params = [('matchingOnly', True)]
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/searches/{doc_id}/{dictionary_id}'.format(doc_id=56, dictionary_id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_run_search(client):
    """Test case for run_search

    Run a search
    """
    body = {"docId":56487,"dictId":47364}
    headers = { 
        'Accept': 'text/plain',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/searches',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_searches_get(client):
    """Test case for searches_get

    Get your list of searches
    """
    headers = { 
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/searches',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_dictionary(client):
    """Test case for upload_dictionary

    Upload a dictionary (CSV)
    """
    headers = { 
        'Content-Type': 'multipart/form-data',
        'api_key': 'special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    response = await client.request(
        method='POST',
        path='/api/v1/dictionaries',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("multipart/form-data not supported by Connexion")
async def test_upload_doc(client):
    """Test case for upload_doc

    Upload a document
    """
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'multipart/form-data',
        'api_key': 'special-key',
    }
    data = FormData()
    data.add_field('file', '/path/to/file')
    data.add_field('long_sentence_word_count', 56)
    data.add_field('very_long_sentence_word_count', 56)
    response = await client.request(
        method='POST',
        path='/api/v1/documents',
        headers=headers,
        data=data,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

