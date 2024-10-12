# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.inventory_availability_expansions import InventoryAvailabilityExpansions
from openapi_server.models.inventory_item_availability_dto_paged_result import InventoryItemAvailabilityDtoPagedResult
from openapi_server.models.problem_details import ProblemDetails


pytestmark = pytest.mark.asyncio

async def test_inventory_get_list(client):
    """Test case for inventory_get_list

    Gets an inventory summary for inventory items.
    """
    params = [('inventoryId', ['inventory_id_example']),
                    ('warehouseId', ['warehouse_id_example']),
                    ('locationId', ['location_id_example']),
                    ('expand', [openapi_server.InventoryAvailabilityExpansions()]),
                    ('modifiedSince', '2013-10-20T19:20:30+01:00'),
                    ('attributeFilter', ['attribute_filter_example']),
                    ('pageSize', 56),
                    ('pageIndex', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v3/Inventory',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

