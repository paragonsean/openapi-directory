from typing import List, Dict
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
from openapi_server import util


async def add_meal_plan_template(request: web.Request, username, hash, body) -> web.Response:
    """Add Meal Plan Template

    Add a meal plan template for a user.

    :param username: The username.
    :type username: str
    :param hash: The private hash for the username.
    :type hash: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddToMealPlanRequest.from_dict(body)
    return web.Response(status=200)


async def add_to_meal_plan(request: web.Request, username, hash, body) -> web.Response:
    """Add to Meal Plan

    Add an item to the user&#39;s meal plan.

    :param username: The username.
    :type username: str
    :param hash: The private hash for the username.
    :type hash: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddToMealPlanRequest.from_dict(body)
    return web.Response(status=200)


async def add_to_shopping_list(request: web.Request, username, hash, body) -> web.Response:
    """Add to Shopping List

    Add an item to the current shopping list of a user.

    :param username: The username.
    :type username: str
    :param hash: The private hash for the username.
    :type hash: str
    :param body: 
    :type body: dict | bytes

    """
    body = AddToMealPlanRequest.from_dict(body)
    return web.Response(status=200)


async def clear_meal_plan_day(request: web.Request, username, _date, hash, body) -> web.Response:
    """Clear Meal Plan Day

    Delete all planned items from the user&#39;s meal plan for a specific day.

    :param username: The username.
    :type username: str
    :param _date: The date in the format yyyy-mm-dd.
    :type _date: str
    :param hash: The private hash for the username.
    :type hash: str
    :param body: 
    :type body: dict | bytes

    """
    body = ClearMealPlanDayRequest.from_dict(body)
    return web.Response(status=200)


async def connect_user(request: web.Request, body) -> web.Response:
    """Connect User

    In order to call user-specific endpoints, you need to connect your app&#39;s users to spoonacular users.

    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def delete_from_meal_plan(request: web.Request, username, id, hash, body) -> web.Response:
    """Delete from Meal Plan

    Delete an item from the user&#39;s meal plan.

    :param username: The username.
    :type username: str
    :param id: The shopping list item id.
    :type id: 
    :param hash: The private hash for the username.
    :type hash: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteFromMealPlanRequest.from_dict(body)
    return web.Response(status=200)


async def delete_from_shopping_list(request: web.Request, username, id, hash, body) -> web.Response:
    """Delete from Shopping List

    Delete an item from the current shopping list of the user.

    :param username: The username.
    :type username: str
    :param id: The item&#39;s id.
    :type id: int
    :param hash: The private hash for the username.
    :type hash: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteFromMealPlanRequest.from_dict(body)
    return web.Response(status=200)


async def delete_meal_plan_template(request: web.Request, username, id, hash, body) -> web.Response:
    """Delete Meal Plan Template

    Delete a meal plan template for a user.

    :param username: The username.
    :type username: str
    :param id: The item&#39;s id.
    :type id: int
    :param hash: The private hash for the username.
    :type hash: str
    :param body: 
    :type body: dict | bytes

    """
    body = DeleteFromMealPlanRequest.from_dict(body)
    return web.Response(status=200)


async def generate_meal_plan(request: web.Request, time_frame=None, target_calories=None, diet=None, exclude=None) -> web.Response:
    """Generate Meal Plan

    Generate a meal plan with three meals per day (breakfast, lunch, and dinner).

    :param time_frame: Either for one \&quot;day\&quot; or an entire \&quot;week\&quot;.
    :type time_frame: str
    :param target_calories: What is the caloric target for one day? The meal plan generator will try to get as close as possible to that goal.
    :type target_calories: 
    :param diet: Enter a diet that the meal plan has to adhere to. See a full list of supported diets.
    :type diet: str
    :param exclude: A comma-separated list of allergens or ingredients that must be excluded.
    :type exclude: str

    """
    return web.Response(status=200)


async def generate_shopping_list(request: web.Request, username, start_date, end_date, hash, body) -> web.Response:
    """Generate Shopping List

    Generate the shopping list for a user from the meal planner in a given time frame.

    :param username: The username.
    :type username: str
    :param start_date: The start date in the format yyyy-mm-dd.
    :type start_date: str
    :param end_date: The end date in the format yyyy-mm-dd.
    :type end_date: str
    :param hash: The private hash for the username.
    :type hash: str
    :param body: 
    :type body: dict | bytes

    """
    body = GenerateShoppingListRequest.from_dict(body)
    return web.Response(status=200)


async def get_meal_plan_template(request: web.Request, username, id, hash) -> web.Response:
    """Get Meal Plan Template

    Get information about a meal plan template.

    :param username: The username.
    :type username: str
    :param id: The item&#39;s id.
    :type id: int
    :param hash: The private hash for the username.
    :type hash: str

    """
    return web.Response(status=200)


async def get_meal_plan_templates(request: web.Request, username, hash) -> web.Response:
    """Get Meal Plan Templates

    Get meal plan templates from user or public ones.

    :param username: The username.
    :type username: str
    :param hash: The private hash for the username.
    :type hash: str

    """
    return web.Response(status=200)


async def get_meal_plan_week(request: web.Request, username, start_date, hash) -> web.Response:
    """Get Meal Plan Week

    Retrieve a meal planned week for the given user. The username must be a spoonacular user and the hash must the the user&#39;s hash that can be found in his/her account.

    :param username: The username.
    :type username: str
    :param start_date: The start date of the meal planned week in the format yyyy-mm-dd.
    :type start_date: str
    :param hash: The private hash for the username.
    :type hash: str

    """
    return web.Response(status=200)


async def get_shopping_list(request: web.Request, username, hash) -> web.Response:
    """Get Shopping List

    Get the current shopping list for the given user.

    :param username: The username.
    :type username: str
    :param hash: The private hash for the username.
    :type hash: str

    """
    return web.Response(status=200)
