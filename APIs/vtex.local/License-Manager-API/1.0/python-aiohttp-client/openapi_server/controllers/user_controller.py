from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_user200_response import CreateUser200Response
from openapi_server.models.create_user400_response import CreateUser400Response
from openapi_server.models.create_user_request import CreateUserRequest
from openapi_server.models.get_user400_response import GetUser400Response
from openapi_server.models.list_users_response import ListUsersResponse
from openapi_server import util


async def create_user(request: web.Request, body) -> web.Response:
    """Create User

    Allows you to create a user by providing an email (mandatory) and name (optional). The email must be in a valid format. The success response will contain the generated &#x60;userId&#x60; for that user.

    :param body: 
    :type body: dict | bytes

    """
    body = CreateUserRequest.from_dict(body)
    return web.Response(status=200)


async def get_list_users(request: web.Request, content_type, num_items=None, page_number=None, sort=None, sort_type=None) -> web.Response:
    """Get List of Users

    Returns a list of registered users. The response is divided in pages. The query parameter &#x60;numItems&#x60; defines the number of items in each page, and consequently the amount of pages for the whole list.

    :param content_type: The media type of the body of the request. Default value for license manager protocol is application/json
    :type content_type: str
    :param num_items: Number of items in the returned page
    :type num_items: int
    :param page_number: Which page from the whole list will be returned
    :type page_number: int
    :param sort: Chooses the field that the list will be sorted by
    :type sort: str
    :param sort_type: Defines the sorting order. &#x60;ASC&#x60; is used for ascendant order. &#x60;DSC&#x60; is used for descendant order
    :type sort_type: str

    """
    return web.Response(status=200)


async def get_user(request: web.Request, content_type, user_id) -> web.Response:
    """Get User

    Allows you to get a user from the database, using the &#x60;userId&#x60; as the identifier.

    :param content_type: The media type of the body of the request. Default value for license manager protocol is application/json
    :type content_type: str
    :param user_id: ID from queried user.
    :type user_id: str

    """
    return web.Response(status=200)
