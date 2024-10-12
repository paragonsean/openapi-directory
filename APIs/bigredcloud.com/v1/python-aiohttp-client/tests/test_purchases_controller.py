# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_item_purchase_dto import BatchItemPurchaseDto
from openapi_server.models.page_result_purchase_query_dto import PageResultPurchaseQueryDto
from openapi_server.models.purchase_dto import PurchaseDto


pytestmark = pytest.mark.asyncio

async def test_purchases_delete(client):
    """Test case for purchases_delete

    Removes an existing Purchase.
    """
    params = [('timestamp', 'timestamp_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/purchases/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_purchases_get(client):
    """Test case for purchases_get

    Returns a list of company's Purchases. Supports OData querying protocol.  Filtering is allowed by \"entryDate\" field.  Ordering is allowed by \"id\" field.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/purchases',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_purchases_post(client):
    """Test case for purchases_post

    Creates a new Purchase.
    """
    body = {"acCode":"SUP3","acEntries":[{"accountCode":"PU03","analysisCategoryId":10441,"description":"PUR 3","id":12518,"value":90.91}],"bookTranTypeId":4,"customFields":[],"detailCollection":[],"entryDate":"2016-06-01T00:00:00","id":13380,"isDiscrepancyAccepted":False,"netGoods":0,"netServices":0,"note":"Supplier 3","postponedAccounting":False,"procDate":"2016-06-24T00:00:00","reference":"000001","supplierId":10173,"timestamp":"QN/iu9RD2wg=","total":100,"totalNet":90.91,"totalVAT":9.09,"unallocated":100,"unpaid":100,"vatEntries":[{"amount":90.91,"id":12267,"percentage":10,"vatRateId":10317}],"vatTypeId":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/purchases',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_purchases_process_batch(client):
    """Test case for purchases_process_batch

    Processes a batch of Purchases.
    """
    body = [openapi_server.BatchItemPurchaseDto()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/purchases/batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_purchases_put(client):
    """Test case for purchases_put

    Updates an existing Purchase.
    """
    body = {"acCode":"SUP3","acEntries":[{"accountCode":"PU03","analysisCategoryId":10441,"description":"PUR 3","id":12518,"value":90.91}],"bookTranTypeId":4,"customFields":[],"detailCollection":[],"entryDate":"2016-06-01T00:00:00","id":13380,"isDiscrepancyAccepted":False,"netGoods":0,"netServices":0,"note":"Supplier 3","postponedAccounting":False,"procDate":"2016-06-24T00:00:00","reference":"000001","supplierId":10173,"timestamp":"QN/iu9RD2wg=","total":100,"totalNet":90.91,"totalVAT":9.09,"unallocated":100,"unpaid":100,"vatEntries":[{"amount":90.91,"id":12267,"percentage":10,"vatRateId":10317}],"vatTypeId":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/purchases/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_purchases_id_get(client):
    """Test case for v1_purchases_id_get

    Returns information about a single Purchases.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/purchases/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

