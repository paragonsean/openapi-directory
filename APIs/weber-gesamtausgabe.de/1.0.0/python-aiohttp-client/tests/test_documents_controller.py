# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.document import Document
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_documents_doc_idget(client):
    """Test case for documents_doc_idget

    Returns documents by ID
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/exist/apps/WeGA-WebApp/api/v1/documents/{doc_id}'.format(doc_id='A002068'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_find_by_author_author_idget(client):
    """Test case for documents_find_by_author_author_idget

    Finds documents by author
    """
    params = [('docType', ['doc_type_example']),
                    ('offset', 1),
                    ('limit', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/exist/apps/WeGA-WebApp/api/v1/documents/findByAuthor/{author_id}'.format(author_id='A002068'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_find_by_date_get(client):
    """Test case for documents_find_by_date_get

    Finds documents by date
    """
    params = [('fromDate', '2013-10-20'),
                    ('toDate', '2013-10-20'),
                    ('docType', ['doc_type_example']),
                    ('offset', 1),
                    ('limit', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/exist/apps/WeGA-WebApp/api/v1/documents/findByDate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_find_by_mention_doc_idget(client):
    """Test case for documents_find_by_mention_doc_idget

    Finds documents by reference
    """
    params = [('docType', ['doc_type_example']),
                    ('offset', 1),
                    ('limit', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/exist/apps/WeGA-WebApp/api/v1/documents/findByMention/{doc_id}'.format(doc_id='A002068'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_documents_get(client):
    """Test case for documents_get

    Lists all documents
    """
    params = [('docType', ['doc_type_example']),
                    ('offset', 1),
                    ('limit', 10)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/exist/apps/WeGA-WebApp/api/v1/documents',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

