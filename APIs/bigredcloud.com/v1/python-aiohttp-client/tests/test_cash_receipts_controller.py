# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_item_cash_receipt_dto import BatchItemCashReceiptDto
from openapi_server.models.cash_receipt_dto import CashReceiptDto
from openapi_server.models.page_result_cash_receipt_query_dto import PageResultCashReceiptQueryDto


pytestmark = pytest.mark.asyncio

async def test_cash_receipts_delete(client):
    """Test case for cash_receipts_delete

    Removes an existing Cash Receipt.
    """
    params = [('timestamp', 'timestamp_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/cashReceipts/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cash_receipts_get(client):
    """Test case for cash_receipts_get

    Returns a list of company's Cash Receipts. Supports OData querying protocol.  Filtering is allowed by \"entryDate\" field.  Ordering is allowed by \"id\" field.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cashReceipts',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cash_receipts_post(client):
    """Test case for cash_receipts_post

    Creates a new Cash Receipt.
    """
    body = {"acEntries":[{"accountCode":"000","analysisCategoryId":1,"description":"AnCat1","id":1,"value":30}],"bookTranTypeId":1,"customFields":[{"description":"acudf_1","id":1,"userDefinedFieldId":1,"value":"acudfv_1"}],"detailCollection":["det_1","det_2","det_3"],"discount":0,"entryDate":"2011-01-01T00:00:00","id":1,"ledger":0,"note":"note1","procDate":"2011-01-05T00:00:00","timestamp":"uhu/u9RD2wg=","total":50,"unallocated":0,"vatEntries":[{"amount":50,"id":1,"percentage":15,"vatRateId":1}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/cashReceipts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cash_receipts_process_batch(client):
    """Test case for cash_receipts_process_batch

    Processes a batch of Cash Receipts.
    """
    body = [openapi_server.BatchItemCashReceiptDto()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/cashReceipts/batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_cash_receipts_put(client):
    """Test case for cash_receipts_put

    Updates an existing Cash Receipt.
    """
    body = {"acEntries":[{"accountCode":"000","analysisCategoryId":1,"description":"AnCat1","id":1,"value":30}],"bookTranTypeId":1,"customFields":[{"description":"acudf_1","id":1,"userDefinedFieldId":1,"value":"acudfv_1"}],"detailCollection":["det_1","det_2","det_3"],"discount":0,"entryDate":"2011-01-01T00:00:00","id":1,"ledger":0,"note":"note1","procDate":"2011-01-05T00:00:00","timestamp":"uhu/u9RD2wg=","total":50,"unallocated":0,"vatEntries":[{"amount":50,"id":1,"percentage":15,"vatRateId":1}]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/cashReceipts/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_cash_receipts_id_get(client):
    """Test case for v1_cash_receipts_id_get

    Returns information about a single Cash Receipt.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/cashReceipts/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

