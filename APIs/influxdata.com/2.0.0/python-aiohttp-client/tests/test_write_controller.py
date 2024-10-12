# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.line_protocol_error import LineProtocolError
from openapi_server.models.line_protocol_length_error import LineProtocolLengthError
from openapi_server.models.write_precision import WritePrecision


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("text/plain not supported by Connexion")
async def test_post_write(client):
    """Test case for post_write

    Write time series data into InfluxDB
    """
    body = 'body_example'
    params = [('org', 'org_example'),
                    ('orgID', 'org_id_example'),
                    ('bucket', 'bucket_example'),
                    ('precision', openapi_server.WritePrecision())]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'text/plain',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
        'content_encoding': identity,
        'content_type': text/plain; charset=utf-8,
        'content_length': 56,
        'accept': application/json,
    }
    response = await client.request(
        method='POST',
        path='/api/v2/write',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

