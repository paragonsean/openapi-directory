# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.connector_mapping_list_result import ConnectorMappingListResult
from openapi_server.models.connector_mapping_resource_format import ConnectorMappingResourceFormat


pytestmark = pytest.mark.asyncio

async def test_connector_mappings_create_or_update(client):
    """Test case for connector_mappings_create_or_update

    
    """
    parameters = {"properties":{"dataFormatId":"dataFormatId","connectorType":"None","created":"2000-01-23T04:56:07.000+00:00","displayName":"displayName","entityType":"None","description":"description","entityTypeName":"entityTypeName","nextRunTime":"2000-01-23T04:56:07.000+00:00","mappingProperties":{"folderPath":"folderPath","fileFilter":"fileFilter","hasHeader":True,"completeOperation":{"destinationFolder":"destinationFolder","completionOperationType":"DoNothing"},"format":{"acceptLanguage":"acceptLanguage","quoteEscapeCharacter":"quoteEscapeCharacter","quoteCharacter":"quoteCharacter","arraySeparator":"arraySeparator","formatType":"TextFormat","columnDelimiter":"columnDelimiter"},"availability":{"interval":0,"frequency":"Minute"},"structure":[{"propertyName":"propertyName","isEncrypted":True,"customFormatSpecifier":"customFormatSpecifier","columnName":"columnName"},{"propertyName":"propertyName","isEncrypted":True,"customFormatSpecifier":"customFormatSpecifier","columnName":"columnName"}],"errorManagement":{"errorLimit":6,"errorManagementType":"RejectAndContinue"}},"connectorMappingName":"connectorMappingName","tenantId":"tenantId","connectorName":"connectorName","lastModified":"2000-01-23T04:56:07.000+00:00","runId":"runId","state":"Creating"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/connectors/{connector_name}/mappings/{mapping_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', connector_name='connector_name_example', mapping_name='mapping_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connector_mappings_delete(client):
    """Test case for connector_mappings_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/connectors/{connector_name}/mappings/{mapping_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', connector_name='connector_name_example', mapping_name='mapping_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connector_mappings_get(client):
    """Test case for connector_mappings_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/connectors/{connector_name}/mappings/{mapping_name}'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', connector_name='connector_name_example', mapping_name='mapping_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_connector_mappings_list_by_connector(client):
    """Test case for connector_mappings_list_by_connector

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.CustomerInsights/hubs/{hub_name}/connectors/{connector_name}/mappings'.format(resource_group_name='resource_group_name_example', hub_name='hub_name_example', connector_name='connector_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

