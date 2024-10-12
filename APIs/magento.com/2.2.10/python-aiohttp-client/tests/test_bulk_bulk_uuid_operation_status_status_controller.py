# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_asynchronous_operations_bulk_status_v1_get_operations_count_by_bulk_id_and_status_get(client):
    """Test case for asynchronous_operations_bulk_status_v1_get_operations_count_by_bulk_id_and_status_get

    bulk/{bulkUuid}/operation-status/{status}
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/bulk/{bulk_uuid}/operation-status/{status}'.format(bulk_uuid='bulk_uuid_example', status=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

