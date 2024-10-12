# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customer_dto_paged_result import CustomerDtoPagedResult
from openapi_server.models.customer_location_item_dto import CustomerLocationItemDto
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_customers_get_customer_location_list_customer_idlocations(client):
    """Test case for customers_get_customer_location_list_customer_idlocations

    Gets a list of locations for the specified customer
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/Customers/{customer_id}/locations'.format(customer_id='customer_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_customers_get_list(client):
    """Test case for customers_get_list

    Gets a list of customers
    """
    params = [('filter', 'filter_example'),
                    ('pageSize', 100),
                    ('pageIndex', 0)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/Customers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

