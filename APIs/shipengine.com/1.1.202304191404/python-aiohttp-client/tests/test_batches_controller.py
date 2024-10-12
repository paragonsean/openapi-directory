# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_to_batch_request_body import AddToBatchRequestBody
from openapi_server.models.batch_status import BatchStatus
from openapi_server.models.batches_sort_by import BatchesSortBy
from openapi_server.models.create_batch_request_body import CreateBatchRequestBody
from openapi_server.models.create_batch_response_body import CreateBatchResponseBody
from openapi_server.models.error_response_body import ErrorResponseBody
from openapi_server.models.get_batch_by_external_id_response_body import GetBatchByExternalIdResponseBody
from openapi_server.models.get_batch_by_id_response_body import GetBatchByIdResponseBody
from openapi_server.models.list_batch_errors_response_body import ListBatchErrorsResponseBody
from openapi_server.models.list_batches_response_body import ListBatchesResponseBody
from openapi_server.models.process_batch_request_body import ProcessBatchRequestBody
from openapi_server.models.remove_from_batch_request_body import RemoveFromBatchRequestBody
from openapi_server.models.sort_dir import SortDir


pytestmark = pytest.mark.asyncio

async def test_add_to_batch(client):
    """Test case for add_to_batch

    Add to a Batch
    """
    body = openapi_server.AddToBatchRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/batches/{batch_id}/add'.format(batch_id='batch_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_batch(client):
    """Test case for create_batch

    Create A Batch
    """
    body = openapi_server.CreateBatchRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/batches',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_batch(client):
    """Test case for delete_batch

    Delete Batch By Id
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v1/batches/{batch_id}'.format(batch_id='batch_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_batch_by_external_id(client):
    """Test case for get_batch_by_external_id

    Get Batch By External ID
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/batches/external_batch_id/{external_batch_id}'.format(external_batch_id='13553d7f-3c87-4771-bae1-c49bacef11cb'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_batch_by_id(client):
    """Test case for get_batch_by_id

    Get Batch By ID
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/batches/{batch_id}'.format(batch_id='batch_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_batch_errors(client):
    """Test case for list_batch_errors

    Get Batch Errors
    """
    params = [('page', 1),
                    ('pagesize', 56)]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/batches/{batch_id}/errors'.format(batch_id='batch_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_list_batches(client):
    """Test case for list_batches

    List Batches
    """
    params = [('status', openapi_server.BatchStatus()),
                    ('page', 1),
                    ('page_size', 25),
                    ('sort_dir', openapi_server.SortDir()),
                    ('batch_number', 'batch_number_example'),
                    ('sort_by', openapi_server.BatchesSortBy())]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/batches',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_process_batch(client):
    """Test case for process_batch

    Process Batch ID Labels
    """
    body = openapi_server.ProcessBatchRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/batches/{batch_id}/process/labels'.format(batch_id='batch_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_remove_from_batch(client):
    """Test case for remove_from_batch

    Remove From Batch
    """
    body = openapi_server.RemoveFromBatchRequestBody()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v1/batches/{batch_id}/remove'.format(batch_id='batch_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_batch(client):
    """Test case for update_batch

    Update Batch By Id
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v1/batches/{batch_id}'.format(batch_id='batch_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

