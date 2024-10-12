# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_organization_api_requests_overview_response_codes_by_interval200_response_inner import GetOrganizationApiRequestsOverviewResponseCodesByInterval200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_organization_api_requests_overview_response_codes_by_interval_3(client):
    """Test case for get_organization_api_requests_overview_response_codes_by_interval_3

    Tracks organizations' API requests by response code across a given time period
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('interval', 56),
                    ('version', 56),
                    ('operationIds', ['operation_ids_example']),
                    ('sourceIps', ['source_ips_example']),
                    ('adminIds', ['admin_ids_example']),
                    ('userAgent', 'user_agent_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/apiRequests/overview/responseCodes/byInterval'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

