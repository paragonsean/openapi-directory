# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.statistic import Statistic


pytestmark = pytest.mark.asyncio

async def test_get_statistic(client):
    """Test case for get_statistic

    Retrieve usage statistics
    """
    params = [('config_id', 'config_id_example'),
                    ('interval', 'interval_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/statistics.{content_type}'.format(content_type='content_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

