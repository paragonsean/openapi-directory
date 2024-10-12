# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.expense_category_list import ExpenseCategoryList


pytestmark = pytest.mark.asyncio

async def test_expense_category_get(client):
    """Test case for expense_category_get

    Gets list of Expense Categories
    """
    params = [('isEnabled', True)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ExpenseCategory',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

