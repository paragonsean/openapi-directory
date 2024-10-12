# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.asynchronous_operations_data_bulk_operations_status_interface import AsynchronousOperationsDataBulkOperationsStatusInterface
from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_asynchronous_operations_bulk_status_v1_get_bulk_short_status_get(client):
    """Test case for asynchronous_operations_bulk_status_v1_get_bulk_short_status_get

    bulk/{bulkUuid}/status
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/rest/default/V1/bulk/{bulk_uuid}/status'.format(bulk_uuid='bulk_uuid_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

