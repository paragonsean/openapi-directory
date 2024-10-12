# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.wl_status_group import WlStatusGroup


pytestmark = pytest.mark.asyncio

async def test_status_report_get(client):
    """Test case for status_report_get

    Get status_report
    """
    headers = { 
        'Accept': 'application/vnd.wl.status.group+json; type=collection',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/status_report/',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

