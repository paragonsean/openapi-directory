# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.collection import Collection
from openapi_server.models.collection_analytic_data import CollectionAnalyticData


pytestmark = pytest.mark.asyncio

async def test_cancel_collection(client):
    """Test case for cancel_collection

    Cancel collection analysis
    """
    params = [('config_id', 'config_id_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/collection/{collection_id_content_type}'.format(collection_id='collection_id_example', content_type='content_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("*/* not supported by Connexion. Use application/json instead. See https://github.com/zalando/connexion/pull/760")
async def test_queue_collection(client):
    """Test case for queue_collection

    Queue collection for analysis
    """
    collection = None
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/collection.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        json=collection,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_receive_collection_analytic_data(client):
    """Test case for receive_collection_analytic_data

    Retrieve collection analysis or its status in queue
    """
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/collection/{collection_id_content_type}'.format(collection_id='collection_id_example', content_type='content_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_processed_collections(client):
    """Test case for retrieve_processed_collections

    Retrieve collections analysis
    """
    params = [('config_id', 'config_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/collection/processed.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

