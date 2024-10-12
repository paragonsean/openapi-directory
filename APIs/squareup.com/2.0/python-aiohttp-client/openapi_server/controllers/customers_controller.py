from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_group_to_customer_response import AddGroupToCustomerResponse
from openapi_server.models.create_customer_card_request import CreateCustomerCardRequest
from openapi_server.models.create_customer_card_response import CreateCustomerCardResponse
from openapi_server.models.create_customer_request import CreateCustomerRequest
from openapi_server.models.create_customer_response import CreateCustomerResponse
from openapi_server.models.delete_customer_card_response import DeleteCustomerCardResponse
from openapi_server.models.delete_customer_response import DeleteCustomerResponse
from openapi_server.models.list_customers_response import ListCustomersResponse
from openapi_server.models.remove_group_from_customer_response import RemoveGroupFromCustomerResponse
from openapi_server.models.retrieve_customer_response import RetrieveCustomerResponse
from openapi_server.models.search_customers_request import SearchCustomersRequest
from openapi_server.models.search_customers_response import SearchCustomersResponse
from openapi_server.models.update_customer_request import UpdateCustomerRequest
from openapi_server.models.update_customer_response import UpdateCustomerResponse
from openapi_server import util


async def add_group_to_customer(request: web.Request, customer_id, group_id) -> web.Response:
    """AddGroupToCustomer

    Adds a group membership to a customer.  The customer is identified by the &#x60;customer_id&#x60; value and the customer group is identified by the &#x60;group_id&#x60; value.

    :param customer_id: The ID of the customer to add to a group.
    :type customer_id: str
    :param group_id: The ID of the customer group to add the customer to.
    :type group_id: str

    """
    return web.Response(status=200)


async def create_customer(request: web.Request, body) -> web.Response:
    """CreateCustomer

    Creates a new customer for a business.  You must provide at least one of the following values in your request to this endpoint:  - &#x60;given_name&#x60; - &#x60;family_name&#x60; - &#x60;company_name&#x60; - &#x60;email_address&#x60; - &#x60;phone_number&#x60;

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CreateCustomerRequest.from_dict(body)
    return web.Response(status=200)


async def create_customer_card(request: web.Request, customer_id, body) -> web.Response:
    """CreateCustomerCard

    Adds a card on file to an existing customer.  As with charges, calls to &#x60;CreateCustomerCard&#x60; are idempotent. Multiple calls with the same card nonce return the same card record that was created with the provided nonce during the _first_ call.

    :param customer_id: The Square ID of the customer profile the card is linked to.
    :type customer_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = CreateCustomerCardRequest.from_dict(body)
    return web.Response(status=200)


async def delete_customer(request: web.Request, customer_id, version=None) -> web.Response:
    """DeleteCustomer

    Deletes a customer profile from a business. This operation also unlinks any associated cards on file.   As a best practice, you should include the &#x60;version&#x60; field in the request to enable [optimistic concurrency](https://developer.squareup.com/docs/working-with-apis/optimistic-concurrency) control. The value must be set to the current version of the customer profile.   To delete a customer profile that was created by merging existing profiles, you must use the ID of the newly created profile.

    :param customer_id: The ID of the customer to delete.
    :type customer_id: str
    :param version: The current version of the customer profile.  As a best practice, you should include this parameter to enable [optimistic concurrency](https://developer.squareup.com/docs/working-with-apis/optimistic-concurrency) control.  For more information, see [Delete a customer profile](https://developer.squareup.com/docs/customers-api/use-the-api/keep-records#delete-customer-profile).
    :type version: int

    """
    return web.Response(status=200)


async def delete_customer_card(request: web.Request, customer_id, card_id) -> web.Response:
    """DeleteCustomerCard

    Removes a card on file from a customer.

    :param customer_id: The ID of the customer that the card on file belongs to.
    :type customer_id: str
    :param card_id: The ID of the card on file to delete.
    :type card_id: str

    """
    return web.Response(status=200)


async def list_customers(request: web.Request, cursor=None, limit=None, sort_field=None, sort_order=None) -> web.Response:
    """ListCustomers

    Lists customer profiles associated with a Square account.  Under normal operating conditions, newly created or updated customer profiles become available for the listing operation in well under 30 seconds. Occasionally, propagation of the new or updated profiles can take closer to one minute or longer, especially during network incidents and outages.

    :param cursor: A pagination cursor returned by a previous call to this endpoint. Provide this cursor to retrieve the next set of results for your original query.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    :type cursor: str
    :param limit: The maximum number of results to return in a single page. This limit is advisory. The response might contain more or fewer results.  The limit is ignored if it is less than 1 or greater than 100. The default value is 100.  For more information, see [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination).
    :type limit: int
    :param sort_field: Indicates how customers should be sorted.  The default value is &#x60;DEFAULT&#x60;.
    :type sort_field: str
    :param sort_order: Indicates whether customers should be sorted in ascending (&#x60;ASC&#x60;) or descending (&#x60;DESC&#x60;) order.  The default value is &#x60;ASC&#x60;.
    :type sort_order: str

    """
    return web.Response(status=200)


async def remove_group_from_customer(request: web.Request, customer_id, group_id) -> web.Response:
    """RemoveGroupFromCustomer

    Removes a group membership from a customer.  The customer is identified by the &#x60;customer_id&#x60; value and the customer group is identified by the &#x60;group_id&#x60; value.

    :param customer_id: The ID of the customer to remove from the group.
    :type customer_id: str
    :param group_id: The ID of the customer group to remove the customer from.
    :type group_id: str

    """
    return web.Response(status=200)


async def retrieve_customer(request: web.Request, customer_id) -> web.Response:
    """RetrieveCustomer

    Returns details for a single customer.

    :param customer_id: The ID of the customer to retrieve.
    :type customer_id: str

    """
    return web.Response(status=200)


async def search_customers(request: web.Request, body) -> web.Response:
    """SearchCustomers

    Searches the customer profiles associated with a Square account using a supported query filter.  Calling &#x60;SearchCustomers&#x60; without any explicit query filter returns all customer profiles ordered alphabetically based on &#x60;given_name&#x60; and &#x60;family_name&#x60;.  Under normal operating conditions, newly created or updated customer profiles become available for the search operation in well under 30 seconds. Occasionally, propagation of the new or updated profiles can take closer to one minute or longer, especially during network incidents and outages.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = SearchCustomersRequest.from_dict(body)
    return web.Response(status=200)


async def update_customer(request: web.Request, customer_id, body) -> web.Response:
    """UpdateCustomer

    Updates a customer profile. To change an attribute, specify the new value. To remove an attribute, specify the value as an empty string or empty object.  As a best practice, you should include the &#x60;version&#x60; field in the request to enable [optimistic concurrency](https://developer.squareup.com/docs/working-with-apis/optimistic-concurrency) control. The value must be set to the current version of the customer profile.  To update a customer profile that was created by merging existing profiles, you must use the ID of the newly created profile.  You cannot use this endpoint to change cards on file. To make changes, use the [Cards API](https://developer.squareup.com/reference/square_2021-08-18/cards-api) or [Gift Cards API](https://developer.squareup.com/reference/square_2021-08-18/gift-cards-api).

    :param customer_id: The ID of the customer to update.
    :type customer_id: str
    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = UpdateCustomerRequest.from_dict(body)
    return web.Response(status=200)
