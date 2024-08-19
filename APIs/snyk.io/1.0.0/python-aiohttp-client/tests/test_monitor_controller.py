# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.monitor_dep_graph_request import MonitorDepGraphRequest


pytestmark = pytest.mark.asyncio

async def test_monitor_dep_graph(client):
    """Test case for monitor_dep_graph

    Monitor Dep Graph
    """
    body = openapi_server.MonitorDepGraphRequest()
    params = [('org', '9695cbb1-3a87-4d6f-8ae1-61a1c37ee9f7')]
    headers = { 
        'Accept': 'application/json; charset=utf-8',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/v1/monitor/dep-graph',
        headers=headers,
        json=body,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

