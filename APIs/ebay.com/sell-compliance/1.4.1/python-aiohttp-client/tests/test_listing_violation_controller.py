# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.paged_compliance_violation_collection import PagedComplianceViolationCollection
from openapi_server.models.suppress_violation_request import SuppressViolationRequest


pytestmark = pytest.mark.asyncio

async def test_get_listing_violations(client):
    """Test case for get_listing_violations

    
    """
    params = [('compliance_type', 'compliance_type_example'),
                    ('offset', 'offset_example'),
                    ('listing_id', 'listing_id_example'),
                    ('limit', 'limit_example'),
                    ('filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json;charset=UTF-8',
        'x_ebay_c_marketplace_id': 'x_ebay_c_marketplace_id_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/sell/compliance/v1/listing_violation',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_suppress_violation(client):
    """Test case for suppress_violation

    
    """
    body = {"listingId":"listingId","complianceType":"complianceType"}
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/sell/compliance/v1/suppress_listing_violation',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

