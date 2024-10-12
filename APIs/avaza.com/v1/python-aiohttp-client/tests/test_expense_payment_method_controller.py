# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.expense_payment_method_dropdown_list import ExpensePaymentMethodDropdownList


pytestmark = pytest.mark.asyncio

async def test_expense_payment_method_lookup(client):
    """Test case for expense_payment_method_lookup

    Gets minimal list of Expense Payment Methods.
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ExpensePaymentMethod/Lookup',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

