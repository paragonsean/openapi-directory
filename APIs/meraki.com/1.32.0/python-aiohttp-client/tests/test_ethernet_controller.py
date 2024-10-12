# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_organization_wireless_devices_ethernet_statuses200_response_inner import GetOrganizationWirelessDevicesEthernetStatuses200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_organization_wireless_devices_ethernet_statuses_2(client):
    """Test case for get_organization_wireless_devices_ethernet_statuses_2

    Endpoint to see power status for wireless devices
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkIds', ['network_ids_example'])]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/wireless/devices/ethernet/statuses'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

