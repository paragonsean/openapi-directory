# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.summary_report_response import SummaryReportResponse


pytestmark = pytest.mark.asyncio

async def test_get_promotion_summary_report(client):
    """Test case for get_promotion_summary_report

    
    """
    params = [('marketplace_id', 'marketplace_id_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/marketing/v1/promotion_summary_report',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

