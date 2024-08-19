# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.cloud_error import CloudError
from openapi_server.models.heat_map_model import HeatMapModel


pytestmark = pytest.mark.asyncio

async def test_heat_map_get(client):
    """Test case for heat_map_get

    
    """
    params = [('topLeft', [3.4]),
                    ('botRight', [3.4]),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Network/trafficmanagerprofiles/{profile_name}/heatMaps/{heat_map_type}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', profile_name='profile_name_example', heat_map_type='heat_map_type_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

