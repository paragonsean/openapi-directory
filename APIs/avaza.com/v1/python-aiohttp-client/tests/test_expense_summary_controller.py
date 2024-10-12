# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.expense_summary_result import ExpenseSummaryResult


pytestmark = pytest.mark.asyncio

async def test_expense_summary_get(client):
    """Test case for expense_summary_get

    Gets Basic Summary of Expense Statistics
    """
    params = [('model.groupBy', ['model_group_by_example']),
                    ('model.expenseDateFrom', '2013-10-20T19:20:30+01:00'),
                    ('model.expenseDateTo', '2013-10-20T19:20:30+01:00'),
                    ('model.userID', [56]),
                    ('model.projectID', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/ExpenseSummary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

