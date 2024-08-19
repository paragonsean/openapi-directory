from typing import List, Dict
from aiohttp import web

from openapi_server.models.billbee_interfaces_billbee_api_model_create_shipment_api_model import BillbeeInterfacesBillbeeAPIModelCreateShipmentApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_paged_result_system_collections_generic_list_billbee_interfaces_billbee_api_model_shipment import RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelShipment
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_rechnungsdruck_web_app_controllers_api_shipment_with_label_result import RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiShipmentWithLabelResult
from openapi_server.models.rechnungsdruck_web_app_controllers_api_shipment_with_label import RechnungsdruckWebAppControllersApiShipmentWithLabel
from openapi_server import util


async def shipment_get_list(request: web.Request, page=None, page_size=None, created_at_min=None, created_at_max=None, order_id=None, minimum_shipment_id=None, shipping_provider_id=None) -> web.Response:
    """Get a list of all shipments optionally filtered by date. All parameters are optional.

    

    :param page: Specifies the page to request.
    :type page: int
    :param page_size: Specifies the pagesize. Defaults to 50, max value is 250
    :type page_size: int
    :param created_at_min: Specifies the oldest shipment date to include in the response
    :type created_at_min: str
    :param created_at_max: Specifies the newest shipment date to include in the response
    :type created_at_max: str
    :param order_id: Get shipments for this order only.
    :type order_id: int
    :param minimum_shipment_id: Get Shipments with a shipment greater or equal than this id. New shipments have a greater id than older shipments.
    :type minimum_shipment_id: int
    :param shipping_provider_id: Get Shippings for the specified shipping provider only. &lt;seealso cref&#x3D;\&quot;M:Rechnungsdruck.WebApp.Controllers.Api.ShipmentController.GetShippingproviders\&quot; /&gt;
    :type shipping_provider_id: int

    """
    created_at_min = util.deserialize_datetime(created_at_min)
    created_at_max = util.deserialize_datetime(created_at_max)
    return web.Response(status=200)


async def shipment_get_ping(request: web.Request, ) -> web.Response:
    """shipment_get_ping

    


    """
    return web.Response(status=200)


async def shipment_get_shipping_carrier(request: web.Request, ) -> web.Response:
    """Queries the currently available shipping carriers.

    


    """
    return web.Response(status=200)


async def shipment_get_shippingproviders(request: web.Request, ) -> web.Response:
    """Query all defined shipping providers

    


    """
    return web.Response(status=200)


async def shipment_post_shipment(request: web.Request, body) -> web.Response:
    """Creates a new shipment with the selected Shippingprovider

    

    :param body: Data to specify shipment parameters
    :type body: dict | bytes

    """
    body = BillbeeInterfacesBillbeeAPIModelCreateShipmentApiModel.from_dict(body)
    return web.Response(status=200)


async def shipment_ship_with_label(request: web.Request, body) -> web.Response:
    """Creates a shipment for an order in billbee

    

    :param body: Details on the order and the shipping methods, that should be used.
    :type body: dict | bytes

    """
    body = RechnungsdruckWebAppControllersApiShipmentWithLabel.from_dict(body)
    return web.Response(status=200)
