# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error import Error
from openapi_server.models.plugin import Plugin
from openapi_server.models.plugin_params import PluginParams
from openapi_server.models.plugin_run import PluginRun
from openapi_server.models.plugin_run_data import PluginRunData


pytestmark = pytest.mark.asyncio

async def test_create_plugin_run(client):
    """Test case for create_plugin_run

    
    """
    plugin_run = openapi_server.PluginRunData()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/api/v1/deploys/{deploy_id}/plugin_runs'.format(deploy_id='deploy_id_example'),
        headers=headers,
        json=plugin_run,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_get_latest_plugin_runs(client):
    """Test case for get_latest_plugin_runs

    
    """
    params = [('packages', ['packages_example']),
                    ('state', 'state_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/api/v1/sites/{site_id}/plugin_runs/latest'.format(site_id='site_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_plugin(client):
    """Test case for update_plugin

    
    """
    plugin_params = openapi_server.PluginParams()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/api/v1/sites/{site_id}/plugins/{package}'.format(site_id='site_id_example', package='package_example'),
        headers=headers,
        json=plugin_params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

