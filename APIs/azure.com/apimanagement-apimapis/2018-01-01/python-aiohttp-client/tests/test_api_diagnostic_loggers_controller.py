# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.api_diagnostic_logger_create_or_update200_response import ApiDiagnosticLoggerCreateOrUpdate200Response
from openapi_server.models.api_diagnostic_logger_list_by_service200_response import ApiDiagnosticLoggerListByService200Response
from openapi_server.models.api_list_by_service_default_response import ApiListByServiceDefaultResponse


pytestmark = pytest.mark.asyncio

async def test_api_diagnostic_logger_check_entity_exists(client):
    """Test case for api_diagnostic_logger_check_entity_exists

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apis/{api_id}/diagnostics/{diagnostic_id}/loggers/{loggerid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', api_id='api_id_example', diagnostic_id='diagnostic_id_example', loggerid='loggerid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_diagnostic_logger_create_or_update(client):
    """Test case for api_diagnostic_logger_create_or_update

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apis/{api_id}/diagnostics/{diagnostic_id}/loggers/{loggerid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', api_id='api_id_example', diagnostic_id='diagnostic_id_example', loggerid='loggerid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_diagnostic_logger_delete(client):
    """Test case for api_diagnostic_logger_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apis/{api_id}/diagnostics/{diagnostic_id}/loggers/{loggerid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', api_id='api_id_example', diagnostic_id='diagnostic_id_example', loggerid='loggerid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_api_diagnostic_logger_list_by_service(client):
    """Test case for api_diagnostic_logger_list_by_service

    
    """
    params = [('api-version', 'api_version_example'),
                    ('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/apis/{api_id}/diagnostics/{diagnostic_id}/loggers'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', api_id='api_id_example', subscription_id='subscription_id_example', diagnostic_id='diagnostic_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

