# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.export_configurations_list200_response import ExportConfigurationsList200Response
from openapi_server.models.export_configurations_list200_response_values_inner import ExportConfigurationsList200ResponseValuesInner
from openapi_server.models.export_configurations_list200_response_values_inner_export_configuration import ExportConfigurationsList200ResponseValuesInnerExportConfiguration
from openapi_server.models.organizations_list_administered_default_response import OrganizationsListAdministeredDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_export_configurations_create(client):
    """Test case for export_configurations_create

    
    """
    body = openapi_server.ExportConfigurationsList200ResponseValuesInnerExportConfiguration()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/export_configurations'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_configurations_delete(client):
    """Test case for export_configurations_delete

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/v0.1/apps/{owner_name}/{app_name}/export_configurations/{export_configuration_id}'.format(export_configuration_id='export_configuration_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_configurations_disable(client):
    """Test case for export_configurations_disable

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/export_configurations/{export_configuration_id}/disable'.format(export_configuration_id='export_configuration_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_configurations_enable(client):
    """Test case for export_configurations_enable

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='POST',
        path='/v0.1/apps/{owner_name}/{app_name}/export_configurations/{export_configuration_id}/enable'.format(export_configuration_id='export_configuration_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_configurations_get(client):
    """Test case for export_configurations_get

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/export_configurations/{export_configuration_id}'.format(export_configuration_id='export_configuration_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_configurations_list(client):
    """Test case for export_configurations_list

    
    """
    headers = { 
        'Accept': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='GET',
        path='/v0.1/apps/{owner_name}/{app_name}/export_configurations'.format(owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_export_configurations_partial_update(client):
    """Test case for export_configurations_partial_update

    
    """
    body = openapi_server.ExportConfigurationsList200ResponseValuesInnerExportConfiguration()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'APIToken': 'special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/v0.1/apps/{owner_name}/{app_name}/export_configurations/{export_configuration_id}'.format(export_configuration_id='export_configuration_id_example', owner_name='owner_name_example', app_name='app_name_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

