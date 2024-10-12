# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.page_result_sales_query_dto import PageResultSalesQueryDto


pytestmark = pytest.mark.asyncio

async def test_sales_get(client):
    """Test case for sales_get

    Returns a list of company's Sales Entries, Sales Invoices and Sales Credit Notes. Supports OData querying protocol.  Filtering is allowed by \"entryDate\" field.  Ordering is allowed by \"id\" field.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sales',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

