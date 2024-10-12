# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.education_expense_model import EducationExpenseModel
from openapi_server.models.education_expense_with_id_model import EducationExpenseWithIdModel
from openapi_server.models.education_expenses_model import EducationExpensesModel
from openapi_server.models.education_goal_model import EducationGoalModel
from openapi_server.models.education_goal_with_id_model import EducationGoalWithIdModel
from openapi_server.models.education_goals_model import EducationGoalsModel


pytestmark = pytest.mark.asyncio

async def test_education_goals_delete_by_educationgoalid_id(client):
    """Test case for education_goals_delete_by_educationgoalid_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/factfinder/api/EducationGoals/{education_goal_id}/Expenses/{id}'.format(education_goal_id=56, id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_education_goals_delete_by_id(client):
    """Test case for education_goals_delete_by_id

    
    """
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/factfinder/api/EducationGoals/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_education_goals_get_by_id(client):
    """Test case for education_goals_get_by_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/EducationGoals/{id}'.format(id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_education_goals_get_education_expense_by_educationgoalid_id(client):
    """Test case for education_goals_get_education_expense_by_educationgoalid_id

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/EducationGoals/{education_goal_id}/Expenses/{id}'.format(education_goal_id=56, id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_education_goals_get_education_expenses_by_education_goal_id_by_educationgoalid(client):
    """Test case for education_goals_get_education_expenses_by_education_goal_id_by_educationgoalid

    
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/EducationGoals/{education_goal_id}/Expenses'.format(education_goal_id=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_education_goals_get_education_goals_by_fact_finder_id_by_factfinderid(client):
    """Test case for education_goals_get_education_goals_by_fact_finder_id_by_factfinderid

    
    """
    params = [('factFinderId', 56)]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/factfinder/api/EducationGoals',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_education_goals_post_by_educationgoalid_model(client):
    """Test case for education_goals_post_by_educationgoalid_model

    
    """
    model = {"annualCost":0.8008281904610115,"memberDependentId":6,"member":"Client","startYear":"2000-01-23T04:56:07.000+00:00","externalDestinationId":"externalDestinationId","years":15}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/factfinder/api/EducationGoals/{education_goal_id}/Expenses'.format(education_goal_id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_education_goals_post_by_model(client):
    """Test case for education_goals_post_by_model

    
    """
    model = {"factFinderId":0,"projectedCost":6.027456183070403,"description":"description","externalDestinationId":"externalDestinationId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/factfinder/api/EducationGoals',
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_education_goals_put_by_educationgoalid_id_model(client):
    """Test case for education_goals_put_by_educationgoalid_id_model

    
    """
    model = {"annualCost":0.8008281904610115,"memberDependentId":6,"member":"Client","startYear":"2000-01-23T04:56:07.000+00:00","externalDestinationId":"externalDestinationId","years":15}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/factfinder/api/EducationGoals/{education_goal_id}/Expenses/{id}'.format(education_goal_id=56, id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_education_goals_put_by_id_model(client):
    """Test case for education_goals_put_by_id_model

    
    """
    model = {"factFinderId":0,"projectedCost":6.027456183070403,"description":"description","externalDestinationId":"externalDestinationId"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/factfinder/api/EducationGoals/{id}'.format(id=56),
        headers=headers,
        json=model,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

