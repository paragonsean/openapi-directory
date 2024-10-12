# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_response import ErrorResponse


pytestmark = pytest.mark.asyncio

async def test_sales_reports_get_collection(client):
    """Test case for sales_reports_get_collection

    
    """
    params = [('filter[frequency]', ['filter_frequency_example']),
                    ('filter[reportDate]', ['filter_report_date_example']),
                    ('filter[reportSubType]', ['filter_report_sub_type_example']),
                    ('filter[reportType]', ['filter_report_type_example']),
                    ('filter[vendorNumber]', ['filter_vendor_number_example']),
                    ('filter[version]', ['filter_version_example'])]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/v1/salesReports',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

