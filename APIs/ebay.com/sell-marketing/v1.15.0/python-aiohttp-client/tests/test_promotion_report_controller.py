# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.promotions_report_paged_collection import PromotionsReportPagedCollection


pytestmark = pytest.mark.asyncio

async def test_get_promotion_reports(client):
    """Test case for get_promotion_reports

    
    """
    params = [('limit', 'limit_example'),
                    ('marketplace_id', 'marketplace_id_example'),
                    ('offset', 'offset_example'),
                    ('promotion_status', 'promotion_status_example'),
                    ('promotion_type', 'promotion_type_example'),
                    ('q', 'q_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/marketing/v1/promotion_report',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

