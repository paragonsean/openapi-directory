# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bad_request_response import BadRequestResponse
from openapi_server.models.bulk_action_request_body import BulkActionRequestBody
from openapi_server.models.clocking_records_post201_response import ClockingRecordsPost201Response
from openapi_server.models.empty_success_response import EmptySuccessResponse
from openapi_server.models.error_not_found import ErrorNotFound
from openapi_server.models.error_validation import ErrorValidation
from openapi_server.models.expenses_expense_id_get200_response import ExpensesExpenseIdGet200Response
from openapi_server.models.expenses_get200_response import ExpensesGet200Response
from openapi_server.models.expenses_highest_amount_get200_response import ExpensesHighestAmountGet200Response
from openapi_server.models.expenses_post_request import ExpensesPostRequest


pytestmark = pytest.mark.asyncio

async def test_bulk_delete_expenses(client):
    """Test case for bulk_delete_expenses

    Bulk delete expenses
    """
    body = {"id":["id","id"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/expenses/bulkDelete',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expenses_expense_id_delete(client):
    """Test case for expenses_expense_id_delete

    Delete expense
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/expenses/{expense_id}'.format(expense_id='expense_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expenses_expense_id_get(client):
    """Test case for expenses_expense_id_get

    Show expense
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/expenses/{expense_id}'.format(expense_id='expense_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expenses_expense_id_put(client):
    """Test case for expenses_expense_id_put

    Edit expense
    """
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/expenses/{expense_id}'.format(expense_id='expense_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expenses_get(client):
    """Test case for expenses_get

    Show list of expenses
    """
    params = [('created_by_id', 'created_by_id_example'),
                    ('company_id', 'company_id_example'),
                    ('contact_id', 'contact_id_example'),
                    ('project_id', 'project_id_example'),
                    ('due_date', 'due_date_example'),
                    ('gt_created', '2013-10-20'),
                    ('lt_created', '2013-10-20'),
                    ('status', 'status_example'),
                    ('is_imported', True),
                    ('min_amount', 3.4),
                    ('max_amount', 3.4),
                    ('projects', 'projects_example')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/expenses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expenses_highest_amount_get(client):
    """Test case for expenses_highest_amount_get

    Show highest Expense amount(`total_selling_price`)
    """
    params = [('gt_created', '2013-10-20'),
                    ('lt_created', '2013-10-20')]
    headers = { 
        'Accept': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/expenses/highest_amount',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expenses_post(client):
    """Test case for expenses_post

    Add line to expense
    """
    body = openapi_server.ExpensesPostRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/expenses',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_send_emails_expenses(client):
    """Test case for send_emails_expenses

    Bulk delete expenses
    """
    body = {"id":["id","id"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'api_key': 'special-key',
        'X-Auth-Token': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/v1/expenses/sendEmails',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

