# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.expense_group_dropdown_list import ExpenseGroupDropdownList


pytestmark = pytest.mark.asyncio

async def test_expense_group_lookup(client):
    """Test case for expense_group_lookup

    Gets minimal list of Expense Groups.
    """
    params = [('pageSize', 56),
                    ('pageNumber', 56),
                    ('search', 'search_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ExpenseGroup/Lookup',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

