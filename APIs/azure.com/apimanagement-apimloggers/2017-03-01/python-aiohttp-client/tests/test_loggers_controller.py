# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.logger_collection import LoggerCollection
from openapi_server.models.logger_contract import LoggerContract
from openapi_server.models.logger_list_by_service_default_response import LoggerListByServiceDefaultResponse
from openapi_server.models.logger_update_contract import LoggerUpdateContract


pytestmark = pytest.mark.asyncio

async def test_logger_create_or_update(client):
    """Test case for logger_create_or_update

    
    """
    parameters = {"properties":{"loggerType":"azureEventHub","credentials":{"connectionString":"Endpoint=sb://contoso-ns.servicebus.windows.net/;SharedAccessKeyName=Sender;SharedAccessKey=...","name":"apim"},"isBuffered":True,"sampling":{"properties":{"initialPercentage":6.027456183070403,"samplingType":"fixed","maxPercentage":1.4658129805029452,"percentageDecreaseTimeout":"percentageDecreaseTimeout","movingAverageRatio":2.3021358869347655,"minPercentage":5.637376656633329,"percentage":7.061401241503109,"evaluationInterval":"evaluationInterval","percentageIncreaseTimeout":"percentageIncreaseTimeout","maxTelemetryItemsPerSecond":5}},"description":"description"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/loggers/{loggerid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', loggerid='loggerid_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logger_delete(client):
    """Test case for logger_delete

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/loggers/{loggerid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', loggerid='loggerid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logger_get(client):
    """Test case for logger_get

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/loggers/{loggerid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', loggerid='loggerid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logger_get_entity_tag(client):
    """Test case for logger_get_entity_tag

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='HEAD',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/loggers/{loggerid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', loggerid='loggerid_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logger_list_by_service(client):
    """Test case for logger_list_by_service

    
    """
    params = [('$filter', 'filter_example'),
                    ('$top', 56),
                    ('$skip', 56),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/loggers'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_logger_update(client):
    """Test case for logger_update

    
    """
    parameters = {"properties":{"loggerType":"azureEventHub","credentials":{"key":"credentials"},"isBuffered":True,"description":"description"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'if_match': 'if_match_example',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ApiManagement/service/{service_name}/loggers/{loggerid}'.format(resource_group_name='resource_group_name_example', service_name='service_name_example', loggerid='loggerid_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=parameters,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

