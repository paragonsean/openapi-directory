# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.async_operation_status import AsyncOperationStatus
from openapi_server.models.paginated_web_services_list import PaginatedWebServicesList
from openapi_server.models.patched_web_service import PatchedWebService
from openapi_server.models.web_service import WebService
from openapi_server.models.web_service_keys import WebServiceKeys


pytestmark = pytest.mark.asyncio

async def test_web_services_create_or_update(client):
    """Test case for web_services_create_or_update

    
    """
    create_or_update_payload = {"properties":{"exposeSampleData":True,"keys":{"secondary":"secondary","primary":"primary"},"description":"description","readOnly":True,"machineLearningWorkspace":{"id":"id"},"provisioningState":"Unknown","storageAccount":{"name":"name","key":"key"},"title":"title","createdOn":"2000-01-23T04:56:07.000+00:00","packageType":"Graph","payloadsLocation":{"credentials":"credentials","uri":"uri"},"output":{"description":"description","title":"title","type":"object","properties":{"key":{"format":"format","description":"description","title":"title","type":"object","properties":{"key":{"format":"Byte","type":"Boolean","x-ms-isordered":True,"enum":["{}","{}"],"x-ms-isnullable":True}}}}},"input":{"description":"description","title":"title","type":"object","properties":{"key":{"format":"format","description":"description","title":"title","type":"object","properties":{"key":{"format":"Byte","type":"Boolean","x-ms-isordered":True,"enum":["{}","{}"],"x-ms-isnullable":True}}}}},"diagnostics":{"level":"None","expiry":"2000-01-23T04:56:07.000+00:00"},"modifiedOn":"2000-01-23T04:56:07.000+00:00","assets":{"key":{"locationInfo":{"credentials":"credentials","uri":"uri"},"metadata":{"key":"metadata"},"outputPorts":{"key":{"type":"Dataset"}},"name":"name","inputPorts":{"key":{"type":"Dataset"}},"id":"id","type":"Module","parameters":[{"parameterType":"parameterType","modeValuesInfo":{"key":{"interfaceString":"interfaceString","parameters":[null,null]}},"name":"name"},{"parameterType":"parameterType","modeValuesInfo":{"key":{"interfaceString":"interfaceString","parameters":[null,null]}},"name":"name"}]}},"commitmentPlan":{"id":"id"},"payloadsInBlobStorage":True,"realtimeConfiguration":{"maxConcurrentCalls":19},"swaggerLocation":"swaggerLocation","exampleRequest":{"globalParameters":{"key":"{}"},"inputs":{"key":[["{}","{}"],["{}","{}"]]}},"parameters":{"key":{"certificateThumbprint":"certificateThumbprint","value":"{}"}}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearning/webServices/{web_service_name}'.format(resource_group_name='resource_group_name_example', web_service_name='web_service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=create_or_update_payload,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_services_create_regional_properties(client):
    """Test case for web_services_create_regional_properties

    
    """
    params = [('region', 'region_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearning/webServices/{web_service_name}/CreateRegionalBlob'.format(resource_group_name='resource_group_name_example', web_service_name='web_service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_services_get(client):
    """Test case for web_services_get

    
    """
    params = [('region', 'region_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearning/webServices/{web_service_name}'.format(resource_group_name='resource_group_name_example', web_service_name='web_service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_services_list_by_resource_group(client):
    """Test case for web_services_list_by_resource_group

    
    """
    params = [('$skiptoken', 'skiptoken_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearning/webServices'.format(resource_group_name='resource_group_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_services_list_by_subscription_id(client):
    """Test case for web_services_list_by_subscription_id

    
    """
    params = [('$skiptoken', 'skiptoken_example'),
                    ('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.MachineLearning/webServices'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_services_list_keys(client):
    """Test case for web_services_list_keys

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearning/webServices/{web_service_name}/listKeys'.format(resource_group_name='resource_group_name_example', web_service_name='web_service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_services_patch(client):
    """Test case for web_services_patch

    
    """
    patch_payload = {"properties":{"exposeSampleData":True,"keys":{"secondary":"secondary","primary":"primary"},"description":"description","readOnly":True,"machineLearningWorkspace":{"id":"id"},"provisioningState":"Unknown","storageAccount":{"name":"name","key":"key"},"title":"title","createdOn":"2000-01-23T04:56:07.000+00:00","packageType":"Graph","payloadsLocation":{"credentials":"credentials","uri":"uri"},"output":{"description":"description","title":"title","type":"object","properties":{"key":{"format":"format","description":"description","title":"title","type":"object","properties":{"key":{"format":"Byte","type":"Boolean","x-ms-isordered":True,"enum":["{}","{}"],"x-ms-isnullable":True}}}}},"input":{"description":"description","title":"title","type":"object","properties":{"key":{"format":"format","description":"description","title":"title","type":"object","properties":{"key":{"format":"Byte","type":"Boolean","x-ms-isordered":True,"enum":["{}","{}"],"x-ms-isnullable":True}}}}},"diagnostics":{"level":"None","expiry":"2000-01-23T04:56:07.000+00:00"},"modifiedOn":"2000-01-23T04:56:07.000+00:00","assets":{"key":{"locationInfo":{"credentials":"credentials","uri":"uri"},"metadata":{"key":"metadata"},"outputPorts":{"key":{"type":"Dataset"}},"name":"name","inputPorts":{"key":{"type":"Dataset"}},"id":"id","type":"Module","parameters":[{"parameterType":"parameterType","modeValuesInfo":{"key":{"interfaceString":"interfaceString","parameters":[null,null]}},"name":"name"},{"parameterType":"parameterType","modeValuesInfo":{"key":{"interfaceString":"interfaceString","parameters":[null,null]}},"name":"name"}]}},"commitmentPlan":{"id":"id"},"payloadsInBlobStorage":True,"realtimeConfiguration":{"maxConcurrentCalls":19},"swaggerLocation":"swaggerLocation","exampleRequest":{"globalParameters":{"key":"{}"},"inputs":{"key":[["{}","{}"],["{}","{}"]]}},"parameters":{"key":{"certificateThumbprint":"certificateThumbprint","value":"{}"}}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearning/webServices/{web_service_name}'.format(resource_group_name='resource_group_name_example', web_service_name='web_service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        json=patch_payload,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_web_services_remove(client):
    """Test case for web_services_remove

    
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.MachineLearning/webServices/{web_service_name}'.format(resource_group_name='resource_group_name_example', web_service_name='web_service_name_example', subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

