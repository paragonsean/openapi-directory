# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.data_connection import DataConnection


pytestmark = pytest.mark.asyncio

async def test_create_partner_expense_connection(client):
    """Test case for create_partner_expense_connection

    Create Partner Expense connection
    """
    headers = { 
        'Accept': 'application/json',
        'auth_header': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/companies/{company_id}/sync/expenses/connections/partnerExpense'.format(company_id='8a210b68-6988-11ed-a1eb-0242ac120002'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

