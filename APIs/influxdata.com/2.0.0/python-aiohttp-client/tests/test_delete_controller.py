# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.delete_predicate_request import DeletePredicateRequest
from openapi_server.models.error import Error


pytestmark = pytest.mark.asyncio

async def test_post_delete(client):
    """Test case for post_delete

    Delete time series data from InfluxDB
    """
    body = {"predicate":"tag1=\"value1\" and (tag2=\"value2\" and tag3!=\"value3\")","stop":"2000-01-23T04:56:07.000+00:00","start":"2000-01-23T04:56:07.000+00:00"}
    params = [('org', 'org_example'),
                    ('bucket', 'bucket_example'),
                    ('orgID', 'org_id_example'),
                    ('bucketID', 'bucket_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='POST',
        path='/api/v2/delete',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

