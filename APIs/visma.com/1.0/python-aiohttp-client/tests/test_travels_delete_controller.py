# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.exception_model import ExceptionModel


pytestmark = pytest.mark.asyncio

async def test_project_travel_expenses_delete_project_travel_expense(client):
    """Test case for project_travel_expenses_delete_project_travel_expense

    Deletes a project travel expense.
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/projecttravelexpenses/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_travel_reimbursements_delete_travel_reimbursement(client):
    """Test case for travel_reimbursements_delete_travel_reimbursement

    Delete a travel reimbursement
    """
    headers = { 
        'Accept': 'application/json',
        'ClientIdAuth': 'special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/rest-api/v1/travelreimbursements/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

