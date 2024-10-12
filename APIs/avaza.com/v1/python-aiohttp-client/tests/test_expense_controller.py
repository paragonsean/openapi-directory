# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.expense_attachment_request import ExpenseAttachmentRequest
from openapi_server.models.expense_attachment_upload_result import ExpenseAttachmentUploadResult
from openapi_server.models.expense_delete_result_set import ExpenseDeleteResultSet
from openapi_server.models.expense_details import ExpenseDetails
from openapi_server.models.expense_list import ExpenseList
from openapi_server.models.new_expense import NewExpense
from openapi_server.models.update_expense import UpdateExpense


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_expense_approval(client):
    """Test case for expense_approval

    Submit Expenses for Approval.
    """
    expense_ids = [56]
    params = [('UserID', 56),
                    ('SendNotifications', True)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/ExpenseApproval/Submit',
        headers=headers,
        json=expense_ids,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/form-data not supported by Connexion")
async def test_expense_attachment(client):
    """Test case for expense_attachment

    
    """
    body = openapi_server.ExpenseAttachmentRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/form-data',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/Expense/Attachment',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_expense_delete(client):
    """Test case for expense_delete

    Delete a Timesheet Entry
    """
    expense_ids = [56]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/api/Expense',
        headers=headers,
        json=expense_ids,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expense_get(client):
    """Test case for expense_get

    Gets list of Expenses
    """
    params = [('UpdatedAfter', '2013-10-20T19:20:30+01:00'),
                    ('ExpenseDateFrom', '2013-10-20T19:20:30+01:00'),
                    ('ExpenseDateTo', '2013-10-20T19:20:30+01:00'),
                    ('UserEmail', 'user_email_example'),
                    ('UserID', 56),
                    ('CategoryName', 'category_name_example'),
                    ('CustomerID', 56),
                    ('ProjectID', 56),
                    ('isChargeable', True),
                    ('isInvoiced', True),
                    ('ExpenseReimbursementIDFK', 56),
                    ('ExpensePaymentMethodIDFK', 56),
                    ('ExpenseApprovalStatusCode', 'expense_approval_status_code_example'),
                    ('Search', 'search_example'),
                    ('pageSize', 56),
                    ('pageNumber', 56),
                    ('Sort', 'sort_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Expense',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expense_get_by_id(client):
    """Test case for expense_get_by_id

    Gets an Expense Entry by Expense ID
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/Expense/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_expense_post(client):
    """Test case for expense_post

    Create an Expense
    """
    model = {"ExchangeRate":1.4658129805029452,"ExpenseCategoryIDFK":5,"ProjectName":"ProjectName","ProjectIDFK":7,"UserEmail":"UserEmail","ExpensePaymentMethodIDFK":5,"GroupTripName":"GroupTripName","VerifyAndSave":True,"CurrencyCode":"CurrencyCode","Merchant":"Merchant","CustomerName":"CustomerName","Notes":"Notes","FileAttachmentIDs":[2,2],"isReimbursable":True,"TaxIDFK":2,"Amount":0.8008281904610115,"TaskIDFK":3,"TaxName":"TaxName","MerchantTaxNumber":"MerchantTaxNumber","Quantity":9.301444243932576,"isChargeable":True,"CustomerIDFK":6,"ExpenseDate":"2000-01-23T04:56:07.000+00:00","ExpenseCategoryName":"ExpenseCategoryName","UserIDFK":4,"TransactionTaxConfigCode":"TransactionTaxConfigCode"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/Expense',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_expense_put(client):
    """Test case for expense_put

    Update an Expense
    """
    model = {"isReimbursable":True,"ExchangeRate":1.4658129805029452,"ExpenseCategoryIDFK":5,"FieldsToUpdate":["FieldsToUpdate","FieldsToUpdate"],"ExpenseID":5,"TaxIDFK":4,"Amount":0.8008281904610115,"ProjectIDFK":9,"TaskIDFK":2,"MerchantTaxNumber":"MerchantTaxNumber","Quantity":3.616076749251911,"ExpensePaymentMethodIDFK":2,"GroupTripName":"GroupTripName","VerifyAndSave":True,"isChargeable":True,"CurrencyCode":"CurrencyCode","CustomerIDFK":6,"ExpenseDate":"2000-01-23T04:56:07.000+00:00","Merchant":"Merchant","Notes":"Notes","FileAttachmentIDs":[7,7],"TransactionTaxConfigCode":"TransactionTaxConfigCode"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/Expense',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

