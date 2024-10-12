# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.update_run import UpdateRun
from openapi_server.models.update_run_list import UpdateRunList


pytestmark = pytest.mark.asyncio

async def test_update_runs_get(client):
    """Test case for update_runs_get

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Update.Admin/updateLocations/{update_location}/updates/{update_name}/updateRuns/{run_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', update_location='update_location_example', update_name='update_name_example', run_name='run_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_runs_get_top_level(client):
    """Test case for update_runs_get_top_level

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Update.Admin/updateLocations/{update_location}/updateRuns/{run_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', update_location='update_location_example', run_name='run_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_runs_list(client):
    """Test case for update_runs_list

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Update.Admin/updateLocations/{update_location}/updates/{update_name}/updateRuns'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', update_location='update_location_example', update_name='update_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_runs_list_top_level(client):
    """Test case for update_runs_list_top_level

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Update.Admin/updateLocations/{update_location}/updateRuns'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', update_location='update_location_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_runs_rerun(client):
    """Test case for update_runs_rerun

    
    """
    params = [('api-version', '2016-05-01')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourcegroups/{resource_group_name}/providers/Microsoft.Update.Admin/updateLocations/{update_location}/updates/{update_name}/updateRuns/{run_name}/rerun'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', update_location='update_location_example', update_name='update_name_example', run_name='run_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

