# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.document import Document
from openapi_server.models.document_analytic_data import DocumentAnalyticData


pytestmark = pytest.mark.asyncio

async def test_cancel_document(client):
    """Test case for cancel_document

    Cancel document analysis
    """
    params = [('config_id', 'config_id_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/document/{document_id_content_type}'.format(document_id='document_id_example', content_type='content_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_queue_batch_of_documents(client):
    """Test case for queue_batch_of_documents

    Queue batch of documents for analysis
    """
    batch_of_documents = None
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/document/batch.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        json=batch_of_documents,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_queue_document(client):
    """Test case for queue_document

    Queue document for analysis
    """
    document = None
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/document.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        json=document,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_receive_document_analytic_data(client):
    """Test case for receive_document_analytic_data

    Retrieve document analysis or its status in queue
    """
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/document/{document_id_content_type}'.format(document_id='document_id_example', content_type='content_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_processed_documents(client):
    """Test case for retrieve_processed_documents

    Retrieve documents analysis
    """
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/document/processed.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

