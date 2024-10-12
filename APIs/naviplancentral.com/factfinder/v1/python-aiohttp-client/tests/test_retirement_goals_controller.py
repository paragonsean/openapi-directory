# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.retirement_expense_model import RetirementExpenseModel
from openapi_server.models.retirement_expense_with_id_model import RetirementExpenseWithIdModel
from openapi_server.models.retirement_expenses_model import RetirementExpensesModel
from openapi_server.models.retirement_goal_model import RetirementGoalModel
from openapi_server.models.retirement_goal_with_id_model import RetirementGoalWithIdModel
from openapi_server.models.retirement_goals_model import RetirementGoalsModel


pytestmark = pytest.mark.asyncio

async def test_retirement_goals_delete_by_id(client):
    """Test case for retirement_goals_delete_by_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/factfinder/api/RetirementGoals/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retirement_goals_delete_by_retirementgoalid_id(client):
    """Test case for retirement_goals_delete_by_retirementgoalid_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/factfinder/api/RetirementGoals/{retirement_goal_id}/Expenses/{id}'.format(retirement_goal_id=56, id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retirement_goals_get_by_id(client):
    """Test case for retirement_goals_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/RetirementGoals/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retirement_goals_get_retirement_expense_by_retirementgoalid_id(client):
    """Test case for retirement_goals_get_retirement_expense_by_retirementgoalid_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/RetirementGoals/{retirement_goal_id}/Expenses/{id}'.format(retirement_goal_id=56, id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retirement_goals_get_retirement_expenses_by_retirement_goal_id_by_retirementgoalid(client):
    """Test case for retirement_goals_get_retirement_expenses_by_retirement_goal_id_by_retirementgoalid

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/RetirementGoals/{retirement_goal_id}/Expenses'.format(retirement_goal_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_retirement_goals_get_retirement_goals_by_fact_finder_id_by_factfinderid(client):
    """Test case for retirement_goals_get_retirement_goals_by_fact_finder_id_by_factfinderid

    
    """
    params = [('factFinderId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/RetirementGoals',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_retirement_goals_post_by_model(client):
    """Test case for retirement_goals_post_by_model

    
    """
    model = {"factFinderId":0,"head2RetirementDate":"2000-01-23T04:56:07.000+00:00","externalDestinationId":"externalDestinationId","head1RetirementDate":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/factfinder/api/RetirementGoals',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_retirement_goals_post_by_retirementgoalid_model(client):
    """Test case for retirement_goals_post_by_retirementgoalid_model

    
    """
    model = {"amount":0.8008281904610115,"annualPeriod":60,"endDate":"2000-01-23T04:56:07.000+00:00","member":"Client","description":"description","externalDestinationId":"externalDestinationId","startDate":"2000-01-23T04:56:07.000+00:00","frequency":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/factfinder/api/RetirementGoals/{retirement_goal_id}/Expenses'.format(retirement_goal_id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_retirement_goals_put_by_id_model(client):
    """Test case for retirement_goals_put_by_id_model

    
    """
    model = {"factFinderId":0,"head2RetirementDate":"2000-01-23T04:56:07.000+00:00","externalDestinationId":"externalDestinationId","head1RetirementDate":"2000-01-23T04:56:07.000+00:00"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/factfinder/api/RetirementGoals/{id}'.format(id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_retirement_goals_put_by_retirementgoalid_id_model(client):
    """Test case for retirement_goals_put_by_retirementgoalid_id_model

    
    """
    model = {"amount":0.8008281904610115,"annualPeriod":60,"endDate":"2000-01-23T04:56:07.000+00:00","member":"Client","description":"description","externalDestinationId":"externalDestinationId","startDate":"2000-01-23T04:56:07.000+00:00","frequency":1}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/factfinder/api/RetirementGoals/{retirement_goal_id}/Expenses/{id}'.format(retirement_goal_id=56, id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

