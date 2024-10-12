# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.report_usage_batch_request import ReportUsageBatchRequest
from openapi_server.models.report_usage_batch_response import ReportUsageBatchResponse


pytestmark = pytest.mark.asyncio

async def test_v3_usage_batches_id_put(client):
    """Test case for v3_usage_batches_id_put

    Report usage of assets via a batch format.
    """
    body = openapi_server.ReportUsageBatchRequest()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
        'Api-Key': 'special-key',
    }
    response = await client.request(
        method='PUT',
        path='/v3/usage-batches/{id}'.format(id='id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

