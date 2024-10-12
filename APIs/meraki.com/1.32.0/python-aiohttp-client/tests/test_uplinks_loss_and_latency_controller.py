# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_organization_devices_uplinks_loss_and_latency200_response_inner import GetOrganizationDevicesUplinksLossAndLatency200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_organization_devices_uplinks_loss_and_latency_3(client):
    """Test case for get_organization_devices_uplinks_loss_and_latency_3

    Return the uplink loss and latency for every MX in the organization from at latest 2 minutes ago
    """
    params = [('t0', 't0_example'),
                    ('t1', 't1_example'),
                    ('timespan', 3.4),
                    ('uplink', 'uplink_example'),
                    ('ip', 'ip_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/devices/uplinksLossAndLatency'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

