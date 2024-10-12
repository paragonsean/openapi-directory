# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.bulk_sla_conflicts_summary import BulkSlaConflictsSummary
from openapi_server.models.hierarchy_object_ids import HierarchyObjectIds


pytestmark = pytest.mark.asyncio

async def test_bulk_hierarchy_sla_conflicts_v1(client):
    """Test case for bulk_hierarchy_sla_conflicts_v1

    Retrieve the list of descendant objects with SLA conflicts in bulk
    """
    body = {"ids":["ids","ids"]}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
        'Bearer': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/hierarchy/bulk_sla_conflicts',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

