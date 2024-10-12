# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.dns_name_availability_result import DnsNameAvailabilityResult


pytestmark = pytest.mark.asyncio

async def test_check_dns_name_availability(client):
    """Test case for check_dns_name_availability

    
    """
    params = [('domainNameLabel', 'domain_name_label_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Network/locations/{location}/CheckDnsNameAvailability'.format(location='location_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

