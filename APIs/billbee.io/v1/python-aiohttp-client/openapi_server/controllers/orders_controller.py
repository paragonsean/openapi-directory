from typing import List, Dict
from aiohttp import web

from openapi_server.models.billbee_interfaces_billbee_api_model_order import BillbeeInterfacesBillbeeAPIModelOrder
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_add_shipment_to_order_model import RechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_paged_result_system_collections_generic_list_billbee_interfaces_billbee_api_model_invoice_api_model import RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelInvoiceApiModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_paged_result_system_collections_generic_list_billbee_interfaces_billbee_api_model_order import RechnungsdruckWebAppControllersApiApiPagedResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelOrder
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_billbee_interfaces_billbee_api_model_order import RechnungsdruckWebAppControllersApiApiResultBillbeeInterfacesBillbeeAPIModelOrder
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_rechnungsdruck_web_app_controllers_api_invoice import RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiInvoice
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_rechnungsdruck_web_app_controllers_api_search_controller_search_results_model import RechnungsdruckWebAppControllersApiApiResultRechnungsdruckWebAppControllersApiSearchControllerSearchResultsModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_api_result_system_collections_generic_list_billbee_interfaces_billbee_api_models_layout_template import RechnungsdruckWebAppControllersApiApiResultSystemCollectionsGenericListBillbeeInterfacesBillbeeAPIModelsLayoutTemplate
from openapi_server.models.rechnungsdruck_web_app_controllers_api_order_api_controller_parse_text_container import RechnungsdruckWebAppControllersApiOrderApiControllerParseTextContainer
from openapi_server.models.rechnungsdruck_web_app_controllers_api_order_api_controller_send_message_model import RechnungsdruckWebAppControllersApiOrderApiControllerSendMessageModel
from openapi_server.models.rechnungsdruck_web_app_controllers_api_order_api_controller_trigger_event_container import RechnungsdruckWebAppControllersApiOrderApiControllerTriggerEventContainer
from openapi_server.models.rechnungsdruck_web_app_controllers_api_order_state_update import RechnungsdruckWebAppControllersApiOrderStateUpdate
from openapi_server.models.rechnungsdruck_web_app_controllers_api_order_tag_create import RechnungsdruckWebAppControllersApiOrderTagCreate
from openapi_server.models.rechnungsdruck_web_app_controllers_api_search_controller_search_model import RechnungsdruckWebAppControllersApiSearchControllerSearchModel
from openapi_server import util


async def layout_api_get_list(request: web.Request, ) -> web.Response:
    """layout_api_get_list

    


    """
    return web.Response(status=200)


async def order_api_add_shipment(request: web.Request, id, body) -> web.Response:
    """Add a shipment to a given order

    

    :param id: The internal billbee id of the order
    :type id: int
    :param body: The shipment data to create the shipment
    :type body: dict | bytes

    """
    body = RechnungsdruckWebAppControllersApiApiAddShipmentToOrderModel.from_dict(body)
    return web.Response(status=200)


async def order_api_create_delivery_note(request: web.Request, id, include_pdf=None, send_to_cloud_id=None) -> web.Response:
    """Create an delivery note for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes.

    

    :param id: The internal billbee id of the order
    :type id: int
    :param include_pdf: If true, the PDF is included in the response as base64 encoded string
    :type include_pdf: bool
    :param send_to_cloud_id: Optionally specify the id of a billbee connected cloud device to send the pdf to
    :type send_to_cloud_id: int

    """
    return web.Response(status=200)


async def order_api_create_invoice(request: web.Request, id, include_invoice_pdf=None, template_id=None, send_to_cloud_id=None) -> web.Response:
    """Create an invoice for an existing order. This request is extra throttled by order and api key to a maximum of 1 per 5 minutes.

    

    :param id: The internal billbee id of the order
    :type id: int
    :param include_invoice_pdf: If true, the PDF is included in the response as base64 encoded string
    :type include_invoice_pdf: bool
    :param template_id: You can pass the id of an invoice template to overwrite the assigned template for invoice creation
    :type template_id: int
    :param send_to_cloud_id: You can pass the id of a connected cloud printer/storage to send the invoice to it
    :type send_to_cloud_id: int

    """
    return web.Response(status=200)


async def order_api_find(request: web.Request, id, partner) -> web.Response:
    """Find a single order by its external id (order number)

    

    :param id: The order id from the external system
    :type id: str
    :param partner: Optional the name of the shop/marketplace the order was imported from
    :type partner: str

    """
    return web.Response(status=200)


async def order_api_get(request: web.Request, id, article_title_source=None) -> web.Response:
    """Get a single order by its internal billbee id. This request is throttled to 6 calls per order in one minute

    

    :param id: The internal billbee id of the order
    :type id: int
    :param article_title_source: The source field for the article title. 0 &#x3D; Order Position (default), 1 &#x3D; Article Title, 2 &#x3D; Article Invoice Text
    :type article_title_source: int

    """
    return web.Response(status=200)


async def order_api_get_by_ext_ref(request: web.Request, ext_ref) -> web.Response:
    """Get a single order by its external order number

    

    :param ext_ref: The extern order number of the order
    :type ext_ref: str

    """
    return web.Response(status=200)


async def order_api_get_invoice_list(request: web.Request, min_invoice_date=None, max_invoice_date=None, page=None, page_size=None, shop_id=None, order_state_id=None, tag=None, min_pay_date=None, max_pay_date=None, include_positions=None, exclude_tags=None) -> web.Response:
    """Get a list of all invoices optionally filtered by date. This request ist throttled to 1 per 1 minute for same page and minInvoiceDate

    

    :param min_invoice_date: Specifies the oldest invoice date to include
    :type min_invoice_date: str
    :param max_invoice_date: Specifies the newest invoice date to include
    :type max_invoice_date: str
    :param page: Specifies the page to request
    :type page: int
    :param page_size: Specifies the pagesize. Defaults to 50, max value is 250
    :type page_size: int
    :param shop_id: Specifies a list of shop ids for which invoices should be included
    :type shop_id: List[int]
    :param order_state_id: Specifies a list of state ids to include in the response
    :type order_state_id: List[int]
    :param tag: 
    :type tag: List[str]
    :param min_pay_date: 
    :type min_pay_date: str
    :param max_pay_date: 
    :type max_pay_date: str
    :param include_positions: 
    :type include_positions: bool
    :param exclude_tags: If true the list of tags passed to the call are used to filter orders to not include these tags
    :type exclude_tags: bool

    """
    min_invoice_date = util.deserialize_datetime(min_invoice_date)
    max_invoice_date = util.deserialize_datetime(max_invoice_date)
    min_pay_date = util.deserialize_datetime(min_pay_date)
    max_pay_date = util.deserialize_datetime(max_pay_date)
    return web.Response(status=200)


async def order_api_get_list(request: web.Request, min_order_date=None, max_order_date=None, page=None, page_size=None, shop_id=None, order_state_id=None, tag=None, minimum_bill_bee_order_id=None, modified_at_min=None, modified_at_max=None, article_title_source=None, exclude_tags=None) -> web.Response:
    """Get a list of all orders optionally filtered by date

    

    :param min_order_date: Specifies the oldest order date to include in the response
    :type min_order_date: str
    :param max_order_date: Specifies the newest order date to include in the response
    :type max_order_date: str
    :param page: Specifies the page to request
    :type page: int
    :param page_size: Specifies the pagesize. Defaults to 50, max value is 250
    :type page_size: int
    :param shop_id: Specifies a list of shop ids for which invoices should be included
    :type shop_id: List[int]
    :param order_state_id: Specifies a list of state ids to include in the response
    :type order_state_id: List[int]
    :param tag: Specifies a list of tags the order must have attached to be included in the response
    :type tag: List[str]
    :param minimum_bill_bee_order_id: If given, all delivered orders have an Id greater than or equal to the given minimumOrderId
    :type minimum_bill_bee_order_id: int
    :param modified_at_min: If given, the last modification has to be newer than the given date
    :type modified_at_min: str
    :param modified_at_max: If given, the last modification has to be older or equal than the given date.
    :type modified_at_max: str
    :param article_title_source: The source field for the article title. 0 &#x3D; Order Position (default), 1 &#x3D; Article Title, 2 &#x3D; Article Invoice Text
    :type article_title_source: int
    :param exclude_tags: If true the list of tags passed to the call are used to filter orders to not include these tags
    :type exclude_tags: bool

    """
    min_order_date = util.deserialize_datetime(min_order_date)
    max_order_date = util.deserialize_datetime(max_order_date)
    modified_at_min = util.deserialize_datetime(modified_at_min)
    modified_at_max = util.deserialize_datetime(modified_at_max)
    return web.Response(status=200)


async def order_api_get_patchable_fields(request: web.Request, ) -> web.Response:
    """Returns a list of fields which can be updated with the orders/{id} patch call

    


    """
    return web.Response(status=200)


async def order_api_parse_placeholders(request: web.Request, id, body) -> web.Response:
    """Parses a text and replaces all placeholders

    

    :param id: The id of the order
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = RechnungsdruckWebAppControllersApiOrderApiControllerParseTextContainer.from_dict(body)
    return web.Response(status=200)


async def order_api_patch_order(request: web.Request, id, body) -> web.Response:
    """Updates one or more fields of an order

    

    :param id: 
    :type id: int
    :param body: 
    :type body: 

    """
    return web.Response(status=200)


async def order_api_post_new_order(request: web.Request, body, shop_id=None) -> web.Response:
    """Creates a new order in the Billbee account

    To create an order POST an JSON object to the orders endpoint with the shown properties.  Not all properties are required.

    :param body: 
    :type body: dict | bytes
    :param shop_id: Deprecated, if orderData.ApiAccountId is set, it will be used instead of &#39;shopId&#39;
    :type shop_id: int

    """
    body = BillbeeInterfacesBillbeeAPIModelOrder.from_dict(body)
    return web.Response(status=200)


async def order_api_send_message(request: web.Request, id, body) -> web.Response:
    """Sends a message to the buyer

    

    :param id: The id of the order
    :type id: int
    :param body: The message model
    :type body: dict | bytes

    """
    body = RechnungsdruckWebAppControllersApiOrderApiControllerSendMessageModel.from_dict(body)
    return web.Response(status=200)


async def order_api_tags_create(request: web.Request, id, body) -> web.Response:
    """Attach one or more tags to an order

    When a tag is already attached, it is ignored. Tags are not case sensitive. All given tags are added to the existing tags.

    :param id: The internal id of the order
    :type id: int
    :param body: Tags to attach
    :type body: dict | bytes

    """
    body = RechnungsdruckWebAppControllersApiOrderTagCreate.from_dict(body)
    return web.Response(status=200)


async def order_api_tags_update(request: web.Request, id, body) -> web.Response:
    """Sets the tags attached to an order

    All existing tags will be replaced by the given list of new tags. To just add tags, use POST method.

    :param id: The internal id of the order
    :type id: int
    :param body: Tags to attach
    :type body: dict | bytes

    """
    body = RechnungsdruckWebAppControllersApiOrderTagCreate.from_dict(body)
    return web.Response(status=200)


async def order_api_trigger_event(request: web.Request, id, body) -> web.Response:
    """Triggers a rule event

    

    :param id: The id of the order
    :type id: int
    :param body: 
    :type body: dict | bytes

    """
    body = RechnungsdruckWebAppControllersApiOrderApiControllerTriggerEventContainer.from_dict(body)
    return web.Response(status=200)


async def order_api_update_state(request: web.Request, id, body) -> web.Response:
    """Changes the main state of a single order

    ### REMARKS ###  Use this call to change the state of an order to i.e. paid or sent.    The state is transfered to the external shop/marketplace if configured.  This is the list of known states:  - 1: ordered  - 2: confirmed  - 3: paid  - 4: shipped  - 5: reclamation  - 6: deleted  - 7: closed  - 8: canceled  - 9: archived  - 10: not used  - 11: demand note 1  - 12: demand note 2  - 13: packed  - 14: offered  - 15: payment reminder  - 16: fulfilling

    :param id: The internal id of the order
    :type id: int
    :param body: The data used to change the state
    :type body: dict | bytes

    """
    body = RechnungsdruckWebAppControllersApiOrderStateUpdate.from_dict(body)
    return web.Response(status=200)


async def search_search_1(request: web.Request, body) -> web.Response:
    """Search for products, customers and orders.  Type can be \&quot;order\&quot;, \&quot;product\&quot; and / or \&quot;customer\&quot;  Term can contains lucene query syntax

    

    :param body: 
    :type body: dict | bytes

    """
    body = RechnungsdruckWebAppControllersApiSearchControllerSearchModel.from_dict(body)
    return web.Response(status=200)
