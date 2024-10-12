# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.marketdata_exchange_components_get200_response_inner import MarketdataExchangeComponentsGet200ResponseInner
from openapi_server.models.marketdata_snapshot_get200_response_inner import MarketdataSnapshotGet200ResponseInner
from openapi_server.models.marketdata_snapshot_get_request_inner import MarketdataSnapshotGetRequestInner


pytestmark = pytest.mark.asyncio

async def test_marketdata_exchange_components_get(client):
    """Test case for marketdata_exchange_components_get

    Exchange Components
    """
    headers = { 
        'Accept': 'application/json',
        'cookieAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tradingapi/v1/marketdata/exchange_components',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_marketdata_snapshot_get(client):
    """Test case for marketdata_snapshot_get

    Market Data Snapshot
    """
    body = [openapi_server.MarketdataSnapshotGetRequestInner()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'cookieAuth': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/tradingapi/v1/marketdata/snapshot',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

