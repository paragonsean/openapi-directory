# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.batch_item_sale_reps_dto import BatchItemSaleRepsDto
from openapi_server.models.page_result_sale_reps_dto import PageResultSaleRepsDto
from openapi_server.models.sale_reps_dto import SaleRepsDto


pytestmark = pytest.mark.asyncio

async def test_sales_rep_delete(client):
    """Test case for sales_rep_delete

    Removes an existing Sale Rep.
    """
    params = [('timestamp', 'timestamp_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/salesReps/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_rep_get(client):
    """Test case for sales_rep_get

    Returns a list of company's SaleRep.  Filtering is forbidden.  Ordering is allowed by \"id\".
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/salesReps',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_rep_post(client):
    """Test case for sales_rep_post

    Creates a new SaleRep.
    """
    body = {"code":"SR0001","companyId":123456,"email":"example@gmail.com","id":1,"name":"Sales Rep 1","phone":"1234567890","timeStamp":"SGcLvNRD2wg="}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/salesReps',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_rep_process_batch(client):
    """Test case for sales_rep_process_batch

    Processes a batch of Sale Rep.
    """
    body = [openapi_server.BatchItemSaleRepsDto()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/salesReps/batch',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_sales_rep_put(client):
    """Test case for sales_rep_put

    Updates an existing Sale Rep.
    """
    body = {"code":"SR0001","companyId":123456,"email":"example@gmail.com","id":1,"name":"Sales Rep 1","phone":"1234567890","timeStamp":"SGcLvNRD2wg="}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/salesReps/{id}'.format(id=56),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_v1_sales_reps_id_get(client):
    """Test case for v1_sales_reps_id_get

    Returns information about a single SaleRep.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/salesReps/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

