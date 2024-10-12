from typing import List, Dict
from aiohttp import web

from openapi_server.models.category import Category
from openapi_server.models.error import Error
from openapi_server import util


async def check_if_user_subscribed_to_category(request: web.Request, category, user_id) -> web.Response:
    """Check if a user follows a category

    

    :param category: The name of the category.
    :type category: str
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def check_if_user_subscribed_to_category_alt1(request: web.Request, category) -> web.Response:
    """Check if a user follows a category

    

    :param category: The name of the category.
    :type category: str

    """
    return web.Response(status=200)


async def get_category_subscriptions(request: web.Request, user_id, direction=None, page=None, per_page=None, sort=None) -> web.Response:
    """Get all the categories that a user follows

    

    :param user_id: The ID of the user.
    :type user_id: 
    :param direction: The sort direction of the results.
    :type direction: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)


async def get_category_subscriptions_alt1(request: web.Request, direction=None, page=None, per_page=None, sort=None) -> web.Response:
    """Get all the categories that a user follows

    

    :param direction: The sort direction of the results.
    :type direction: str
    :param page: The page number of the results to show.
    :type page: 
    :param per_page: The number of items to show on each page of results, up to a maximum of 100.
    :type per_page: 
    :param sort: The way to sort the results.
    :type sort: str

    """
    return web.Response(status=200)


async def subscribe_to_category(request: web.Request, category, user_id) -> web.Response:
    """Subscribe a user to a single category

    

    :param category: The name of the category.
    :type category: 
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def subscribe_to_category_alt1(request: web.Request, category) -> web.Response:
    """Subscribe a user to a single category

    

    :param category: The name of the category.
    :type category: 

    """
    return web.Response(status=200)


async def unsubscribe_from_category(request: web.Request, category, user_id) -> web.Response:
    """Unsubscribe a user from a category

    

    :param category: The name of the category.
    :type category: str
    :param user_id: The ID of the user.
    :type user_id: 

    """
    return web.Response(status=200)


async def unsubscribe_from_category_alt1(request: web.Request, category) -> web.Response:
    """Unsubscribe a user from a category

    

    :param category: The name of the category.
    :type category: str

    """
    return web.Response(status=200)
