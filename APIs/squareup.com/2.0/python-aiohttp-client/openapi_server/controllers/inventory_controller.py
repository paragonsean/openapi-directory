from typing import List, Dict
from aiohttp import web

from openapi_server.models.batch_change_inventory_request import BatchChangeInventoryRequest
from openapi_server.models.batch_change_inventory_response import BatchChangeInventoryResponse
from openapi_server.models.batch_retrieve_inventory_changes_request import BatchRetrieveInventoryChangesRequest
from openapi_server.models.batch_retrieve_inventory_changes_response import BatchRetrieveInventoryChangesResponse
from openapi_server.models.batch_retrieve_inventory_counts_request import BatchRetrieveInventoryCountsRequest
from openapi_server.models.batch_retrieve_inventory_counts_response import BatchRetrieveInventoryCountsResponse
from openapi_server.models.retrieve_inventory_adjustment_response import RetrieveInventoryAdjustmentResponse
from openapi_server.models.retrieve_inventory_changes_response import RetrieveInventoryChangesResponse
from openapi_server.models.retrieve_inventory_count_response import RetrieveInventoryCountResponse
from openapi_server.models.retrieve_inventory_physical_count_response import RetrieveInventoryPhysicalCountResponse
from openapi_server.models.retrieve_inventory_transfer_response import RetrieveInventoryTransferResponse
from openapi_server import util


async def batch_change_inventory(request: web.Request, body) -> web.Response:
    """BatchChangeInventory

    Applies adjustments and counts to the provided item quantities.  On success: returns the current calculated counts for all objects referenced in the request. On failure: returns a list of related errors.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = BatchChangeInventoryRequest.from_dict(body)
    return web.Response(status=200)


async def batch_retrieve_inventory_changes(request: web.Request, body) -> web.Response:
    """BatchRetrieveInventoryChanges

    Returns historical physical counts and adjustments based on the provided filter criteria.  Results are paginated and sorted in ascending order according their &#x60;occurred_at&#x60; timestamp (oldest first).  BatchRetrieveInventoryChanges is a catch-all query endpoint for queries that cannot be handled by other, simpler endpoints.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = BatchRetrieveInventoryChangesRequest.from_dict(body)
    return web.Response(status=200)


async def batch_retrieve_inventory_counts(request: web.Request, body) -> web.Response:
    """BatchRetrieveInventoryCounts

    Returns current counts for the provided [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject)s at the requested [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location)s.  Results are paginated and sorted in descending order according to their &#x60;calculated_at&#x60; timestamp (newest first).  When &#x60;updated_after&#x60; is specified, only counts that have changed since that time (based on the server timestamp for the most recent change) are returned. This allows clients to perform a \&quot;sync\&quot; operation, for example in response to receiving a Webhook notification.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = BatchRetrieveInventoryCountsRequest.from_dict(body)
    return web.Response(status=200)


async def deprecated_batch_change_inventory(request: web.Request, body) -> web.Response:
    """DeprecatedBatchChangeInventory

    Deprecated version of [BatchChangeInventory](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-change-inventory) after the endpoint URL  is updated to conform to the standard convention.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = BatchChangeInventoryRequest.from_dict(body)
    return web.Response(status=200)


async def deprecated_batch_retrieve_inventory_changes(request: web.Request, body) -> web.Response:
    """DeprecatedBatchRetrieveInventoryChanges

    Deprecated version of [BatchRetrieveInventoryChanges](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-retrieve-inventory-changes) after the endpoint URL  is updated to conform to the standard convention.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = BatchRetrieveInventoryChangesRequest.from_dict(body)
    return web.Response(status=200)


async def deprecated_batch_retrieve_inventory_counts(request: web.Request, body) -> web.Response:
    """DeprecatedBatchRetrieveInventoryCounts

    Deprecated version of [BatchRetrieveInventoryCounts](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-retrieve-inventory-counts) after the endpoint URL  is updated to conform to the standard convention.

    :param body: An object containing the fields to POST for the request.  See the corresponding object definition for field details.
    :type body: dict | bytes

    """
    body = BatchRetrieveInventoryCountsRequest.from_dict(body)
    return web.Response(status=200)


async def deprecated_retrieve_inventory_adjustment(request: web.Request, adjustment_id) -> web.Response:
    """DeprecatedRetrieveInventoryAdjustment

    Deprecated version of [RetrieveInventoryAdjustment](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/retrieve-inventory-adjustment) after the endpoint URL  is updated to conform to the standard convention.

    :param adjustment_id: ID of the [InventoryAdjustment](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryAdjustment) to retrieve.
    :type adjustment_id: str

    """
    return web.Response(status=200)


async def deprecated_retrieve_inventory_physical_count(request: web.Request, physical_count_id) -> web.Response:
    """DeprecatedRetrieveInventoryPhysicalCount

    Deprecated version of [RetrieveInventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/retrieve-inventory-physical-count) after the endpoint URL  is updated to conform to the standard convention.

    :param physical_count_id: ID of the [InventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryPhysicalCount) to retrieve.
    :type physical_count_id: str

    """
    return web.Response(status=200)


async def retrieve_inventory_adjustment(request: web.Request, adjustment_id) -> web.Response:
    """RetrieveInventoryAdjustment

    Returns the [InventoryAdjustment](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryAdjustment) object with the provided &#x60;adjustment_id&#x60;.

    :param adjustment_id: ID of the [InventoryAdjustment](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryAdjustment) to retrieve.
    :type adjustment_id: str

    """
    return web.Response(status=200)


async def retrieve_inventory_changes(request: web.Request, catalog_object_id, location_ids=None, cursor=None) -> web.Response:
    """RetrieveInventoryChanges

    Returns a set of physical counts and inventory adjustments for the provided [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) at the requested [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location)s.   You can achieve the same result by calling [BatchRetrieveInventoryChanges](https://developer.squareup.com/reference/square_2021-08-18/inventory-api/batch-retrieve-inventory-changes)  and having the &#x60;catalog_object_ids&#x60; list contain a single element of the &#x60;CatalogObject&#x60; ID.  Results are paginated and sorted in descending order according to their &#x60;occurred_at&#x60; timestamp (newest first).  There are no limits on how far back the caller can page. This endpoint can be  used to display recent changes for a specific item. For more sophisticated queries, use a batch endpoint.

    :param catalog_object_id: ID of the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) to retrieve.
    :type catalog_object_id: str
    :param location_ids: The [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) IDs to look up as a comma-separated list. An empty list queries all locations.
    :type location_ids: str
    :param cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for the original query.  See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    :type cursor: str

    """
    return web.Response(status=200)


async def retrieve_inventory_count(request: web.Request, catalog_object_id, location_ids=None, cursor=None) -> web.Response:
    """RetrieveInventoryCount

    Retrieves the current calculated stock count for a given [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) at a given set of [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location)s. Responses are paginated and unsorted. For more sophisticated queries, use a batch endpoint.

    :param catalog_object_id: ID of the [CatalogObject](https://developer.squareup.com/reference/square_2021-08-18/objects/CatalogObject) to retrieve.
    :type catalog_object_id: str
    :param location_ids: The [Location](https://developer.squareup.com/reference/square_2021-08-18/objects/Location) IDs to look up as a comma-separated list. An empty list queries all locations.
    :type location_ids: str
    :param cursor: A pagination cursor returned by a previous call to this endpoint. Provide this to retrieve the next set of results for the original query.  See the [Pagination](https://developer.squareup.com/docs/working-with-apis/pagination) guide for more information.
    :type cursor: str

    """
    return web.Response(status=200)


async def retrieve_inventory_physical_count(request: web.Request, physical_count_id) -> web.Response:
    """RetrieveInventoryPhysicalCount

    Returns the [InventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryPhysicalCount) object with the provided &#x60;physical_count_id&#x60;.

    :param physical_count_id: ID of the [InventoryPhysicalCount](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryPhysicalCount) to retrieve.
    :type physical_count_id: str

    """
    return web.Response(status=200)


async def retrieve_inventory_transfer(request: web.Request, transfer_id) -> web.Response:
    """RetrieveInventoryTransfer

    Returns the [InventoryTransfer](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryTransfer) object with the provided &#x60;transfer_id&#x60;.

    :param transfer_id: ID of the [InventoryTransfer](https://developer.squareup.com/reference/square_2021-08-18/objects/InventoryTransfer) to retrieve.
    :type transfer_id: str

    """
    return web.Response(status=200)
