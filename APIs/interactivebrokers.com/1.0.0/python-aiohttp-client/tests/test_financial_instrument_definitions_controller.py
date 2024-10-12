# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.marketdata_snapshot_get_request_inner import MarketdataSnapshotGetRequestInner
from openapi_server.models.secdef_get200_response_inner import SecdefGet200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_secdef_get(client):
    """Test case for secdef_get

    Get security definition
    """
    body = openapi_server.MarketdataSnapshotGetRequestInner()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'cookieAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tradingapi/v1/secdef',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

