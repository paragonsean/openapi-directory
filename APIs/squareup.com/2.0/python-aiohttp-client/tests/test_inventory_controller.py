# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_change_inventory_request import BatchChangeInventoryRequest
from openapi_server.models.batch_change_inventory_response import BatchChangeInventoryResponse
from openapi_server.models.batch_retrieve_inventory_changes_request import BatchRetrieveInventoryChangesRequest
from openapi_server.models.batch_retrieve_inventory_changes_response import BatchRetrieveInventoryChangesResponse
from openapi_server.models.batch_retrieve_inventory_counts_request import BatchRetrieveInventoryCountsRequest
from openapi_server.models.batch_retrieve_inventory_counts_response import BatchRetrieveInventoryCountsResponse
from openapi_server.models.retrieve_inventory_adjustment_response import RetrieveInventoryAdjustmentResponse
from openapi_server.models.retrieve_inventory_changes_response import RetrieveInventoryChangesResponse
from openapi_server.models.retrieve_inventory_count_response import RetrieveInventoryCountResponse
from openapi_server.models.retrieve_inventory_physical_count_response import RetrieveInventoryPhysicalCountResponse
from openapi_server.models.retrieve_inventory_transfer_response import RetrieveInventoryTransferResponse


pytestmark = pytest.mark.asyncio

async def test_batch_change_inventory(client):
    """Test case for batch_change_inventory

    BatchChangeInventory
    """
    body = {"request_body":{"changes":[{"physical_count":{"catalog_object_id":"W62UWFY35CWMYGVWK6TWJDNI","employee_id":"LRK57NSQ5X7PUD05","location_id":"C6W5YS5QM06F5","occurred_at":"2016-11-16T22:25:24.878Z","quantity":"53","reference_id":"1536bfbf-efed-48bf-b17d-a197141b2a92","state":"IN_STOCK"},"type":"PHYSICAL_COUNT"}],"idempotency_key":"8fc6a5b0-9fe8-4b46-b46b-2ef95793abbe","ignore_unchanged_counts":True}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/inventory/changes/batch-create',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_retrieve_inventory_changes(client):
    """Test case for batch_retrieve_inventory_changes

    BatchRetrieveInventoryChanges
    """
    body = {"request_body":{"catalog_object_ids":["W62UWFY35CWMYGVWK6TWJDNI"],"location_ids":["C6W5YS5QM06F5"],"states":["IN_STOCK"],"types":["PHYSICAL_COUNT"],"updated_after":"2016-11-01T00:00:00.000Z","updated_before":"2016-12-01T00:00:00.000Z"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/inventory/changes/batch-retrieve',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_batch_retrieve_inventory_counts(client):
    """Test case for batch_retrieve_inventory_counts

    BatchRetrieveInventoryCounts
    """
    body = {"request_body":{"catalog_object_ids":["W62UWFY35CWMYGVWK6TWJDNI"],"location_ids":["59TNP9SA8VGDA"],"updated_after":"2016-11-16T00:00:00.000Z"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/inventory/counts/batch-retrieve',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deprecated_batch_change_inventory(client):
    """Test case for deprecated_batch_change_inventory

    DeprecatedBatchChangeInventory
    """
    body = {"request_body":{"changes":[{"physical_count":{"catalog_object_id":"W62UWFY35CWMYGVWK6TWJDNI","employee_id":"LRK57NSQ5X7PUD05","location_id":"C6W5YS5QM06F5","occurred_at":"2016-11-16T22:25:24.878Z","quantity":"53","reference_id":"1536bfbf-efed-48bf-b17d-a197141b2a92","state":"IN_STOCK"},"type":"PHYSICAL_COUNT"}],"idempotency_key":"8fc6a5b0-9fe8-4b46-b46b-2ef95793abbe","ignore_unchanged_counts":True}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/inventory/batch-change',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deprecated_batch_retrieve_inventory_changes(client):
    """Test case for deprecated_batch_retrieve_inventory_changes

    DeprecatedBatchRetrieveInventoryChanges
    """
    body = {"request_body":{"catalog_object_ids":["W62UWFY35CWMYGVWK6TWJDNI"],"location_ids":["C6W5YS5QM06F5"],"states":["IN_STOCK"],"types":["PHYSICAL_COUNT"],"updated_after":"2016-11-01T00:00:00.000Z","updated_before":"2016-12-01T00:00:00.000Z"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/inventory/batch-retrieve-changes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deprecated_batch_retrieve_inventory_counts(client):
    """Test case for deprecated_batch_retrieve_inventory_counts

    DeprecatedBatchRetrieveInventoryCounts
    """
    body = {"request_body":{"catalog_object_ids":["W62UWFY35CWMYGVWK6TWJDNI"],"location_ids":["59TNP9SA8VGDA"],"updated_after":"2016-11-16T00:00:00.000Z"}}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/v2/inventory/batch-retrieve-counts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deprecated_retrieve_inventory_adjustment(client):
    """Test case for deprecated_retrieve_inventory_adjustment

    DeprecatedRetrieveInventoryAdjustment
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/inventory/adjustment/{adjustment_id}'.format(adjustment_id='adjustment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_deprecated_retrieve_inventory_physical_count(client):
    """Test case for deprecated_retrieve_inventory_physical_count

    DeprecatedRetrieveInventoryPhysicalCount
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/inventory/physical-count/{physical_count_id}'.format(physical_count_id='physical_count_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_inventory_adjustment(client):
    """Test case for retrieve_inventory_adjustment

    RetrieveInventoryAdjustment
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/inventory/adjustments/{adjustment_id}'.format(adjustment_id='adjustment_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_inventory_changes(client):
    """Test case for retrieve_inventory_changes

    RetrieveInventoryChanges
    """
    params = [('location_ids', 'location_ids_example'),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/inventory/{catalog_object_id}/changes'.format(catalog_object_id='catalog_object_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_inventory_count(client):
    """Test case for retrieve_inventory_count

    RetrieveInventoryCount
    """
    params = [('location_ids', 'location_ids_example'),
                    ('cursor', 'cursor_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/inventory/{catalog_object_id}'.format(catalog_object_id='catalog_object_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_inventory_physical_count(client):
    """Test case for retrieve_inventory_physical_count

    RetrieveInventoryPhysicalCount
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/inventory/physical-counts/{physical_count_id}'.format(physical_count_id='physical_count_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retrieve_inventory_transfer(client):
    """Test case for retrieve_inventory_transfer

    RetrieveInventoryTransfer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v2/inventory/transfers/{transfer_id}'.format(transfer_id='transfer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

