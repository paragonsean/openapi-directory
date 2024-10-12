# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.click_model_pg import ClickModelPg
from openapi_server.models.clicks_filter_model import ClicksFilterModel


pytestmark = pytest.mark.asyncio

async def test_get_statistics(client):
    """Test case for get_statistics

    Get clicks statistics
    """
    body = {"aliasId":"aBcDe012","domain":"short.fyi","dateTo":"2001-05-02","lastId":100,"dateFrom":"2001-05-02"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'ApiKeyAuth': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/clicks/pg',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

