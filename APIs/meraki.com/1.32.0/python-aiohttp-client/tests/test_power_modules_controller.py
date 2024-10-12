# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.get_organization_devices_power_modules_statuses_by_device200_response_inner import GetOrganizationDevicesPowerModulesStatusesByDevice200ResponseInner


pytestmark = pytest.mark.asyncio

async def test_get_organization_devices_power_modules_statuses_by_device_2(client):
    """Test case for get_organization_devices_power_modules_statuses_by_device_2

    List the power status information for devices in an organization
    """
    params = [('perPage', 56),
                    ('startingAfter', 'starting_after_example'),
                    ('endingBefore', 'ending_before_example'),
                    ('networkIds', ['network_ids_example']),
                    ('productTypes', ['product_types_example']),
                    ('serials', ['serials_example']),
                    ('tags', ['tags_example']),
                    ('tagsFilterType', 'tags_filter_type_example')]
    headers = { 
        'Accept': 'application/json',
        'meraki_api_key': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/organizations/{organization_id}/devices/powerModules/statuses/byDevice'.format(organization_id='organization_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

