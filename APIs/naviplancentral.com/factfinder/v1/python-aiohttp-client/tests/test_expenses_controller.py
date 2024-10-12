# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.expense_model import ExpenseModel
from openapi_server.models.expense_with_id_model import ExpenseWithIdModel
from openapi_server.models.expenses_model import ExpensesModel


pytestmark = pytest.mark.asyncio

async def test_expenses_delete_by_id(client):
    """Test case for expenses_delete_by_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/factfinder/api/Expenses/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expenses_get_by_id(client):
    """Test case for expenses_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/Expenses/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_expenses_get_expenses_by_fact_finder_id_by_factfinderid(client):
    """Test case for expenses_get_expenses_by_fact_finder_id_by_factfinderid

    
    """
    params = [('factFinderId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/Expenses',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_expenses_post_by_model(client):
    """Test case for expenses_post_by_model

    
    """
    model = {"expenseAmount":6.027456183070403,"factFinderId":5,"annualPeriod":8,"endDate":"2000-01-23T04:56:07.000+00:00","member":"Client","description":"description","expenseTypeId":1,"externalDestinationId":"externalDestinationId","startDate":"2000-01-23T04:56:07.000+00:00","frequency":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/factfinder/api/Expenses',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_expenses_put_by_id_model(client):
    """Test case for expenses_put_by_id_model

    
    """
    model = {"expenseAmount":6.027456183070403,"factFinderId":5,"annualPeriod":8,"endDate":"2000-01-23T04:56:07.000+00:00","member":"Client","description":"description","expenseTypeId":1,"externalDestinationId":"externalDestinationId","startDate":"2000-01-23T04:56:07.000+00:00","frequency":5}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/factfinder/api/Expenses/{id}'.format(id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

