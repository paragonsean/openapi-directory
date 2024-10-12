from typing import List, Dict
from aiohttp import web

from openapi_server.models.create_customer_group_request import CreateCustomerGroupRequest
from openapi_server.models.create_customer_group_response import CreateCustomerGroupResponse
from openapi_server.models.delete_customer_group_response import DeleteCustomerGroupResponse
from openapi_server.models.list_customer_groups_response import ListCustomerGroupsResponse
from openapi_server.models.retrieve_customer_group_response import RetrieveCustomerGroupResponse
from openapi_server.models.update_customer_group_request import UpdateCustomerGroupRequest
from openapi_server.models.update_customer_group_response import UpdateCustomerGroupResponse
from openapi_server import util


async def create_customer_group(request: web.Request, body) -> web.Response:
    """CreateCustomerGroup

    Creates a new customer group for a business.  The request must include the &#x60;name&#x60; value of the group.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CreateCustomerGroupRequest.from_dict(body)
    return web.Response(status=200)


async def delete_customer_group(request: web.Request, group_id) -> web.Response:
    """DeleteCustomerGroup

    Deletes a customer group as identified by the &#x60;group_id&#x60; value.

    :param group_id: The ID of the customer group to delete.
    :type group_id: str

    """
    return web.Response(status=200)


async def list_customer_groups(request: web.Request, cursor=None, limit=None) -> web.Response:
    """ListCustomerGroups

    Retrieves the list of customer groups of a business.

    :param cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for your original query.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    :type cursor: str
    :param limit: The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.  The limit is ignored if it is less than 1 or greater than 50. The default value is 50.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    :type limit: int

    """
    return web.Response(status=200)


async def retrieve_customer_group(request: web.Request, group_id) -> web.Response:
    """RetrieveCustomerGroup

    Retrieves a specific customer group as identified by the &#x60;group_id&#x60; value.

    :param group_id: The ID of the customer group to retrieve.
    :type group_id: str

    """
    return web.Response(status=200)


async def update_customer_group(request: web.Request, group_id, body) -> web.Response:
    """UpdateCustomerGroup

    Updates a customer group as identified by the &#x60;group_id&#x60; value.

    :param group_id: The ID of the customer group to update.
    :type group_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = UpdateCustomerGroupRequest.from_dict(body)
    return web.Response(status=200)
