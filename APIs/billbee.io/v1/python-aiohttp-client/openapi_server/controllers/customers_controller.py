from typing import List, Dict
from aiohttp import web

from openapi_server.models.billbee_interfaces_billbee_api_model_create_customer_api_model import BillbeeInterfacesBillbeeAPIModelCreateCustomerApiModel
from openapi_server.models.billbee_interfaces_billbee_api_model_customer_address_api_model import BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel
from openapi_server.models.billbee_interfaces_billbee_api_model_customer_api_model import BillbeeInterfacesBillbeeAPIModelCustomerApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_paged_result_system_collections_generic_list_billbee_interfaces_billbee_api_model_customer_address_api_model import RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_paged_result_system_collections_generic_list_billbee_interfaces_billbee_api_model_customer_api_model import RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_paged_result_system_collections_generic_list_rechnungsdruck_web_app_controllers_api_order import RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListRechnungsdruckWebAppControllersApiOrder
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_billbee_interfaces_billbee_api_model_customer_address_api_model import RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_billbee_interfaces_billbee_api_model_customer_api_model import RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_rechnungsdruck_web_app_controllers_api_search_controller_search_results_model import RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_search_controller_search_model import RechnungsdruckWebAppControllersApiSearchControllerSearchModel
from openapi_server import util


async def customer_add_customer_address(request: web.Request, id, body) -> web.Response:
    """Adds a new address to a customer

    Id and  CustomerId will be ignored in model. If Id is set, the addition will be stopped.

    :param id: CustomerId to attach the new address to.
    :type id: int
    :param body: Model containing the address, that should be attached.
    :type body: dict | bytes

    """
    body = BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.from_dict(body)
    return web.Response(status=200)


async def customer_create(request: web.Request, body) -> web.Response:
    """Creates a new customer

    

    :param body: 
    :type body: dict | bytes

    """
    body = BillbeeInterfacesBillbeeAPIModelCreateCustomerApiModel.from_dict(body)
    return web.Response(status=200)


async def customer_get_all(request: web.Request, page=None, page_size=None) -> web.Response:
    """Get a list of all customers

    

    :param page: The current page to request starting with 1
    :type page: int
    :param page_size: The pagesize for the result list. Values between 1 and 250 are allowed
    :type page_size: int

    """
    return web.Response(status=200)


async def customer_get_customer_address(request: web.Request, id) -> web.Response:
    """Queries a single address from a customer

    

    :param id: The id of the address
    :type id: int

    """
    return web.Response(status=200)


async def customer_get_customer_addresses(request: web.Request, id, page=None, page_size=None) -> web.Response:
    """Queries a list of addresses from a customer

    

    :param id: The id of the customer
    :type id: int
    :param page: The current page to request starting with 1
    :type page: int
    :param page_size: The pagesize for the result list. Values between 1 and 250 are allowed
    :type page_size: int

    """
    return web.Response(status=200)


async def customer_get_customer_orders(request: web.Request, id, page=None, page_size=None) -> web.Response:
    """Queries a list of orders from a customer

    

    :param id: The id of the customer
    :type id: int
    :param page: The current page to request starting with 1
    :type page: int
    :param page_size: The pagesize for the result list. Values between 1 and 250 are allowed
    :type page_size: int

    """
    return web.Response(status=200)


async def customer_get_one(request: web.Request, id) -> web.Response:
    """Queries a single customer by id

    

    :param id: The id of the customer to query
    :type id: int

    """
    return web.Response(status=200)


async def customer_patch_address(request: web.Request, id, body) -> web.Response:
    """Updates one or more fields of an address

    Id and CustomerId cannot be changed

    :param id: The id of the address
    :type id: int
    :param body: The address fields to be changed. Please query an address via (todo) to see all fields. Note that Id and CustomerId cannot be changed.
    :type body: 

    """
    return web.Response(status=200)


async def customer_update(request: web.Request, id, body) -> web.Response:
    """Updates a customer by id

    

    :param id: The id of the customer
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = BillbeeInterfacesBillbeeAPIModelCustomerApiModel.from_dict(body)
    return web.Response(status=200)


async def customer_update_address(request: web.Request, id, body) -> web.Response:
    """Updates all fields of an address

    Id and CustomerId cannot be changed. Fields you do not send will become empty.

    :param id: The id of the address
    :type id: int
    :param body: The updated address. Please query an address via (todo) to see all fields. Note that Id and CustomerId cannot be changed.
    :type body: dict | bytes

    """
    body = BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.from_dict(body)
    return web.Response(status=200)


async def search_search_0(request: web.Request, body) -> web.Response:
    """Search for products, customers and orders.  Type can be \&quot;order\&quot;, \&quot;product\&quot; and / or \&quot;customer\&quot;  Term can contains lucene query syntax

    

    :param body: 
    :type body: dict | bytes

    """
    body = RechnungsdruckWebAppControllersApiSearchControllerSearchModel.from_dict(body)
    return web.Response(status=200)
