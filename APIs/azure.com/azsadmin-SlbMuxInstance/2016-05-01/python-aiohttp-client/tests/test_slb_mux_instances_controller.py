# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.slb_mux_instance import SlbMuxInstance
from openapi_server.models.slb_mux_instance_list import SlbMuxInstanceList


pytestmark = pytest.mark.asyncio

async def test_slb_mux_instances_get(client):
    """Test case for slb_mux_instances_get

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/slbMuxInstances/{slb_mux_instance}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example', slb_mux_instance='slb_mux_instance_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_slb_mux_instances_list(client):
    """Test case for slb_mux_instances_list

    
    """
    params = [('api-version', '2016-05-01'),
                    ('$filter', 'filter_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Fabric.Admin/fabricLocations/{location}/slbMuxInstances'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', location='location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

