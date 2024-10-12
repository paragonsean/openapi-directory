# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_item_cash_payment_dto import BatchItemCashPaymentDto
from openapi_server.models.cash_payment_dto import CashPaymentDto
from openapi_server.models.page_result_cash_payment_query_dto import PageResultCashPaymentQueryDto


pytestmark = pytest.mark.asyncio

async def test_cash_payments_delete(client):
    """Test case for cash_payments_delete

    Removes an existing Cash Payment.
    """
    params = [('timestamp', 'timestamp_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/cashPayments/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cash_payments_get(client):
    """Test case for cash_payments_get

    Returns a list of company's Cash Payments. Supports OData querying protocol.  Filtering is allowed by \"entryDate\" field.  Ordering is allowed by \"id\" field.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cashPayments',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cash_payments_post(client):
    """Test case for cash_payments_post

    Creates a new Cash Payment.
    """
    body = {"acEntries":[{"accountCode":"CP01","analysisCategoryId":10433,"description":"Cash Pay 01","id":62741,"value":200}],"bankAccountCode":"BAK2","bankAccountId":11111,"bookTranTypeId":2,"customFields":[],"detailCollection":["test"],"discount":0,"entryDate":"2017-07-01T00:00:00","id":12345,"ledger":100,"lodgement":0,"note":"Supplier 1","procDate":"2017-07-26T00:00:00","supplierId":70599,"timestamp":"rfS3u9RD2wg=","total":100}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/cashPayments',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cash_payments_process_batch(client):
    """Test case for cash_payments_process_batch

    Processes a batch of Cash Payments.
    """
    body = [openapi_server.BatchItemCashPaymentDto()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/cashPayments/batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cash_payments_put(client):
    """Test case for cash_payments_put

    Updates an existing Cash Payment.
    """
    body = {"acEntries":[{"accountCode":"CP01","analysisCategoryId":10433,"description":"Cash Pay 01","id":62741,"value":200}],"bankAccountCode":"BAK2","bankAccountId":11111,"bookTranTypeId":2,"customFields":[],"detailCollection":["test"],"discount":0,"entryDate":"2017-07-01T00:00:00","id":12345,"ledger":100,"lodgement":0,"note":"Supplier 1","procDate":"2017-07-26T00:00:00","supplierId":70599,"timestamp":"rfS3u9RD2wg=","total":100}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/cashPayments/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_cash_payments_id_get(client):
    """Test case for v1_cash_payments_id_get

    Returns information about a single Cash Payment.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cashPayments/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

