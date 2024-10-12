# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_item_sales_invoice_credit_note_dto import BatchItemSalesInvoiceCreditNoteDto
from openapi_server.models.page_result_sales_credit_note_query_dto import PageResultSalesCreditNoteQueryDto
from openapi_server.models.sales_invoice_credit_note_dto import SalesInvoiceCreditNoteDto


pytestmark = pytest.mark.asyncio

async def test_sales_credit_notes_delete(client):
    """Test case for sales_credit_notes_delete

    Removes an existing Sales Credit Note.
    """
    params = [('timestamp', 'timestamp_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/salesCreditNotes/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_credit_notes_get(client):
    """Test case for sales_credit_notes_get

    Returns a list of company's Sales Credit Notes. Supports OData querying protocol.  Filtering is allowed by \"entryDate\" field.  Ordering is allowed by \"id\" field.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/salesCreditNotes',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_credit_notes_post(client):
    """Test case for sales_credit_notes_post

    Creates a new Sales Credit Note.
    """
    body = {"acCode":"CUS3","bookTranTypeId":7,"customFields":[{"description":"acudf_1","id":1,"userDefinedFieldId":1,"value":"acudfv_1"},{"description":"acudf_2","id":2,"userDefinedFieldId":1,"value":"acudfv_2"}],"customerId":70585,"deliveryTo":["dt_1","dt_2"],"details":"detail_1","entryDate":"2016-06-01T00:00:00","id":75813,"loType":"1","note":"Customer 3","ourReference":"ddNumber_1","procDate":"2016-06-24T00:00:00","productTrans":[{"acEntries":[{"accountCode":"SA02","analysisCategoryId":40889,"description":"AnCat1","id":73455,"value":-200}],"amount":-220,"amountNet":-200,"id":51820,"percentage":10,"productCode":"PRO2","productId":20108,"quantity":-1,"tranNotes":["tn_1","tn_2"],"unitPrice":200,"vat":-20,"vatAnalysisTypeId":0,"vatRateId":30657}],"saleRepId":33110,"timestamp":"EQUJvNRD2wg=","total":-220,"totalNet":-200,"totalVAT":-20,"unpaid":-220,"vatTypeId":1,"yourReference":"poNumber_1"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/salesCreditNotes',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_credit_notes_process_batch(client):
    """Test case for sales_credit_notes_process_batch

    Processes a batch of Sales Credit Notes.
    """
    body = [openapi_server.BatchItemSalesInvoiceCreditNoteDto()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/salesCreditNotes/batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_credit_notes_put(client):
    """Test case for sales_credit_notes_put

    Updates an existing Sales Credit Note.
    """
    body = {"acCode":"CUS3","bookTranTypeId":7,"customFields":[{"description":"acudf_1","id":1,"userDefinedFieldId":1,"value":"acudfv_1"},{"description":"acudf_2","id":2,"userDefinedFieldId":1,"value":"acudfv_2"}],"customerId":70585,"deliveryTo":["dt_1","dt_2"],"details":"detail_1","entryDate":"2016-06-01T00:00:00","id":75813,"loType":"1","note":"Customer 3","ourReference":"ddNumber_1","procDate":"2016-06-24T00:00:00","productTrans":[{"acEntries":[{"accountCode":"SA02","analysisCategoryId":40889,"description":"AnCat1","id":73455,"value":-200}],"amount":-220,"amountNet":-200,"id":51820,"percentage":10,"productCode":"PRO2","productId":20108,"quantity":-1,"tranNotes":["tn_1","tn_2"],"unitPrice":200,"vat":-20,"vatAnalysisTypeId":0,"vatRateId":30657}],"saleRepId":33110,"timestamp":"EQUJvNRD2wg=","total":-220,"totalNet":-200,"totalVAT":-20,"unpaid":-220,"vatTypeId":1,"yourReference":"poNumber_1"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/salesCreditNotes/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_sales_credit_notes_id_get(client):
    """Test case for v1_sales_credit_notes_id_get

    Returns information about a single Sales Credit Note.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/salesCreditNotes/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

