from typing import List, Dict
from aiohttp import web

from openapi_server.models.add_sales_order_lines_command import AddSalesOrderLinesCommand
from openapi_server.models.new_sales_order_command import NewSalesOrderCommand
from openapi_server.models.patch_sales_order_command import PatchSalesOrderCommand
from openapi_server.models.patch_sales_order_lines_command import PatchSalesOrderLinesCommand
from openapi_server.models.problem_details import ProblemDetails
from openapi_server.models.sales_order_commission_dto import SalesOrderCommissionDto
from openapi_server.models.sales_order_discount_dto import SalesOrderDiscountDto
from openapi_server.models.sales_order_dto import SalesOrderDto
from openapi_server.models.sales_order_expansions import SalesOrderExpansions
from openapi_server.models.sales_order_line_dto import SalesOrderLineDto
from openapi_server.models.sales_order_line_dto_paged_result import SalesOrderLineDtoPagedResult
from openapi_server.models.sales_order_list_dto_paged_result import SalesOrderListDtoPagedResult
from openapi_server.models.sales_order_rot_rut_dto import SalesOrderRotRutDto
from openapi_server.models.sales_order_shipment_dto import SalesOrderShipmentDto
from openapi_server.models.sales_order_tax_dto import SalesOrderTaxDto
from openapi_server.models.sales_order_validation_problem_details import SalesOrderValidationProblemDetails
from openapi_server import util


async def sales_orders_add_lines_typeorder_idlines(request: web.Request, type, order_id, body=None) -> web.Response:
    """Adds new lines to a existing sales order in the system

    If-Match header represents a version of Sales Order to be modified and must be included in request.  Value of current version is included in GET /salesorders/{type}/{orderId} and modification endpoints on that resource as ETag header.

    :param type: 
    :type type: str
    :param order_id: 
    :type order_id: str
    :param body: Information about the lines to create
    :type body: dict | bytes

    """
    body = AddSalesOrderLinesCommand.from_dict(body)
    return web.Response(status=200)


async def sales_orders_create_new_item(request: web.Request, body=None) -> web.Response:
    """Adds a new sales order to the system

    Sample requests:                &#x60;&#x60;&#x60;  POST /salesorders  {      \&quot;customer\&quot;: {        \&quot;id\&quot;: \&quot;10001\&quot;,      },      \&quot;type\&quot;: \&quot;SO\&quot;  }  &#x60;&#x60;&#x60;  &#x60;&#x60;&#x60;  POST /salesorders  {      \&quot;customer\&quot;: {        \&quot;id\&quot;: \&quot;10000\&quot;,        \&quot;order\&quot;: \&quot;some-customer-order-nbr\&quot;      },      \&quot;type\&quot;: \&quot;SO\&quot;,      \&quot;description\&quot;: \&quot;sample request order\&quot;,      \&quot;status\&quot;: \&quot;Hold\&quot;,      \&quot;orderLines\&quot;: [          {              \&quot;inventoryId\&quot;: \&quot;StockItem1\&quot;,              \&quot;quantity\&quot;: 4,              \&quot;unitPrice\&quot;: 101.25          }      ]  }  &#x60;&#x60;&#x60;

    :param body: Information about the sales order to create
    :type body: dict | bytes

    """
    body = NewSalesOrderCommand.from_dict(body)
    return web.Response(status=200)


async def sales_orders_delete_lines_typeorder_idlines(request: web.Request, type, order_id, ids=None) -> web.Response:
    """Delete lines from an existing sales order

    If-Match header represents a version of Sales Order to be modified and must be included in request.  Value of current version is included in GET /salesorders/{type}/{orderId} and modification endpoints on that resource as ETag header.

    :param type: The type of the order to make modifications to
    :type type: str
    :param order_id: The order number to make modifications to
    :type order_id: str
    :param ids: Lines to delete with comma seprator. Limit of line ids is 1000.
    :type ids: List[int]

    """
    return web.Response(status=200)


async def sales_orders_delete_typeorder_id(request: web.Request, type, order_id) -> web.Response:
    """Delete an existing sales order

    If-Match header represents a version of Sales Order to be modified and must be included in request.  Value of current version is included in GET /salesorders/{type}/{orderId} and modification endpoints on that resource as ETag header.

    :param type: The type of the order to delete
    :type type: str
    :param order_id: The order number to delete
    :type order_id: str

    """
    return web.Response(status=200)


async def sales_orders_get_item_async_typeorder_id(request: web.Request, type, order_id, expand=None) -> web.Response:
    """Gets information about a single sales order

    The expand query parameter corresponds to sections in the Visma.net.ERP.SalesOrders.Api.Dto.SalesOrder.SalesOrderDto.  If an expand value is not specified it will not be filled and returned in the response object.                Sample request:                &#x60;GET /salesorders/SO/000100?expand&#x3D;customer,payment&#x60;

    :param type: The type of sales order to get
    :type type: str
    :param order_id: The id of the sales order to get
    :type order_id: str
    :param expand: An optional specification of what details to include about the sales order. The default value if not supplied is \&quot;None\&quot;
    :type expand: list | bytes

    """
    expand = [SalesOrderExpansions.from_dict(d) for d in expand]
    return web.Response(status=200)


async def sales_orders_get_item_commissions_typeorder_idcommissions(request: web.Request, type, order_id) -> web.Response:
    """Gets commission information for a single sales order

    Sample request:                &#x60;GET /salesorders/SO/000101/commissions&#x60;

    :param type: The type of sales order to get
    :type type: str
    :param order_id: The id of the sales order to get
    :type order_id: str

    """
    return web.Response(status=200)


async def sales_orders_get_item_discounts_typeorder_iddiscounts(request: web.Request, type, order_id) -> web.Response:
    """Gets discount details information for a single sales order

    Sample request:                &#x60;GET /salesorders/SO/000101/discounts&#x60;

    :param type: The type of sales order to get
    :type type: str
    :param order_id: The id of the sales order to get
    :type order_id: str

    """
    return web.Response(status=200)


async def sales_orders_get_item_line_typeorder_idlinesline_id(request: web.Request, type, order_id, line_id) -> web.Response:
    """Gets a specific sales order line for a single sales order

    Sample request:                &#x60;GET /salesorders/SO/000101/lines/1&#x60;

    :param type: The type of sales order to get
    :type type: str
    :param order_id: The id of the sales order to get
    :type order_id: str
    :param line_id: The id of the line to get
    :type line_id: int

    """
    return web.Response(status=200)


async def sales_orders_get_item_lines_typeorder_idlines(request: web.Request, type, order_id, page_size=None, page_index=None) -> web.Response:
    """Gets sales order lines for a single sales order

    Sample request:                &#x60;GET /salesorders/SO/000101/lines&#x60;

    :param type: The type of sales order to get
    :type type: str
    :param order_id: The id of the sales order to get
    :type order_id: str
    :param page_size: The number of lines retrieved per page, defaults to 1000 if not specified
    :type page_size: int
    :param page_index: The zero based page index to retrieve, defaults to 0 if not specified
    :type page_index: int

    """
    return web.Response(status=200)


async def sales_orders_get_item_rot_rut_typeorder_idrotrut(request: web.Request, type, order_id) -> web.Response:
    """Gets ROT/RUT information for a single sales order

    Sample request:                &#x60;GET /salesorders/SO/000123/rotrut&#x60;

    :param type: The type of sales order to get
    :type type: str
    :param order_id: The id of the sales order to get
    :type order_id: str

    """
    return web.Response(status=200)


async def sales_orders_get_item_tax_typeorder_idtax(request: web.Request, type, order_id) -> web.Response:
    """Gets tax information for a single sales order

    Sample request:                &#x60;GET /salesorders/SO/000101/tax&#x60;

    :param type: The type of sales order to get
    :type type: str
    :param order_id: The id of the sales order to get
    :type order_id: str

    """
    return web.Response(status=200)


async def sales_orders_get_list(request: web.Request, customer_id=None, status=None, modified_since=None, page_size=None, page_index=None, order_by=None, filter=None) -> web.Response:
    """Gets a paged list with sales orders of any type

    Sample requests:                &#x60;GET /salesorders&#x60;                &#x60;GET /salesorders?customerId&#x3D;10000&amp;status&#x3D;Open&amp;pageSize&#x3D;10&#x60;                &#x60;GET /salesorders?orderBy&#x3D;lastModified%20asc&#x60;

    :param customer_id: The customer for which to retrieve orders. If omitted or empty, orders for all customers are included
    :type customer_id: str
    :param status: The order status to include in the result. If omitted or empty, orders with any status are included.
    :type status: str
    :param modified_since: A date/time value for filtering when a sales order last changed.  Unless a specific time zone offset is included (e.g. &#39;2012-12-24T12:15:14+02:00&#39;), the date is considered to be in the UTC time zone.
    :type modified_since: str
    :param page_size: The number of customers retrieved per page
    :type page_size: int
    :param page_index: The zero based page index to retrieve
    :type page_index: int
    :param order_by: The field to order the list by. Can be one of &#x60;created&#x60;, &#x60;lastModified&#x60;, or &#x60;orderId&#x60; followed by an optional sort direction (&#x60;asc&#x60; or &#x60;desc&#x60;), default direction is &#x60;asc&#x60; (ascending) if not present.
    :type order_by: str
    :param filter: A filter for the list, applied to the orderId
    :type filter: str

    """
    modified_since = util.deserialize_datetime(modified_since)
    return web.Response(status=200)


async def sales_orders_get_list_type(request: web.Request, type, customer_id=None, status=None, modified_since=None, page_size=None, page_index=None, order_by=None, filter=None) -> web.Response:
    """Gets a paged list with sales orders of a specific type

    Sample requests:                &#x60;GET /salesorders/SO&#x60;                &#x60;GET /salesorders/SO?customerId&#x3D;10000&amp;status&#x3D;Open&amp;pageSize&#x3D;10&#x60;                &#x60;GET /salesorders/SO?orderBy&#x3D;created%20desc&#x60;

    :param type: The type of sales orders to get.
    :type type: str
    :param customer_id: The customer for which to retrieve orders. If omitted or empty, orders for all customers are included
    :type customer_id: str
    :param status: The order status to include in the result. If omitted or empty, orders with any status are included.
    :type status: str
    :param modified_since: A date/time value for filtering when a sales order last changed.  Unless a specific time zone offset is included (e.g. &#39;2012-12-24T12:15:14+02:00&#39;), the date is considered to be in the UTC time zone.
    :type modified_since: str
    :param page_size: The number of customers retrieved per page
    :type page_size: int
    :param page_index: The zero based page index to retrieve
    :type page_index: int
    :param order_by: The field to order the list by. Can be one of &#x60;created&#x60;, &#x60;lastModified&#x60;, or &#x60;orderId&#x60; followed by an optional sort direction (&#x60;asc&#x60; or &#x60;desc&#x60;), default direction is &#x60;asc&#x60; (ascending) if not present.
    :type order_by: str
    :param filter: A filter for the list, applied to the orderId
    :type filter: str

    """
    modified_since = util.deserialize_datetime(modified_since)
    return web.Response(status=200)


async def sales_orders_get_sales_order_shipment_typeorder_idshipment(request: web.Request, type, order_id) -> web.Response:
    """Gets shipment information for a single sales order

    Sample request:                &#x60;GET /salesorders/SO/000101/shipment&#x60;

    :param type: The type of sales order to get
    :type type: str
    :param order_id: The id of the sales order to get
    :type order_id: str

    """
    return web.Response(status=200)


async def sales_orders_patch_lines_typeorder_idlines(request: web.Request, type, order_id, body=None) -> web.Response:
    """Make modifications to an existing sales order lines

    If-Match header represents a version of Sales Order to be modified and must be included in request.  Value of current version is included in GET /salesorders/{type}/{orderId} and modification endpoints on that resource as ETag header.

    :param type: The type of the order to make modifications to
    :type type: str
    :param order_id: The order number to make modifications to
    :type order_id: str
    :param body: Data to change about the sales order lines
    :type body: dict | bytes

    """
    body = PatchSalesOrderLinesCommand.from_dict(body)
    return web.Response(status=200)


async def sales_orders_patch_typeorder_id(request: web.Request, type, order_id, body=None) -> web.Response:
    """Make modifications to an existing sales order

    If-Match header represents a version of Sales Order to be modified and must be included in request.  Value of current version is included in GET /salesorders/{type}/{orderId} and modification endpoints on that resource as ETag header.

    :param type: The type of the order to make modifications to
    :type type: str
    :param order_id: The order number to make modifications to
    :type order_id: str
    :param body: Data to change about the sales order
    :type body: dict | bytes

    """
    body = PatchSalesOrderCommand.from_dict(body)
    return web.Response(status=200)
