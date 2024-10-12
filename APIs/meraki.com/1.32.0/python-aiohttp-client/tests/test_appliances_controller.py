# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_organization_summary_top_appliances_by_utilization200_response_inner import GetOrganizationSummaryTopAppliancesByUtilization200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_organization_summary_top_appliances_by_utilization_3(client):
    """Test case for get_organization_summary_top_appliances_by_utilization_3

    Return the top 10 appliances sorted by utilization over given time range.
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4)]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/summary/top/appliances/byUtilization'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

