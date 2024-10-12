# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.add_meal_plan_template200_response import AddMealPlanTemplate200Response
from openapi_server.models.add_to_meal_plan_request import AddToMealPlanRequest
from openapi_server.models.add_to_meal_plan_request1 import AddToMealPlanRequest1
from openapi_server.models.add_to_shopping_list200_response import AddToShoppingList200Response
from openapi_server.models.add_to_shopping_list_request import AddToShoppingListRequest
from openapi_server.models.clear_meal_plan_day_request import ClearMealPlanDayRequest
from openapi_server.models.connect_user200_response import ConnectUser200Response
from openapi_server.models.connect_user_request import ConnectUserRequest
from openapi_server.models.delete_from_meal_plan_request import DeleteFromMealPlanRequest
from openapi_server.models.generate_meal_plan200_response import GenerateMealPlan200Response
from openapi_server.models.generate_shopping_list_request import GenerateShoppingListRequest
from openapi_server.models.get_meal_plan_template200_response import GetMealPlanTemplate200Response
from openapi_server.models.get_meal_plan_templates200_response import GetMealPlanTemplates200Response
from openapi_server.models.get_meal_plan_week200_response import GetMealPlanWeek200Response
from openapi_server.models.get_shopping_list200_response import GetShoppingList200Response


pytestmark = pytest.mark.asyncio

@pytest.mark.skip(" not supported by Connexion")
async def test_add_meal_plan_template(client):
    """Test case for add_meal_plan_template

    Add Meal Plan Template
    """
    body = openapi_server.AddToMealPlanRequest()
    params = [('hash', '4b5v4398573406')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': '',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/mealplanner/{username}/templates'.format(username='dsky'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_add_to_meal_plan(client):
    """Test case for add_to_meal_plan

    Add to Meal Plan
    """
    body = openapi_server.AddToMealPlanRequest()
    params = [('hash', 'hash_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': '',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/mealplanner/{username}/items'.format(username='dsky'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_add_to_shopping_list(client):
    """Test case for add_to_shopping_list

    Add to Shopping List
    """
    body = openapi_server.AddToMealPlanRequest()
    params = [('hash', 'hash_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': '',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/mealplanner/{username}/shopping-list/items'.format(username='dsky'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip(" not supported by Connexion")
async def test_clear_meal_plan_day(client):
    """Test case for clear_meal_plan_day

    Clear Meal Plan Day
    """
    body = openapi_server.ClearMealPlanDayRequest()
    params = [('hash', 'hash_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': '',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/mealplanner/{username}/day/{_date}'.format(username='dsky', _date='2020-06-01'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_connect_user(client):
    """Test case for connect_user

    Connect User
    """
    body = None
    headers = { 
        'Accept': 'application/json',
        'Content-Type': '',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/users/connect',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip(" not supported by Connexion")
async def test_delete_from_meal_plan(client):
    """Test case for delete_from_meal_plan

    Delete from Meal Plan
    """
    body = openapi_server.DeleteFromMealPlanRequest()
    params = [('hash', 'hash_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': '',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/mealplanner/{username}/items/{id}'.format(username='dsky', id=15678),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip(" not supported by Connexion")
async def test_delete_from_shopping_list(client):
    """Test case for delete_from_shopping_list

    Delete from Shopping List
    """
    body = openapi_server.DeleteFromMealPlanRequest()
    params = [('hash', 'hash_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': '',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/mealplanner/{username}/shopping-list/items/{id}'.format(username='dsky', id=1),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip(" not supported by Connexion")
async def test_delete_meal_plan_template(client):
    """Test case for delete_meal_plan_template

    Delete Meal Plan Template
    """
    body = openapi_server.DeleteFromMealPlanRequest()
    params = [('hash', '4b5v4398573406')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': '',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/mealplanner/{username}/templates/{id}'.format(username='dsky', id=1),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_generate_meal_plan(client):
    """Test case for generate_meal_plan

    Generate Meal Plan
    """
    params = [('timeFrame', 'day'),
                    ('targetCalories', 2000),
                    ('diet', 'vegetarian'),
                    ('exclude', 'shellfish, olives')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/mealplanner/generate',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip(" not supported by Connexion")
async def test_generate_shopping_list(client):
    """Test case for generate_shopping_list

    Generate Shopping List
    """
    body = openapi_server.GenerateShoppingListRequest()
    params = [('hash', 'hash_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': '',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/mealplanner/{username}/shopping-list/{start_date}/{end_date}'.format(username='dsky', start_date='2020-06-01', end_date='2020-06-07'),
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_meal_plan_template(client):
    """Test case for get_meal_plan_template

    Get Meal Plan Template
    """
    params = [('hash', 'hash_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/mealplanner/{username}/templates/{id}'.format(username='dsky', id=1),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_meal_plan_templates(client):
    """Test case for get_meal_plan_templates

    Get Meal Plan Templates
    """
    params = [('hash', 'hash_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/mealplanner/{username}/templates'.format(username='dsky'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_meal_plan_week(client):
    """Test case for get_meal_plan_week

    Get Meal Plan Week
    """
    params = [('hash', 'hash_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/mealplanner/{username}/week/{start_date}'.format(username='dsky', start_date='2020-06-01'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_shopping_list(client):
    """Test case for get_shopping_list

    Get Shopping List
    """
    params = [('hash', 'hash_example')]
    headers = { 
        'Accept': 'application/json',
        'apiKeyScheme': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/mealplanner/{username}/shopping-list'.format(username='dsky'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

