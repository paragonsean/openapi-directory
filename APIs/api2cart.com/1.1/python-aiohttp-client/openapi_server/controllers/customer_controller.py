from typing import List, Dict
from aiohttp import web

from openapi_server.models.customer_add import CustomerAdd
from openapi_server.models.customer_add200_response import CustomerAdd200Response
from openapi_server.models.customer_count200_response import CustomerCount200Response
from openapi_server.models.customer_find200_response import CustomerFind200Response
from openapi_server.models.customer_group_add200_response import CustomerGroupAdd200Response
from openapi_server.models.customer_info200_response import CustomerInfo200Response
from openapi_server.models.customer_update import CustomerUpdate
from openapi_server.models.customer_update200_response import CustomerUpdate200Response
from openapi_server.models.customer_wishlist_list200_response import CustomerWishlistList200Response
from openapi_server.models.model_response_customer_attribute_list import ModelResponseCustomerAttributeList
from openapi_server.models.model_response_customer_group_list import ModelResponseCustomerGroupList
from openapi_server.models.model_response_customer_list import ModelResponseCustomerList
from openapi_server import util


async def customer_add(request: web.Request, body) -> web.Response:
    """customer_add

    Add customer into store.

    :param body: 
    :type body: dict | bytes

    """
    body = CustomerAdd.from_dict(body)
    return web.Response(status=200)


async def customer_attribute_list(request: web.Request, customer_id, count=None, page_cursor=None, store_id=None, lang_id=None, params=None, exclude=None, response_fields=None) -> web.Response:
    """customer_attribute_list

    Get attributes for specific customer

    :param customer_id: Retrieves orders specified by customer id
    :type customer_id: str
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param page_cursor: Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter)
    :type page_cursor: str
    :param store_id: Store Id
    :type store_id: str
    :param lang_id: Language id
    :type lang_id: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str

    """
    return web.Response(status=200)


async def customer_count(request: web.Request, group_id=None, created_from=None, created_to=None, modified_from=None, modified_to=None, store_id=None, customer_list_id=None, avail=None) -> web.Response:
    """customer_count

    Get number of customers from store.

    :param group_id: Customer group_id
    :type group_id: str
    :param created_from: Retrieve entities from their creation date
    :type created_from: str
    :param created_to: Retrieve entities to their creation date
    :type created_to: str
    :param modified_from: Retrieve entities from their modification date
    :type modified_from: str
    :param modified_to: Retrieve entities to their modification date
    :type modified_to: str
    :param store_id: Counts customer specified by store id
    :type store_id: str
    :param customer_list_id: The numeric ID of the customer list in Demandware.
    :type customer_list_id: str
    :param avail: Defines category&#39;s visibility status
    :type avail: bool

    """
    return web.Response(status=200)


async def customer_find(request: web.Request, find_value, find_where=None, find_params=None, store_id=None) -> web.Response:
    """customer_find

    Find customers in store.

    :param find_value: Entity search that is specified by some value
    :type find_value: str
    :param find_where: Entity search that is specified by the comma-separated unique fields
    :type find_where: str
    :param find_params: Entity search that is specified by comma-separated parameters
    :type find_params: str
    :param store_id: Store Id
    :type store_id: str

    """
    return web.Response(status=200)


async def customer_group_add(request: web.Request, name, store_id=None, stores_ids=None) -> web.Response:
    """customer_group_add

    Create customer group.

    :param name: Customer group name
    :type name: str
    :param store_id: Store Id
    :type store_id: str
    :param stores_ids: Assign customer group to the stores that is specified by comma-separated stores&#39; id
    :type stores_ids: str

    """
    return web.Response(status=200)


async def customer_group_list(request: web.Request, page_cursor=None, start=None, count=None, store_id=None, lang_id=None, group_ids=None, params=None, exclude=None, response_fields=None) -> web.Response:
    """customer_group_list

    Get list of customers groups.

    :param page_cursor: Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter)
    :type page_cursor: str
    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param store_id: Store Id
    :type store_id: str
    :param lang_id: Language id
    :type lang_id: str
    :param group_ids: Groups that will be assigned to a customer
    :type group_ids: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str

    """
    return web.Response(status=200)


async def customer_info(request: web.Request, id, params=None, response_fields=None, exclude=None, store_id=None) -> web.Response:
    """customer_info

    Get customers&#39; details from store.

    :param id: Retrieves customer&#39;s info specified by customer id
    :type id: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param store_id: Retrieves customer info specified by store id
    :type store_id: str

    """
    return web.Response(status=200)


async def customer_list(request: web.Request, page_cursor=None, start=None, count=None, created_from=None, created_to=None, modified_from=None, modified_to=None, params=None, response_fields=None, exclude=None, group_id=None, store_id=None, customer_list_id=None, avail=None) -> web.Response:
    """customer_list

    Get list of customers from store.

    :param page_cursor: Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter)
    :type page_cursor: str
    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param created_from: Retrieve entities from their creation date
    :type created_from: str
    :param created_to: Retrieve entities to their creation date
    :type created_to: str
    :param modified_from: Retrieve entities from their modification date
    :type modified_from: str
    :param modified_to: Retrieve entities to their modification date
    :type modified_to: str
    :param params: Set this parameter in order to choose which entity fields you want to retrieve
    :type params: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str
    :param exclude: Set this parameter in order to choose which entity fields you want to ignore. Works only if parameter &#x60;params&#x60; equal force_all
    :type exclude: str
    :param group_id: Customer group_id
    :type group_id: str
    :param store_id: Retrieves customers specified by store id
    :type store_id: str
    :param customer_list_id: The numeric ID of the customer list in Demandware.
    :type customer_list_id: str
    :param avail: Defines category&#39;s visibility status
    :type avail: bool

    """
    return web.Response(status=200)


async def customer_update(request: web.Request, body) -> web.Response:
    """customer_update

    Update information of customer in store.

    :param body: 
    :type body: dict | bytes

    """
    body = CustomerUpdate.from_dict(body)
    return web.Response(status=200)


async def customer_wishlist_list(request: web.Request, customer_id, id=None, store_id=None, start=None, count=None, page_cursor=None, response_fields=None) -> web.Response:
    """customer_wishlist_list

    Get a Wish List of customer from the store.

    :param customer_id: Retrieves orders specified by customer id
    :type customer_id: str
    :param id: Entity id
    :type id: str
    :param store_id: Store Id
    :type store_id: str
    :param start: This parameter sets the number from which you want to get entities
    :type start: int
    :param count: This parameter sets the entity amount that has to be retrieved. Max allowed count&#x3D;250
    :type count: int
    :param page_cursor: Used to retrieve entities via cursor-based pagination (it can&#39;t be used with any other filtering parameter)
    :type page_cursor: str
    :param response_fields: Set this parameter in order to choose which entity fields you want to retrieve
    :type response_fields: str

    """
    return web.Response(status=200)
