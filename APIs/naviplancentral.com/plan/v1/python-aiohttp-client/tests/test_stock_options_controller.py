# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.stock_option_model import StockOptionModel
from openapi_server.models.stock_options_model import StockOptionsModel


pytestmark = pytest.mark.asyncio

async def test_stock_options_get_by_id_planid(client):
    """Test case for stock_options_get_by_id_planid

    Retrieve a stock option
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/StockOptions/{id}'.format(id=56),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_stock_options_get_by_planid(client):
    """Test case for stock_options_get_by_planid

    Retrieve stock options
    """
    params = [('planId', 'plan_id_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/plan/api/StockOptions',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

