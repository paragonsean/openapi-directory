# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.chart_axes import ChartAxes


pytestmark = pytest.mark.asyncio

async def test_chart_axes_get_id(client):
    """Test case for chart_axes_get_id

    Axes: Get by Id
    """
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/ooxml-automation/Charts/Axes/{id}'.format(id='id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

