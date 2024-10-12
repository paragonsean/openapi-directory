# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.patch_operation import PatchOperation
from openapi_server.models.project_travel_expense_input_model import ProjectTravelExpenseInputModel
from openapi_server.models.project_travel_expense_output_model import ProjectTravelExpenseOutputModel
from openapi_server.models.travel_reimbursement_input_model import TravelReimbursementInputModel
from openapi_server.models.travel_reimbursement_output_model import TravelReimbursementOutputModel


pytestmark = pytest.mark.asyncio

async def test_project_travel_expenses_patch_project_travel_expense(client):
    """Test case for project_travel_expenses_patch_project_travel_expense

    Update (Patch) a project travel expense or a part of it.
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/projecttravelexpenses/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_travel_expenses_post_project_travel_expense(client):
    """Test case for project_travel_expenses_post_project_travel_expense

    Insert a project travel expense.
    """
    body = {"vatRate":5.637376656633329,"description":"description","project":{"guid":"guid"},"invoiceRowDescription":"invoiceRowDescription","travelReimbursementRequired":True,"travelReimbursement":{"guid":"guid"},"phase":{"guid":"guid"},"travelStartTime":"2000-01-23T04:56:07.000+00:00","unitPrice":{"amount":5.962133916683182,"currencyCode":"currencyCode"},"salesAccount":{"guid":"guid"},"quantity":1.4658129805029452,"billingSchedule":"Immediately","costCenter":{"guid":"guid"},"billingDependencyPhase":{"guid":"guid"},"travelEndTime":"2000-01-23T04:56:07.000+00:00","plannedBillingDate":"2000-01-23","measurementUnit":"measurementUnit","isBillable":True,"invoiceQuantity":0.8008281904610115,"travelExpense":{"guid":"guid"},"purchaseVatRate":6.027456183070403,"unitCost":{"amount":5.962133916683182,"currencyCode":"currencyCode"},"costAccount":{"guid":"guid"},"invoice":{"guid":"guid"},"invoiceRowComment":"invoiceRowComment","user":{"guid":"guid"},"eventDate":"2000-01-23"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/projecttravelexpenses',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_travel_reimbursements_patch_travel_reimbursement(client):
    """Test case for travel_reimbursements_patch_travel_reimbursement

    Update (Patch) a travel reimbursement
    """
    body = {"op":"Add","path":"path","from":"from","value":"value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/rest-api/v1/travelreimbursements/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_travel_reimbursements_post_travel_reimbursement(client):
    """Test case for travel_reimbursements_post_travel_reimbursement

    Add a travel reimbursement
    """
    body = {"travelReimbursementStatus":{"guid":"guid"},"advancePayment":{"amount":6.027456183070403,"currencyCode":"currencyCode"},"groupBy":"None","title":"title","user":{"name":"name","guid":"guid"}}
    params = [('addAllUnreimbursedTravelExpenses', True),
                    ('includedProjectTravelExpenses', ['included_project_travel_expenses_example'])]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/rest-api/v1/travelreimbursements',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

