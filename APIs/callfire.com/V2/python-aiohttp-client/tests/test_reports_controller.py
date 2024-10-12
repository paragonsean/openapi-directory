# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse
from openapi_server.models.page_delivery_report import PageDeliveryReport


pytestmark = pytest.mark.asyncio

async def test_get_delivery_reports(client):
    """Test case for get_delivery_reports

    Get delivery reports by ad hoc criteria
    """
    params = [('startDate', 'start_date_example'),
                    ('endDate', 'end_date_example'),
                    ('limit', 100),
                    ('offset', 0),
                    ('campaignId', 56),
                    ('fromNumber', 'from_number_example'),
                    ('toNumber', 'to_number_example'),
                    ('deliveryCategory', 'delivery_category_example'),
                    ('deliveryState', 'delivery_state_example'),
                    ('carrier', 'carrier_example'),
                    ('messageText', 'message_text_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v2/reports/delivery',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

