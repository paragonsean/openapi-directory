from typing import List, Dict
from aiohttp import web

from openapi_server.models.get_inventory200_response import GetInventory200Response
from openapi_server.models.get_multi_node_inventory_for_all_sku_and_all_ship_nodes200_response import GetMultiNodeInventoryForAllSkuAndAllShipNodes200Response
from openapi_server.models.get_multi_node_inventory_for_sku_and_all_shipnodes200_response import GetMultiNodeInventoryForSkuAndAllShipnodes200Response
from openapi_server.models.get_wfs_inventory200_response import GetWFSInventory200Response
from openapi_server.models.update_bulk_inventory200_response import UpdateBulkInventory200Response
from openapi_server.models.update_multi_node_inventory200_response import UpdateMultiNodeInventory200Response
from openapi_server.models.update_multi_node_inventory_request import UpdateMultiNodeInventoryRequest
from openapi_server import util


async def get_inventory(request: web.Request, sku, wm_sec_access_token, wm_qos_correlation_id, wm_svc_name, ship_node=None, wm_consumer_channel_type=None) -> web.Response:
    """Inventory

    You can use this API to get the inventory for a given item.

    :param sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: &#39;:&#39;, &#39;/&#39;, &#39;?&#39;, &#39;#&#39;, &#39;[&#39;, &#39;]&#39;, &#39;@&#39;, &#39;!&#39;, &#39;$&#39;, &#39;&amp;&#39;, \&quot;&#39;\&quot;, &#39;(&#39;, &#39;)&#39;, &#39;*&#39;, &#39;+&#39;, &#39;,&#39;, &#39;;&#39;, &#39;&#x3D;&#39;, ‘ ’, &#39;{&#39;, &#39;}&#39; as well as &#39;%&#39; itself if it&#39;s a part of sku. Make sure to encode space with %20. Other characters don&#39;t need to be encoded.
    :type sku: str
    :param wm_sec_access_token: The access token retrieved in the Token API call
    :type wm_sec_access_token: str
    :param wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    :type wm_qos_correlation_id: str
    :param wm_svc_name: Walmart Service Name
    :type wm_svc_name: str
    :param ship_node: The shipNode for which the inventory is requested
    :type ship_node: str
    :param wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    :type wm_consumer_channel_type: str

    """
    return web.Response(status=200)


async def get_multi_node_inventory_for_all_sku_and_all_ship_nodes(request: web.Request, wm_sec_access_token, wm_qos_correlation_id, wm_svc_name, limit=None, next_cursor=None, wm_consumer_channel_type=None) -> web.Response:
    """Multiple Item Inventory for All Ship Nodes

    This API will retrieve the inventory count for all of a seller&#39;s items across all ship nodes by item to ship node mapping. Inventory can be zero or non-zero. Please note that NextCursor value changes and it needs to be passed on from the previous call to next call.

    :param wm_sec_access_token: The access token retrieved in the Token API call
    :type wm_sec_access_token: str
    :param wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    :type wm_qos_correlation_id: str
    :param wm_svc_name: Walmart Service Name
    :type wm_svc_name: str
    :param limit: The number of items returned. Cannot be more than 50.
    :type limit: str
    :param next_cursor: String returned from initial API call to indicate pagination. Specify nextCursor value to retrieve the next 50 items.
    :type next_cursor: str
    :param wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    :type wm_consumer_channel_type: str

    """
    return web.Response(status=200)


async def get_multi_node_inventory_for_sku_and_all_shipnodes(request: web.Request, sku, wm_sec_access_token, wm_qos_correlation_id, wm_svc_name, ship_node=None, wm_consumer_channel_type=None) -> web.Response:
    """Single Item Inventory by Ship Node

    This API will retrieve the inventory count for an item across all ship nodes or one specific ship node. You can specify the ship node for which you want to fetch the inventory

    :param sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: &#39;:&#39;, &#39;/&#39;, &#39;?&#39;, &#39;#&#39;, &#39;[&#39;, &#39;]&#39;, &#39;@&#39;, &#39;!&#39;, &#39;$&#39;, &#39;&amp;&#39;, \&quot;&#39;\&quot;, &#39;(&#39;, &#39;)&#39;, &#39;*&#39;, &#39;+&#39;, &#39;,&#39;, &#39;;&#39;, &#39;&#x3D;&#39;, ‘ ’ as well as &#39;%&#39; itself if it&#39;s a part of sku. Make sure to encode space with %20. Other characters don&#39;t need to be encoded.
    :type sku: str
    :param wm_sec_access_token: The access token retrieved in the Token API call
    :type wm_sec_access_token: str
    :param wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    :type wm_qos_correlation_id: str
    :param wm_svc_name: Walmart Service Name
    :type wm_svc_name: str
    :param ship_node: ShipNode Id of the ship node for which the inventory is requested
    :type ship_node: str
    :param wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    :type wm_consumer_channel_type: str

    """
    return web.Response(status=200)


async def get_wfs_inventory(request: web.Request, wm_sec_access_token, wm_qos_correlation_id, wm_svc_name, sku=None, from_modified_date=None, to_modified_date=None, limit=None, offset=None, wm_consumer_channel_type=None) -> web.Response:
    """WFS Inventory

    You can use this API to get the current Available to Sell inventory quantities for all WFS items in your catalog. You can also query specific SKUs or filter to only items updated after a specific date in order to reduce the response size.

    :param wm_sec_access_token: The access token retrieved in the Token API call
    :type wm_sec_access_token: str
    :param wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    :type wm_qos_correlation_id: str
    :param wm_svc_name: Walmart Service Name
    :type wm_svc_name: str
    :param sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: &#39;:&#39;, &#39;/&#39;, &#39;?&#39;, &#39;#&#39;, &#39;[&#39;, &#39;]&#39;, &#39;@&#39;, &#39;!&#39;, &#39;$&#39;, &#39;&amp;&#39;, \&quot;&#39;\&quot;, &#39;(&#39;, &#39;)&#39;, &#39;*&#39;, &#39;+&#39;, &#39;,&#39;, &#39;;&#39;, &#39;&#x3D;&#39;, ‘ ’ as well as &#39;%&#39; itself if it&#39;s a part of sku. Make sure to encode space with %20. Other characters don&#39;t need to be encoded.
    :type sku: str
    :param from_modified_date: last inventory modified date - starting range.
    :type from_modified_date: str
    :param to_modified_date: last inventory modified date - starting range.
    :type to_modified_date: str
    :param limit: Number of Sku to be returned. Cannot be larger than 300.
    :type limit: str
    :param offset: Offset is the number of records you wish to skip before selecting records.
    :type offset: str
    :param wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    :type wm_consumer_channel_type: str

    """
    return web.Response(status=200)


async def update_bulk_inventory(request: web.Request, feed_type, wm_sec_access_token, wm_qos_correlation_id, wm_svc_name, file, ship_node=None, wm_consumer_channel_type=None) -> web.Response:
    """Bulk Item Inventory Update

    Updates inventory for items in bulk.  Seller Can either use feed type \&quot;inventory\&quot; or \&quot;MP_INVENTORY\&quot;  * Inventory spec 1.4 feed type: inventory  * Inventory spec 1.5 feed type: MP_INVENTORY   Please Note: Multi Node Inventory Update Feed (feedType&#x3D;MP_INVENTORY) only supports JSON Request and Responses. Refer to \&quot;MultiNode_Bulk_Inventory_Update_Request.json\&quot; for the corresponding request sample    Refer to the &lt;a href&#x3D;\&quot;https://developer.walmart.com/doc/us/us-mp/us-mp-inventory/\&quot;&gt;guide section&lt;/a&gt; for more detailed guide around each of the feed types    Refer to the throttling limits before uploading the Feed Files.

    :param feed_type: The feed Type
    :type feed_type: str
    :param wm_sec_access_token: The access token retrieved in the Token API call
    :type wm_sec_access_token: str
    :param wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    :type wm_qos_correlation_id: str
    :param wm_svc_name: Walmart Service Name
    :type wm_svc_name: str
    :param file: Feed file to upload
    :type file: str
    :param ship_node: The shipNode for which the inventory is to be updated. Not required in case of Multi Node Inventory Update Feed (feedType&#x3D;MP_INVENTORY)
    :type ship_node: str
    :param wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    :type wm_consumer_channel_type: str

    """
    return web.Response(status=200)


async def update_inventory_for_an_item(request: web.Request, sku, wm_sec_access_token, wm_qos_correlation_id, wm_svc_name, body, ship_node=None, wm_consumer_channel_type=None) -> web.Response:
    """Update inventory

    Updates the inventory for a given item.

    :param sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: &#39;:&#39;, &#39;/&#39;, &#39;?&#39;, &#39;#&#39;, &#39;[&#39;, &#39;]&#39;, &#39;@&#39;, &#39;!&#39;, &#39;$&#39;, &#39;&amp;&#39;, \&quot;&#39;\&quot;, &#39;(&#39;, &#39;)&#39;, &#39;*&#39;, &#39;+&#39;, &#39;,&#39;, &#39;;&#39;, &#39;&#x3D;&#39;, ‘ ’, &#39;{&#39;, &#39;}&#39; as well as &#39;%&#39; itself if it&#39;s a part of sku. Make sure to encode space with %20. Other characters don&#39;t need to be encoded.
    :type sku: str
    :param wm_sec_access_token: The access token retrieved in the Token API call
    :type wm_sec_access_token: str
    :param wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    :type wm_qos_correlation_id: str
    :param wm_svc_name: Walmart Service Name
    :type wm_svc_name: str
    :param body: File fields
    :type body: dict | bytes
    :param ship_node: The shipNode for which the inventory is to be updated.
    :type ship_node: str
    :param wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    :type wm_consumer_channel_type: str

    """
    body = GetInventory200Response.from_dict(body)
    return web.Response(status=200)


async def update_multi_node_inventory(request: web.Request, sku, wm_sec_access_token, wm_qos_correlation_id, wm_svc_name, body, wm_consumer_channel_type=None) -> web.Response:
    """Update Item Inventory per Ship Node

    This API will update the inventory for an item across one or more fulfillment centers, known as ship nodes.

    :param sku: An arbitrary alphanumeric unique ID, specified by the seller, which identifies each item. This will be used by the seller in the XSD file to refer to each item. Special characters in the sku needing encoding are: &#39;:&#39;, &#39;/&#39;, &#39;?&#39;, &#39;#&#39;, &#39;[&#39;, &#39;]&#39;, &#39;@&#39;, &#39;!&#39;, &#39;$&#39;, &#39;&amp;&#39;, \&quot;&#39;\&quot;, &#39;(&#39;, &#39;)&#39;, &#39;*&#39;, &#39;+&#39;, &#39;,&#39;, &#39;;&#39;, &#39;&#x3D;&#39;, ‘ ’ as well as &#39;%&#39; itself if it&#39;s a part of sku. Make sure to encode space with %20. Other characters don&#39;t need to be encoded.
    :type sku: str
    :param wm_sec_access_token: The access token retrieved in the Token API call
    :type wm_sec_access_token: str
    :param wm_qos_correlation_id: A unique ID which identifies each API call and used to track and debug issues; use a random generated GUID for this ID
    :type wm_qos_correlation_id: str
    :param wm_svc_name: Walmart Service Name
    :type wm_svc_name: str
    :param body: Request fields
    :type body: dict | bytes
    :param wm_consumer_channel_type: A unique ID to track the consumer request by channel. Use the Consumer Channel Type received during onboarding
    :type wm_consumer_channel_type: str

    """
    body = UpdateMultiNodeInventoryRequest.from_dict(body)
    return web.Response(status=200)
