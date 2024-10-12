# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_bank_transfer_batch_payment_request import AddBankTransferBatchPaymentRequest
from openapi_server.models.batch import Batch
from openapi_server.models.batch_approvers import BatchApprovers
from openapi_server.models.batch_item_internal_transfer import BatchItemInternalTransfer
from openapi_server.models.batch_item_international_transfer_mode1 import BatchItemInternationalTransferMode1
from openapi_server.models.batch_items import BatchItems
from openapi_server.models.new_batch import NewBatch
from openapi_server.models.new_batch_item_response import NewBatchItemResponse
from openapi_server.models.new_batch_response import NewBatchResponse


pytestmark = pytest.mark.asyncio

async def test_add_bank_transfer_batch_payment(client):
    """Test case for add_bank_transfer_batch_payment

    Add a bank transfer payment to the batch.
    """
    body = openapi_server.AddBankTransferBatchPaymentRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/business/v1/batches/{batch_uuid}/banktransfers'.format(batch_uuid='4ADFB67A-0F5B-4A9A-9D74-34437250045C'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_internal_transfer_batch_payment(client):
    """Test case for add_internal_transfer_batch_payment

    Add an internal transfer payment to the batch
    """
    body = openapi_server.BatchItemInternalTransfer()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/business/v1/batches/{batch_uuid}/internaltransfers'.format(batch_uuid='4ADFB67A-0F5B-4A9A-9D74-34437250045C'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_add_international_transfer_batch_payment(client):
    """Test case for add_international_transfer_batch_payment

    Add an international transfer payment to the batch.
    """
    body = openapi_server.BatchItemInternationalTransferMode1()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/business/v2/batches/{batch_uuid}/internationaltransfers'.format(batch_uuid='4ADFB67A-0F5B-4A9A-9D74-34437250045C'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cancel_batch_payment(client):
    """Test case for cancel_batch_payment

    Cancel a batch
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/business/v1/batches/{batch_uuid}'.format(batch_uuid='4ADFB67A-0F5B-4A9A-9D74-34437250045C'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_batch_payment(client):
    """Test case for create_batch_payment

    Create a new batch of payments
    """
    body = openapi_server.NewBatch()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/business/v1/batches',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_bank_transfer_batch_payment(client):
    """Test case for delete_bank_transfer_batch_payment

    Remove a Payment from the Batch (Bank Transfers)
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/business/v1/batches/{batch_uuid}/banktransfers/{item_uuid}'.format(batch_uuid='4ADFB67A-0F5B-4A9A-9D74-34437250045C', item_uuid='item_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_internal_transfer_batch_payment(client):
    """Test case for delete_internal_transfer_batch_payment

    Remove a Payment from the Batch (Internal Transfer)
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/business/v1/batches/{batch_uuid}/internaltransfers/{item_uuid}'.format(batch_uuid='4ADFB67A-0F5B-4A9A-9D74-34437250045C', item_uuid='4ADFB67A-0F5B-4A9A-9D74-34437250045C'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_international_transfer_batch_payment(client):
    """Test case for delete_international_transfer_batch_payment

    Remove a Payment from the Batch (International Transfers)
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/business/v2/batches/{batch_uuid}/internationaltransfers/{item_uuid}'.format(batch_uuid='4ADFB67A-0F5B-4A9A-9D74-34437250045C', item_uuid='item_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_batches(client):
    """Test case for get_batches

    List batches
    """
    params = [('batchStatus', 'SUBMITTED'),
                    ('batchTypes', 'INTERNAL_TRANSFER'),
                    ('orderBy', 'DATE'),
                    ('order', 'DESC')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/business/v1/batches',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_details_single_batch(client):
    """Test case for get_details_single_batch

    Get details of a single Batch
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/business/v1/batches/{batch_uuid}'.format(batch_uuid='4ADFB67A-0F5B-4A9A-9D74-34437250045C'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_items_batch_bank_transfer(client):
    """Test case for get_items_batch_bank_transfer

    List items in a Batch (Bank Transfers)
    """
    params = [('offset', 0),
                    ('limit', 10)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/business/v1/batches/{batch_uuid}/banktransfers'.format(batch_uuid='4ADFB67A-0F5B-4A9A-9D74-34437250045C'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_items_batch_internal_trasnfer(client):
    """Test case for get_items_batch_internal_trasnfer

    List items in a Batch (Internal Transfers)
    """
    params = [('offset', 0),
                    ('limit', 10)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/business/v1/batches/{batch_uuid}/internaltransfers'.format(batch_uuid='4ADFB67A-0F5B-4A9A-9D74-34437250045C'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_items_batch_international_transfer(client):
    """Test case for get_items_batch_international_transfer

    List items in a Batch (International Transfers)
    """
    params = [('offset', 0),
                    ('limit', 10)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/business/v2/batches/{batch_uuid}/internationaltransfers'.format(batch_uuid='4ADFB67A-0F5B-4A9A-9D74-34437250045C'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_listof_approvers_for_batch(client):
    """Test case for get_listof_approvers_for_batch

    List Approvers for a Batch
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/business/v1/batches/{batch_uuid}/approvals'.format(batch_uuid='4ADFB67A-0F5B-4A9A-9D74-34437250045C'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_submit_batch(client):
    """Test case for submit_batch

    Submit a batch for approval
    """
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/business/v1/batches/{batch_uuid}'.format(batch_uuid='4ADFB67A-0F5B-4A9A-9D74-34437250045C'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

