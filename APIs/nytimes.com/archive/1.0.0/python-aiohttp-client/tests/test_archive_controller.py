# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.year_month_json_get200_response import YearMonthJsonGet200Response


pytestmark = pytest.mark.asyncio

async def test_year_month_json_get(client):
    """Test case for year_month_json_get

    Archive API
    """
    headers = { 
        'Accept': 'application/json',
        'apikey': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/svc/archive/v1/{year}/{month_jso}'.format(year=56, month=56),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

