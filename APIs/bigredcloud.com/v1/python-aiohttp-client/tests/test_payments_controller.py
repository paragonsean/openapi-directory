# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_item_payment_dto import BatchItemPaymentDto
from openapi_server.models.page_result_payment_query_dto import PageResultPaymentQueryDto
from openapi_server.models.payment_dto import PaymentDto


pytestmark = pytest.mark.asyncio

async def test_payments_delete(client):
    """Test case for payments_delete

    Removes an existing Payment.
    """
    params = [('timestamp', 'timestamp_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/payments/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payments_get(client):
    """Test case for payments_get

    Returns a list of company's Payments. Supports OData querying protocol.  Filtering is allowed by \"entryDate\" field.  Ordering is allowed by \"id\" field.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/payments',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payments_post(client):
    """Test case for payments_post

    Creates a new Payment.
    """
    body = {"acCode":"C1","acEntries":[],"bankAccountCode":"B1","bankAccountId":1,"bookTranTypeId":3,"customFields":[{"description":"F1","id":1,"userDefinedFieldId":1,"value":"f1"},{"description":"F2","id":2,"userDefinedFieldId":2,"value":"f2"}],"detailCollection":["d1","d2"],"discount":2,"entryDate":"2011-07-01T00:00:00","id":2,"note":"123","procDate":"2011-08-08T00:00:00","reference":"000002","supplierId":2,"timestamp":"M7jbu9RD2wg=","total":155,"transferBankCode":"","transferBankId":1,"unallocated":155}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/payments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payments_process_batch(client):
    """Test case for payments_process_batch

    Processes a batch of Payments.
    """
    body = [openapi_server.BatchItemPaymentDto()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/payments/batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_payments_put(client):
    """Test case for payments_put

    Updates an existing Payment.
    """
    body = {"acCode":"C1","acEntries":[],"bankAccountCode":"B1","bankAccountId":1,"bookTranTypeId":3,"customFields":[{"description":"F1","id":1,"userDefinedFieldId":1,"value":"f1"},{"description":"F2","id":2,"userDefinedFieldId":2,"value":"f2"}],"detailCollection":["d1","d2"],"discount":2,"entryDate":"2011-07-01T00:00:00","id":2,"note":"123","procDate":"2011-08-08T00:00:00","reference":"000002","supplierId":2,"timestamp":"M7jbu9RD2wg=","total":155,"transferBankCode":"","transferBankId":1,"unallocated":155}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/payments/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_payments_id_get(client):
    """Test case for v1_payments_id_get

    Returns information about a single Payments.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/payments/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

