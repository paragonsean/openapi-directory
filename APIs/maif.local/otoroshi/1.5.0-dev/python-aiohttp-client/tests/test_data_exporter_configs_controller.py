# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.create_bulk_data_exporter_configs200_response_inner import CreateBulkDataExporterConfigs200ResponseInner
from openapi_server.models.data_exporter_config import DataExporterConfig
from openapi_server.models.deletebulk_data_exporter_config200_response_inner import DeletebulkDataExporterConfig200ResponseInner
from openapi_server.models.deleted import Deleted
from openapi_server.models.patch_inner import PatchInner
from openapi_server.models.update_bulk_data_exporter_config200_response_inner import UpdateBulkDataExporterConfig200ResponseInner


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/ndjson not supported by Connexion")
async def test_create_bulk_data_exporter_configs(client):
    """Test case for create_bulk_data_exporter_configs

    Create a new data exporter configs
    """
    body = openapi_server.DataExporterConfig()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ndjson',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/data-exporter-configs/_bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_create_data_exporter_config(client):
    """Test case for create_data_exporter_config

    Create a new data exporter config
    """
    body = {"metadata":{"key":"value"},"typ":"kafka","enabled":"a string value","groupDuration":123,"jsonWorkers":123123,"name":"a string value","groupSize":123123,"location":{"teams":[{"key":"value"},{"key":"value"}],"tenant":"a string value"},"id":"a string value","projection":{"key":"value"},"config":{"clusterUri":"a string value","headers":{"key":"value"},"password":"a string value","index":"a string value","type":"a string value","user":"a string value"},"filtering":{"include":[{"key":"value"},{"key":"value"}],"exclude":[{"key":"value"},{"key":"value"}]},"sendWorkers":123123,"bufferSize":123123,"desc":"a string value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='POST',
        path='/api/data-exporter-configs',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_data_exporter_template(client):
    """Test case for data_exporter_template

    Get all data exporter configs
    """
    params = [('type', 'type_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/data-exporter-configs/_template',
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_delete_data_exporter_config(client):
    """Test case for delete_data_exporter_config

    Delete a data exporter config
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/data-exporter-configs/{data_exporter_config_id}'.format(data_exporter_config_id='data_exporter_config_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/ndjson not supported by Connexion")
async def test_deletebulk_data_exporter_config(client):
    """Test case for deletebulk_data_exporter_config

    Delete a data exporter config
    """
    body = [openapi_server.PatchInner()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ndjson',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='DELETE',
        path='/api/data-exporter-configs/_bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_all_data_exporters(client):
    """Test case for find_all_data_exporters

    Get all data exporter configs
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/data-exporter-configs',
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_find_data_exporter_config_by_id(client):
    """Test case for find_data_exporter_config_by_id

    Get a data exporter config
    """
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='GET',
        path='/api/data-exporter-configs/{data_exporter_config_id}'.format(data_exporter_config_id='data_exporter_config_id_example'),
        headers=headers,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/ndjson not supported by Connexion")
async def test_patch_bulk_data_exporter_config(client):
    """Test case for patch_bulk_data_exporter_config

    Update a data exporter configs with a diff
    """
    body = [openapi_server.PatchInner()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ndjson',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PATCH',
        path='/api/data-exporter-configs/_bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_patch_data_exporter_config(client):
    """Test case for patch_data_exporter_config

    Update a data exporter config with a diff
    """
    body = [openapi_server.PatchInner()]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PATCH',
        path='/api/data-exporter-configs/{data_exporter_config_id}'.format(data_exporter_config_id='data_exporter_config_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

@pytest.mark.skip("application/ndjson not supported by Connexion")
async def test_update_bulk_data_exporter_config(client):
    """Test case for update_bulk_data_exporter_config

    Update a data exporter configs
    """
    body = openapi_server.DataExporterConfig()
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/ndjson',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/data-exporter-configs/_bulk',
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_update_data_exporter_config(client):
    """Test case for update_data_exporter_config

    Update a data exporter config
    """
    body = {"metadata":{"key":"value"},"typ":"kafka","enabled":"a string value","groupDuration":123,"jsonWorkers":123123,"name":"a string value","groupSize":123123,"location":{"teams":[{"key":"value"},{"key":"value"}],"tenant":"a string value"},"id":"a string value","projection":{"key":"value"},"config":{"clusterUri":"a string value","headers":{"key":"value"},"password":"a string value","index":"a string value","type":"a string value","user":"a string value"},"filtering":{"include":[{"key":"value"},{"key":"value"}],"exclude":[{"key":"value"},{"key":"value"}]},"sendWorkers":123123,"bufferSize":123123,"desc":"a string value"}
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'BasicZm9vOmJhcg==',
    }
    response = await client.request(
        method='PUT',
        path='/api/data-exporter-configs/{data_exporter_config_id}'.format(data_exporter_config_id='data_exporter_config_id_example'),
        headers=headers,
        json=body,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

