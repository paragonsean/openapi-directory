from typing import List, Dict
from aiohttp import web

from openapi_server.models.getinventorywithdispatchedreservations200_response_inner import Getinventorywithdispatchedreservations200ResponseInner
from openapi_server.models.inventory_by_sku200_response import InventoryBySku200Response
from openapi_server.models.inventoryperdock200_response_inner import Inventoryperdock200ResponseInner
from openapi_server.models.save_supply_lot import SaveSupplyLot
from openapi_server.models.update_inventory_by_skuand_warehouse_request1 import UpdateInventoryBySkuandWarehouseRequest1
from openapi_server import util


async def get_supply_lots(request: web.Request, accept, content_type, sku_id, warehouse_id) -> web.Response:
    """List supply lots

    Returns a list of the supply lots of an SKU in a specific warehouse.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param sku_id: ID of the SKU.
    :type sku_id: str
    :param warehouse_id: ID of the warehouse where the SKU is located.
    :type warehouse_id: str

    """
    return web.Response(status=200)


async def getinventorywithdispatchedreservations(request: web.Request, content_type, accept, item_id, warehouse_id) -> web.Response:
    """List inventory with dispatched reservations

    Lists inventory with dispatched reservations. When the number of active reservations is more than 2000 the return is an error with status code 400 (BadRequest) and the message: Too many active reservations.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param item_id: 
    :type item_id: str
    :param warehouse_id: 
    :type warehouse_id: str

    """
    return web.Response(status=200)


async def inventory_by_sku(request: web.Request, content_type, accept, sku_id) -> web.Response:
    """List inventory by SKU

    Lists your store&#39;s inventory by SKU ID

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param sku_id: 
    :type sku_id: str

    """
    return web.Response(status=200)


async def inventoryperdock(request: web.Request, content_type, accept, sku_id, dock_id) -> web.Response:
    """List inventory per dock

    Lists inventory information per dock set up in your store.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param sku_id: 
    :type sku_id: str
    :param dock_id: 
    :type dock_id: str

    """
    return web.Response(status=200)


async def inventoryperdockandwarehouse(request: web.Request, content_type, accept, sku_id, dock_id, warehouse_id) -> web.Response:
    """List inventory per dock and warehouse

    Lists information of inventory per dock and warehouse.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param sku_id: 
    :type sku_id: str
    :param dock_id: 
    :type dock_id: str
    :param warehouse_id: 
    :type warehouse_id: str

    """
    return web.Response(status=200)


async def inventoryperwarehouse(request: web.Request, content_type, accept, sku_id, warehouse_id) -> web.Response:
    """List inventory per warehouse

    Lists inventory information per warehouse on your store.

    :param content_type: Type of the content being sent
    :type content_type: str
    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param sku_id: 
    :type sku_id: str
    :param warehouse_id: 
    :type warehouse_id: str

    """
    return web.Response(status=200)


async def save_supply_lot(request: web.Request, accept, content_type, sku_id, warehouse_id, supply_lot_id, body) -> web.Response:
    """Save supply lot

    Creates a new Supply Lot. A Supply Lot lets the store sell products that are not currently available in stock but whose arrival is already scheduled.  Check out our [documentation](https://help.vtex.com/en/tutorial/setting-up-future-inventory--UMSGjooqRfkRbeoh94kS4) about this feature.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param content_type: Type of the content being sent
    :type content_type: str
    :param sku_id: ID of the SKU whose availability is being scheduled.
    :type sku_id: str
    :param warehouse_id: ID of the warehouse where the SKU will arrive.
    :type warehouse_id: str
    :param supply_lot_id: ID of the Supply Lot in which the SKU&#39;s scheduling should be considered.
    :type supply_lot_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = SaveSupplyLot.from_dict(body)
    return web.Response(status=200)


async def transfer_supply_lot(request: web.Request, accept, content_type, sku_id, warehouse_id, supply_lot_id) -> web.Response:
    """Transfer supply lot

    Transfers an SKU from a Supply Lot to the currently available inventory.  Check out how this transfer works in further detail by reading our [documentation](https://help.vtex.com/pt/tutorial/configurar-estoque-futuro--UMSGjooqRfkRbeoh94kS4) about this feature.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand
    :type accept: str
    :param content_type: Type of the content being sent
    :type content_type: str
    :param sku_id: ID of the SKU.
    :type sku_id: str
    :param warehouse_id: ID of the warehouse where the SKU is located.
    :type warehouse_id: str
    :param supply_lot_id: ID of the Supply Lot in which the SKU is currently located and from where it will be transfered.
    :type supply_lot_id: str

    """
    return web.Response(status=200)


async def update_inventory_by_skuand_warehouse(request: web.Request, accept, content_type, sku_id, warehouse_id, body) -> web.Response:
    """Update inventory by SKU and warehouse

    Updates inventory for a given SKU and warehouse.

    :param accept: HTTP Client Negotiation Accept Header. Indicates the types of responses the client can understand.
    :type accept: str
    :param content_type: Type of the content being sent.
    :type content_type: str
    :param sku_id: 
    :type sku_id: str
    :param warehouse_id: 
    :type warehouse_id: str
    :param body: 
    :type body: dict | bytes

    """
    body = UpdateInventoryBySkuandWarehouseRequest1.from_dict(body)
    return web.Response(status=200)
