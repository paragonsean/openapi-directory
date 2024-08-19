# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.collection import Collection
from openapi_server.models.collection_list import CollectionList
from openapi_server.models.database_create_collection_request import DatabaseCreateCollectionRequest
from openapi_server.models.database_create_document_request import DatabaseCreateDocumentRequest
from openapi_server.models.database_update_collection_request import DatabaseUpdateCollectionRequest
from openapi_server.models.database_update_document_request import DatabaseUpdateDocumentRequest
from openapi_server.models.document import Document
from openapi_server.models.document_list import DocumentList


pytestmark = pytest.mark.asyncio

async def test_database_create_collection(client):
    """Test case for database_create_collection

    Create Collection
    """
    body = openapi_server.DatabaseCreateCollectionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/database/collections',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_create_document(client):
    """Test case for database_create_document

    Create Document
    """
    body = openapi_server.DatabaseCreateDocumentRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/database/collections/{collection_id}/documents'.format(collection_id='collection_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_delete_collection(client):
    """Test case for database_delete_collection

    Delete Collection
    """
    headers = { 
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/database/collections/{collection_id}'.format(collection_id='collection_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_delete_document(client):
    """Test case for database_delete_document

    Delete Document
    """
    headers = { 
        'Project': 'special-key',
        'JWT': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/database/collections/{collection_id}/documents/{document_id}'.format(collection_id='collection_id_example', document_id='document_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_get_collection(client):
    """Test case for database_get_collection

    Get Collection
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/database/collections/{collection_id}'.format(collection_id='collection_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_get_document(client):
    """Test case for database_get_document

    Get Document
    """
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/database/collections/{collection_id}/documents/{document_id}'.format(collection_id='collection_id_example', document_id='document_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_list_collections(client):
    """Test case for database_list_collections

    List Collections
    """
    params = [('search', ''),
                    ('limit', 25),
                    ('offset', 0),
                    ('orderType', 'ASC')]
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/database/collections',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_list_documents(client):
    """Test case for database_list_documents

    List Documents
    """
    params = [('filters', []),
                    ('limit', 25),
                    ('offset', 0),
                    ('orderField', ''),
                    ('orderType', 'ASC'),
                    ('orderCast', 'string'),
                    ('search', '')]
    headers = { 
        'Accept': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/database/collections/{collection_id}/documents'.format(collection_id='collection_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_update_collection(client):
    """Test case for database_update_collection

    Update Collection
    """
    body = openapi_server.DatabaseUpdateCollectionRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/database/collections/{collection_id}'.format(collection_id='collection_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_database_update_document(client):
    """Test case for database_update_document

    Update Document
    """
    body = openapi_server.DatabaseUpdateDocumentRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Project': 'special-key',
        'JWT': 'special-key',
        'Key': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v1/database/collections/{collection_id}/documents/{document_id}'.format(collection_id='collection_id_example', document_id='document_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

