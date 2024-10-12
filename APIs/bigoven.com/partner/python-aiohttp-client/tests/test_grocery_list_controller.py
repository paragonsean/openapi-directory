# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api2_controllers_web_api_grocery_list_controller_department_model import API2ControllersWebAPIGroceryListControllerDepartmentModel
from openapi_server.models.api2_controllers_web_api_grocery_list_controller_post_grocery_list_add_line_request import API2ControllersWebAPIGroceryListControllerPostGroceryListAddLineRequest
from openapi_server.models.api2_controllers_web_api_grocery_list_controller_post_grocery_list_recipe_request import API2ControllersWebAPIGroceryListControllerPostGroceryListRecipeRequest
from openapi_server.models.api2_controllers_web_api_grocery_list_controller_post_grocery_list_sync_request import API2ControllersWebAPIGroceryListControllerPostGroceryListSyncRequest
from openapi_server.models.api2_controllers_web_api_grocery_list_controller_post_to_grocery_list_recipe_request import API2ControllersWebAPIGroceryListControllerPostToGroceryListRecipeRequest
from openapi_server.models.api2_controllers_web_api_grocery_list_controller_update_item_by_guid_request import API2ControllersWebAPIGroceryListControllerUpdateItemByGuidRequest
from openapi_server.models.api2_grocery_list_department_result import API2GroceryListDepartmentResult
from openapi_server.models.big_oven_model_api2_grocery_list import BigOvenModelAPI2GroceryList
from openapi_server.models.big_oven_model_shopping_list_line import BigOvenModelShoppingListLine


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_grocery_list_add_recipe(client):
    """Test case for grocery_list_add_recipe

    Add a Recipe to the grocery list.  In the request data, pass in recipeId, scale (scale=1.0 says to keep the recipe the same size as originally posted), markAsPending (true/false) to indicate that              the lines in the recipe should be marked in a \"pending\" (unconfirmed by user) state.
    """
    body = openapi_server.API2ControllersWebAPIGroceryListControllerPostGroceryListRecipeRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/grocerylist/recipe',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_grocery_list_delete(client):
    """Test case for grocery_list_delete

    Delete all the items on a grocery list; faster operation than a sync with deleted items.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/grocerylist',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_grocery_list_delete_item_by_guid(client):
    """Test case for grocery_list_delete_item_by_guid

    /grocerylist/item/{guid}  DELETE will delete this item assuming you own it.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='DELETE',
        path='/grocerylist/item/{guid}'.format(guid='guid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_grocery_list_department(client):
    """Test case for grocery_list_department

    Departmentalize a list of strings -- used for ad-hoc grocery list item addition
    """
    body = openapi_server.API2ControllersWebAPIGroceryListControllerDepartmentModel()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/grocerylist/department',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_grocery_list_get(client):
    """Test case for grocery_list_get

    Get the user's grocery list.  User is determined by Basic Authentication.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/grocerylist',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_grocery_list_grocery_list_item_guid(client):
    """Test case for grocery_list_grocery_list_item_guid

    Update a grocery item by GUID
    """
    body = openapi_server.API2ControllersWebAPIGroceryListControllerUpdateItemByGuidRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/grocerylist/item/{guid}'.format(guid='guid_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_grocery_list_grocery_list_remove_marked_items(client):
    """Test case for grocery_list_grocery_list_remove_marked_items

    Clears the checked lines.
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/grocerylist/clearcheckedlines',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_grocery_list_post(client):
    """Test case for grocery_list_post

    Add a single line item to the grocery list
    """
    body = openapi_server.API2ControllersWebAPIGroceryListControllerPostGroceryListAddLineRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/grocerylist/line',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_grocery_list_post_grocery_list_sync(client):
    """Test case for grocery_list_post_grocery_list_sync

    Synchronize the grocery list.  Call this with a POST to /grocerylist/sync
    """
    body = openapi_server.API2ControllersWebAPIGroceryListControllerPostGroceryListSyncRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/grocerylist/sync',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("Connexion does not support multiple consumes. See https://github.com/zalando/connexion/pull/760")
async def test_grocerylist_item_post(client):
    """Test case for grocerylist_item_post

    Add a single line item to the grocery list
    """
    body = openapi_server.API2ControllersWebAPIGroceryListControllerPostToGroceryListRecipeRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/grocerylist/item',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

