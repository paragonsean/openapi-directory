# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.telegraf_plugins import TelegrafPlugins


pytestmark = pytest.mark.asyncio

async def test_get_telegraf_plugins(client):
    """Test case for get_telegraf_plugins

    List all Telegraf plugins
    """
    params = [('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'zap_trace_span': '{\"baggage\":{\"key\":\"value\"},\"span_id\":\"1\",\"trace_id\":\"1\"}',
    }
    response = await client.request(
        method='GET',
        path='/api/v2/telegraf/plugins',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

