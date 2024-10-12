from typing import List, Dict
from aiohttp import web

from openapi_server.models.billbee_interfaces_billbee_api_model_customer_address_api_model import BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_paged_result_system_collections_generic_list_billbee_interfaces_billbee_api_model_customer_address_api_model import RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_billbee_interfaces_billbee_api_model_customer_address_api_model import RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel
from openapi_server import util


async def customer_addresses_create(request: web.Request, body) -> web.Response:
    """Creates a new customer address

    

    :param body: 
    :type body: dict | bytes

    """
    body = BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.from_dict(body)
    return web.Response(status=200)


async def customer_addresses_get_all(request: web.Request, page=None, page_size=None) -> web.Response:
    """Get a list of all customer addresses

    

    :param page: The current page to request starting with 1 (default is 1)
    :type page: int
    :param page_size: The page size for the result list. Values between 1 and 250 are allowed. (default is 50)
    :type page_size: int

    """
    return web.Response(status=200)


async def customer_addresses_get_one(request: web.Request, id) -> web.Response:
    """Queries a single customer address by id

    

    :param id: The id of the address to query
    :type id: int

    """
    return web.Response(status=200)


async def customer_addresses_update(request: web.Request, id, body) -> web.Response:
    """Updates a customer address by id

    

    :param id: The id of the address
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = BillbeeInterfacesBillbeeAPIModelCustomerAddressApiModel.from_dict(body)
    return web.Response(status=200)
