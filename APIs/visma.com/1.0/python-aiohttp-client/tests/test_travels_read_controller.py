# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.deleted_project_travel_expense_model import DeletedProjectTravelExpenseModel
from openapi_server.models.exception_model import ExceptionModel
from openapi_server.models.expenses_class import ExpensesClass
from openapi_server.models.project_travel_expense_output_model import ProjectTravelExpenseOutputModel
from openapi_server.models.travel_reimbursement_output_model import TravelReimbursementOutputModel


pytestmark = pytest.mark.asyncio

async def test_project_travel_expenses_get_deleted_project_travel_expenses(client):
    """Test case for project_travel_expenses_get_deleted_project_travel_expenses

    Get the deleted project travel expenses.
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('projectGuid', ['project_guid_example']),
                    ('userGuid', ['user_guid_example']),
                    ('deletedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/deletedprojecttravelexpenses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_travel_expenses_get_project_travel_expense(client):
    """Test case for project_travel_expenses_get_project_travel_expense

    Get project travel expense by ID.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projecttravelexpenses/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_travel_expenses_get_project_travel_expenses(client):
    """Test case for project_travel_expenses_get_project_travel_expenses

    Get the project travel expenses.
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('changedSince', '2013-10-20T19:20:30+01:00')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projecttravelexpenses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_travel_expenses_get_project_travel_expenses_for_project(client):
    """Test case for project_travel_expenses_get_project_travel_expenses_for_project

    Get all the project travel expenses for a project
    """
    params = [('isBillable', True),
                    ('isBilled', True),
                    ('invoiceableDate', '2013-10-20T19:20:30+01:00'),
                    ('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('isBillablePeriodInFuture', True),
                    ('expenseClass', openapi_server.ExpensesClass())]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/projects/{project_guid}/projecttravelexpenses'.format(project_guid='project_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_travel_expenses_get_project_travel_expenses_for_travel_reimbursement(client):
    """Test case for project_travel_expenses_get_project_travel_expenses_for_travel_reimbursement

    Get all the project travel expenses for a travel reimbursement
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('expenseClass', openapi_server.ExpensesClass())]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/travelreimbursements/{travel_reimbursement_guid}/projecttravelexpenses'.format(travel_reimbursement_guid='travel_reimbursement_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_project_travel_expenses_get_project_travel_expenses_for_user(client):
    """Test case for project_travel_expenses_get_project_travel_expenses_for_user

    Get all the project travel expenses for a user
    """
    params = [('startDate', '2013-10-20'),
                    ('endDate', '2013-10-20'),
                    ('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('expenseClass', openapi_server.ExpensesClass()),
                    ('isReimbursed', True),
                    ('isTravelReimbursementRequired', True),
                    ('travelReimbursementGuid', 'travel_reimbursement_guid_example'),
                    ('costCurrencyGuid', 'cost_currency_guid_example')]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/users/{user_guid}/projecttravelexpenses'.format(user_guid='user_guid_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_travel_reimbursements_get_travel_reimbursement(client):
    """Test case for travel_reimbursements_get_travel_reimbursement

    Get travel reimbursement by ID
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/travelreimbursements/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_travel_reimbursements_get_travel_reimbursements(client):
    """Test case for travel_reimbursements_get_travel_reimbursements

    Get travel reimbursements.
    """
    params = [('pageToken', 'page_token_example'),
                    ('rowCount', 56),
                    ('changedSince', '2013-10-20T19:20:30+01:00'),
                    ('travelReimbursementStatusGuids', ['travel_reimbursement_status_guids_example'])]
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/rest-api/v1/travelreimbursements',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

