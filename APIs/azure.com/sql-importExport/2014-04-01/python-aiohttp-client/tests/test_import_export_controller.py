# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.export_request import ExportRequest
from openapi_server.models.import_export_response import ImportExportResponse
from openapi_server.models.import_extension_request import ImportExtensionRequest
from openapi_server.models.import_request import ImportRequest


pytestmark = pytest.mark.asyncio

async def test_databases_create_import_operation(client):
    """Test case for databases_create_import_operation

    
    """
    parameters = {"name":"name","type":"type","properties":{"operationMode":"Import"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/extensions/{extension_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example', extension_name='extension_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_export(client):
    """Test case for databases_export

    
    """
    parameters = {"administratorLogin":"administratorLogin","storageKeyType":"StorageAccessKey","administratorLoginPassword":"administratorLoginPassword","storageUri":"storageUri","authenticationType":"SQL","storageKey":"storageKey"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/databases/{database_name}/export'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example', database_name='database_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_databases_import(client):
    """Test case for databases_import

    
    """
    parameters = {"databaseName":"databaseName","maxSizeBytes":"maxSizeBytes","serviceObjectiveName":"System","edition":"Web"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Sql/servers/{server_name}/import'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', server_name='server_name_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

