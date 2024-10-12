from typing import List, Dict
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
from openapi_server import util


async def grocery_list_add_recipe(request: web.Request, body) -> web.Response:
    """Add a Recipe to the grocery list.  In the request data, pass in recipeId, scale (scale&#x3D;1.0 says to keep the recipe the same size as originally posted), markAsPending (true/false) to indicate that              the lines in the recipe should be marked in a \&quot;pending\&quot; (unconfirmed by user) state.

    

    :param body: 
    :type body: dict | bytes

    """
    body = API2ControllersWebAPIGroceryListControllerPostGroceryListRecipeRequest.from_dict(body)
    return web.Response(status=200)


async def grocery_list_delete(request: web.Request, ) -> web.Response:
    """Delete all the items on a grocery list; faster operation than a sync with deleted items.

    


    """
    return web.Response(status=200)


async def grocery_list_delete_item_by_guid(request: web.Request, guid) -> web.Response:
    """/grocerylist/item/{guid}  DELETE will delete this item assuming you own it.

    

    :param guid: 
    :type guid: str

    """
    return web.Response(status=200)


async def grocery_list_department(request: web.Request, body) -> web.Response:
    """Departmentalize a list of strings -- used for ad-hoc grocery list item addition

    

    :param body: see DepartmentModel for the request payload
    :type body: dict | bytes

    """
    body = API2ControllersWebAPIGroceryListControllerDepartmentModel.from_dict(body)
    return web.Response(status=200)


async def grocery_list_get(request: web.Request, ) -> web.Response:
    """Get the user&#39;s grocery list.  User is determined by Basic Authentication.

    


    """
    return web.Response(status=200)


async def grocery_list_grocery_list_item_guid(request: web.Request, guid, body) -> web.Response:
    """Update a grocery item by GUID

    

    :param guid: 
    :type guid: str
    :param body: 
    :type body: dict | bytes

    """
    body = API2ControllersWebAPIGroceryListControllerUpdateItemByGuidRequest.from_dict(body)
    return web.Response(status=200)


async def grocery_list_grocery_list_remove_marked_items(request: web.Request, ) -> web.Response:
    """Clears the checked lines.

    


    """
    return web.Response(status=200)


async def grocery_list_post(request: web.Request, body) -> web.Response:
    """Add a single line item to the grocery list

    

    :param body: name, quantity, unit, notes, department
    :type body: dict | bytes

    """
    body = API2ControllersWebAPIGroceryListControllerPostGroceryListAddLineRequest.from_dict(body)
    return web.Response(status=200)


async def grocery_list_post_grocery_list_sync(request: web.Request, body) -> web.Response:
    """Synchronize the grocery list.  Call this with a POST to /grocerylist/sync

    

    :param body: 
    :type body: dict | bytes

    """
    body = API2ControllersWebAPIGroceryListControllerPostGroceryListSyncRequest.from_dict(body)
    return web.Response(status=200)


async def grocerylist_item_post(request: web.Request, body) -> web.Response:
    """Add a single line item to the grocery list

    

    :param body: name, quantity, unit, notes, department
    :type body: dict | bytes

    """
    body = API2ControllersWebAPIGroceryListControllerPostToGroceryListRecipeRequest.from_dict(body)
    return web.Response(status=200)
