# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_organization_summary_top_devices_models_by_usage200_response_inner import GetOrganizationSummaryTopDevicesModelsByUsage200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_organization_summary_top_devices_models_by_usage_4(client):
    """Test case for get_organization_summary_top_devices_models_by_usage_4

    Return metrics for organization's top 10 device models sorted by data usage over given time range
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
        path='/api/v1/organizations/{organization_id}/summary/top/devices/models/byUsage'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

