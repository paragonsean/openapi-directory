# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.customers import Customers


pytestmark = pytest.mark.asyncio

async def test_list_customers(client):
    """Test case for list_customers

    List customers
    """
    params = [('page', 1),
                    ('pageSize', 100),
                    ('query', 'query_example'),
                    ('orderBy', '-modifiedDate')]
    headers = { 
        'Accept': 'application/json',
        'auth_header': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/companies/{company_id}/connections/{connection_id}/data/commerce-customers',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

