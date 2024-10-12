# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.compliance_summary import ComplianceSummary


pytestmark = pytest.mark.asyncio

async def test_get_listing_violations_summary(client):
    """Test case for get_listing_violations_summary

    
    """
    params = [('compliance_type', 'compliance_type_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'x_ebay_c_marketplace_id': 'x_ebay_c_marketplace_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/compliance/v1/listing_violation_summary',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

