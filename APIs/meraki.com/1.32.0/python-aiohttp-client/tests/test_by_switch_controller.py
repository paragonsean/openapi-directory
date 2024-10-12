# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_organization_switch_ports_by_switch200_response_inner import GetOrganizationSwitchPortsBySwitch200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_organization_switch_ports_by_switch_2(client):
    """Test case for get_organization_switch_ports_by_switch_2

    List the switchports in an organization by switch
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkIds', ['network_ids_example']),
                    ('portProfileIds', ['port_profile_ids_example']),
                    ('name', 'name_example'),
                    ('mac', 'mac_example'),
                    ('macs', ['macs_example']),
                    ('serial', 'serial_example'),
                    ('serials', ['serials_example']),
                    ('configurationUpdatedAfter', 'configuration_updated_after_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/switch/ports/bySwitch'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

