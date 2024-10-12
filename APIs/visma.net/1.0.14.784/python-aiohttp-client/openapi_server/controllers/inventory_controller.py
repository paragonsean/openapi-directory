from typing import List, Dict
from aiohttp import web

from openapi_server.models.inventory_availability_expansions import InventoryAvailabilityExpansions
from openapi_server.models.inventory_item_availability_dto_paged_result import InventoryItemAvailabilityDtoPagedResult
from openapi_server.models.problem_details import ProblemDetails
from openapi_server import util


async def inventory_get_list(request: web.Request, inventory_id=None, warehouse_id=None, location_id=None, expand=None, modified_since=None, attribute_filter=None, page_size=None, page_index=None) -> web.Response:
    """Gets an inventory summary for inventory items.

    Sample request:                GET /inventory?inventoryId&#x3D;Item1                GET /inventory?warehouseId&#x3D;MAIN&amp;modifiedSince&#x3D;2021-08-01T12:00:00&amp;pageSize&#x3D;1000                GET /inventory?inventoryId&#x3D;Item1&amp;InventoryId&#x3D;Item2&amp;expand&#x3D;location,attribute                GET /inventory?expand&#x3D;location&amp;attributeFilter&#x3D;WEBSHOP:1

    :param inventory_id: A list of zero or more inventory items to get a summary for. If no inventoryId is passed, all inventory items will be included in the response.
    :type inventory_id: List[str]
    :param warehouse_id: A list of zero or more warehouses to get a summary for. If no warehouse is supplied, all warehouses will be included in the response.
    :type warehouse_id: List[str]
    :param location_id: A list of zero or more locations to get a summary for. If no location is supplied, all locations will be included in the response.
    :type location_id: List[str]
    :param expand: An additional option to include location detail information with the warehouse summary, or attribute details for the inventory item. If this is not supplied, location information or attributes will not be included in the response.
    :type expand: list | bytes
    :param modified_since: A date/time value for filtering when an inventory item&#39;s warehouse or location availability last changed  Unless a specific time zone offset is included (e.g. &#39;2012-12-24T12:15:14+02:00&#39;), the date is considered to be in the UTC time zone.
    :type modified_since: str
    :param attribute_filter: One or more attribute filter values specified as attribute-id:attribute-value. For example \&quot;attributeFilter&#x3D;WEBSHOP:1&amp;attributeFilter&#x3D;AnotherAttribute:someValue\&quot;  If two attributeFilter values have the same attribute-Id either one need to match.
    :type attribute_filter: List[str]
    :param page_size: The number of inventory items retrieved per page. If not specified the default pagesize is 10000 items per page
    :type page_size: int
    :param page_index: Gets or sets the zero based page index to get
    :type page_index: int

    """
    expand = [InventoryAvailabilityExpansions.from_dict(d) for d in expand]
    modified_since = util.deserialize_datetime(modified_since)
    return web.Response(status=200)
