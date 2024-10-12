# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_item_sales_entry_dto import BatchItemSalesEntryDto
from openapi_server.models.page_result_sales_entry_query_dto import PageResultSalesEntryQueryDto
from openapi_server.models.sales_entry_dto import SalesEntryDto


pytestmark = pytest.mark.asyncio

async def test_sales_entries_delete(client):
    """Test case for sales_entries_delete

    Removes an existing Sales Entry.
    """
    params = [('timestamp', 'timestamp_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/salesEntries/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_entries_get(client):
    """Test case for sales_entries_get

    Returns a list of company's Sales Entries. Supports OData querying protocol.  Filtering is allowed by \"entryDate\" field.  Ordering is allowed by \"id\" field.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/salesEntries',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_entries_post(client):
    """Test case for sales_entries_post

    Creates a new Sales Entry.
    """
    body = {"acCode":"code","acEntries":[{"accountCode":"SA01","analysisCategoryId":40888,"description":"SAL 1","id":73450,"value":636.36}],"bookTranTypeId":5,"customFields":[{"description":"acudf_1","id":1,"userDefinedFieldId":1,"value":"acudfv_1"},{"description":"acudf_2","id":2,"userDefinedFieldId":1,"value":"acudfv_2"}],"customerId":70583,"detailCollection":[],"details":"detail_1","entryDate":"2011-01-01T00:00:00","id":1,"netGoods":0,"netServices":0,"note":"Customer 1","procDate":"2011-01-01T00:00:00","reference":"000001","timestamp":"Ehn9u9RD2wg=","total":700,"totalNet":636.36,"totalVAT":63.64,"unpaid":0,"vatEntries":[{"amount":636.36,"id":63649,"percentage":10,"vatRateId":30657}],"vatTypeId":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/salesEntries',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_entries_process_batch(client):
    """Test case for sales_entries_process_batch

    Processes a batch of Sales Entries.
    """
    body = [openapi_server.BatchItemSalesEntryDto()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/salesEntries/batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_entries_put(client):
    """Test case for sales_entries_put

    Updates an existing Sales Entry.
    """
    body = {"acCode":"code","acEntries":[{"accountCode":"SA01","analysisCategoryId":40888,"description":"SAL 1","id":73450,"value":636.36}],"bookTranTypeId":5,"customFields":[{"description":"acudf_1","id":1,"userDefinedFieldId":1,"value":"acudfv_1"},{"description":"acudf_2","id":2,"userDefinedFieldId":1,"value":"acudfv_2"}],"customerId":70583,"detailCollection":[],"details":"detail_1","entryDate":"2011-01-01T00:00:00","id":1,"netGoods":0,"netServices":0,"note":"Customer 1","procDate":"2011-01-01T00:00:00","reference":"000001","timestamp":"Ehn9u9RD2wg=","total":700,"totalNet":636.36,"totalVAT":63.64,"unpaid":0,"vatEntries":[{"amount":636.36,"id":63649,"percentage":10,"vatRateId":30657}],"vatTypeId":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/salesEntries/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_sales_entries_id_get(client):
    """Test case for v1_sales_entries_id_get

    Returns information about a single Sales Entry.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/salesEntries/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

