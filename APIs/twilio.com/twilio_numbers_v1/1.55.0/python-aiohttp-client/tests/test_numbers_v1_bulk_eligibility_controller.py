# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.numbers_v1_bulk_eligibility import NumbersV1BulkEligibility


pytestmark = pytest.mark.asyncio

async def test_fetch_bulk_eligibility(client):
    """Test case for fetch_bulk_eligibility

    
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/v1/HostedNumber/Eligibility/Bulk/{request_id}'.format(request_id='request_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

