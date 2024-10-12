# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.expense_lines_expense_line_id_get200_response import ExpenseLinesExpenseLineIdGet200Response
from openapi_server.models.expense_lines_get200_response import ExpenseLinesGet200Response
from openapi_server.models.expense_lines_post_request import ExpenseLinesPostRequest


pytestmark = pytest.mark.asyncio

async def test_expense_lines_expense_line_id_delete(client):
    """Test case for expense_lines_expense_line_id_delete

    Delete expense line
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/expense_lines/{expense_line_id}'.format(expense_line_id='expense_line_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expense_lines_expense_line_id_get(client):
    """Test case for expense_lines_expense_line_id_get

    Show expense line
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/expense_lines/{expense_line_id}'.format(expense_line_id='expense_line_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expense_lines_expense_line_id_put(client):
    """Test case for expense_lines_expense_line_id_put

    Edit expense line
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/expense_lines/{expense_line_id}'.format(expense_line_id='expense_line_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expense_lines_get(client):
    """Test case for expense_lines_get

    Show list of expense lines
    """
    params = [('created_by_id', 'created_by_id_example'),
                    ('currency_id', 'currency_id_example'),
                    ('expense_id', 'expense_id_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/expense_lines',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expense_lines_post(client):
    """Test case for expense_lines_post

    Add line to expense
    """
    body = openapi_server.ExpenseLinesPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/expense_lines',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

