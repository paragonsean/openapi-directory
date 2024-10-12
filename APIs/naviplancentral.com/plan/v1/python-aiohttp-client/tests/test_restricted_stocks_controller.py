# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.restricted_stock_model import RestrictedStockModel
from openapi_server.models.restricted_stocks_model import RestrictedStocksModel


pytestmark = pytest.mark.asyncio

async def test_restricted_stocks_get_by_id_planid(client):
    """Test case for restricted_stocks_get_by_id_planid

    Retrieve a restricted stock
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/RestrictedStocks/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_restricted_stocks_get_by_planid(client):
    """Test case for restricted_stocks_get_by_planid

    Retrieve restricted stocks
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/RestrictedStocks',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

