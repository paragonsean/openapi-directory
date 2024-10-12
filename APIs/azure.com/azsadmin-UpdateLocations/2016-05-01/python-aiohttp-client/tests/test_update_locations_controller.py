# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_location import UpdateLocation
from openapi_server.models.update_location_list import UpdateLocationList


pytestmark = pytest.mark.asyncio

async def test_update_locations_get(client):
    """Test case for update_locations_get

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Update.Admin/updateLocations/{update_location}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', update_location='update_location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_locations_list(client):
    """Test case for update_locations_list

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Update.Admin/updateLocations'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

