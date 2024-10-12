# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_or_replace_documents_request_inner import AddOrReplaceDocumentsRequestInner
from openapi_server.models.add_or_update_documents_request_inner import AddOrUpdateDocumentsRequestInner


pytestmark = pytest.mark.asyncio

async def test_add_or_replace_documents(client):
    """Test case for add_or_replace_documents

    Add or replace documents
    """
    body = [{"author":"Jane Austen","genre":"romance","id":2,"price":3.5,"title":"Pride and Prejudice"},{"author":"Antoine de Saint-Exupéry","genre":"adventure","id":456,"price":10,"title":"Le Petit Prince"},{"author":"Lewis Carroll","genre":"fantasy","id":1,"price":25.99,"title":"Alice In Wonderland"},{"author":"J. R. R. Tolkien","genre":"fantasy","id":1344,"title":"The Hobbit"},{"author":"J. K. Rowling","genre":"fantasy","id":4,"title":"Harry Potter and the Half-Blood Prince"},{"author":"Douglas Adams","id":42,"title":"The Hitchhiker's Guide to the Galaxy"}]
    params = [('primaryKey', 'id'),
                    ('csvDelimiter', ';')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/indexes/books/documents',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_or_update_documents(client):
    """Test case for add_or_update_documents

    Add or update documents
    """
    body = [{"author":"J. Austen","date":"1813","id":2}]
    params = [('primaryKey', 'id'),
                    ('csvDelimiter', ';')]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/indexes/books/documents',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_all_documents(client):
    """Test case for delete_all_documents

    Delete all documents
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/indexes/books/documents',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_documents(client):
    """Test case for delete_documents

    Delete documents
    """
    body = [1,2]
    headers = { 
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/indexes/books/documents/delete-batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_delete_one_document(client):
    """Test case for delete_one_document

    Delete one document
    """
    headers = { 
        'Content-Type': 'text/plain',
    }
    response = await client.request(
        method='DELETE',
        path='/indexes/books/documents/1',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_documents(client):
    """Test case for get_documents

    Get documents
    """
    params = [('limit', '1'),
                    ('offset', '10'),
                    ('fields', 'id')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/indexes/books/documents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_one_document(client):
    """Test case for get_one_document

    Get one document
    """
    params = [('fields', 'id')]
    headers = { 
    }
    response = await client.request(
        method='GET',
        path='/indexes/books/documents/2',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

