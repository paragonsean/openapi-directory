# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.custom_api_definition import CustomApiDefinition
from openapi_server.models.custom_api_definition_collection import CustomApiDefinitionCollection
from openapi_server.models.custom_api_reference import CustomApiReference
from openapi_server.models.wsdl_definition import WsdlDefinition
from openapi_server.models.wsdl_service_collection import WsdlServiceCollection


pytestmark = pytest.mark.asyncio

async def test_custom_apis_create_or_update(client):
    """Test case for custom_apis_create_or_update

    Replaces an existing custom API
    """
    custom_api = {"properties":{"runtimeUrls":["runtimeUrls","runtimeUrls"],"brandColor":"brandColor","capabilities":["capabilities","capabilities"],"connectionParameters":{"key":{"oAuthSettings":{"clientId":"clientId","redirectUrl":"redirectUrl","clientSecret":"clientSecret","customParameters":{"key":{"options":"{}","value":"value","uiDefinition":"{}"}},"scopes":["scopes","scopes"],"identityProvider":"identityProvider","properties":"{}"},"type":"string"}},"apiDefinitions":{"originalSwaggerUrl":"originalSwaggerUrl","modifiedSwaggerUrl":"modifiedSwaggerUrl"},"displayName":"displayName","backendService":{"serviceUrl":"serviceUrl"},"wsdlDefinition":{"service":{"endpointQualifiedNames":["endpointQualifiedNames","endpointQualifiedNames"],"qualifiedName":"qualifiedName"},"importMethod":"NotSpecified","content":"content","url":"url"},"description":"description","apiType":"NotSpecified","iconUri":"iconUri","swagger":"{}"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/customApis/{api_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', api_name='api_name_example'),
        headers=headers,
        json=custom_api,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_apis_delete(client):
    """Test case for custom_apis_delete

    Delete a custom API
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/customApis/{api_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', api_name='api_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_apis_extract_api_definition_from_wsdl(client):
    """Test case for custom_apis_extract_api_definition_from_wsdl

    Returns API definition from WSDL
    """
    wsdl_definition = {"service":{"endpointQualifiedNames":["endpointQualifiedNames","endpointQualifiedNames"],"qualifiedName":"qualifiedName"},"importMethod":"NotSpecified","content":"content","url":"url"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/locations/{location}/extractApiDefinitionFromWsdl'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        json=wsdl_definition,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_apis_get(client):
    """Test case for custom_apis_get

    Get a custom API
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/customApis/{api_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', api_name='api_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_apis_list(client):
    """Test case for custom_apis_list

    List of custom APIs
    """
    params = [('api-version', 'api_version_example'),
                    ('$top', 56),
                    ('skiptoken', 'skiptoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/customApis'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_apis_list_by_resource_group(client):
    """Test case for custom_apis_list_by_resource_group

    List of custom APIs
    """
    params = [('api-version', 'api_version_example'),
                    ('$top', 56),
                    ('skiptoken', 'skiptoken_example')]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/customApis'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_apis_list_wsdl_interfaces(client):
    """Test case for custom_apis_list_wsdl_interfaces

    Lists WSDL interfaces
    """
    wsdl_definition = {"service":{"endpointQualifiedNames":["endpointQualifiedNames","endpointQualifiedNames"],"qualifiedName":"qualifiedName"},"importMethod":"NotSpecified","content":"content","url":"url"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/providers/Microsoft.Web/locations/{location}/listWsdlInterfaces'.format(subscription_id='subscription_id_example', location='location_example'),
        headers=headers,
        json=wsdl_definition,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_apis_move(client):
    """Test case for custom_apis_move

    Moves the custom API
    """
    custom_api_reference = {"name":"name"}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='POST',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/customApis/{api_name}/move'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', api_name='api_name_example'),
        headers=headers,
        json=custom_api_reference,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_custom_apis_update(client):
    """Test case for custom_apis_update

    Update an existing custom API
    """
    custom_api = {"properties":{"runtimeUrls":["runtimeUrls","runtimeUrls"],"brandColor":"brandColor","capabilities":["capabilities","capabilities"],"connectionParameters":{"key":{"oAuthSettings":{"clientId":"clientId","redirectUrl":"redirectUrl","clientSecret":"clientSecret","customParameters":{"key":{"options":"{}","value":"value","uiDefinition":"{}"}},"scopes":["scopes","scopes"],"identityProvider":"identityProvider","properties":"{}"},"type":"string"}},"apiDefinitions":{"originalSwaggerUrl":"originalSwaggerUrl","modifiedSwaggerUrl":"modifiedSwaggerUrl"},"displayName":"displayName","backendService":{"serviceUrl":"serviceUrl"},"wsdlDefinition":{"service":{"endpointQualifiedNames":["endpointQualifiedNames","endpointQualifiedNames"],"qualifiedName":"qualifiedName"},"importMethod":"NotSpecified","content":"content","url":"url"},"description":"description","apiType":"NotSpecified","iconUri":"iconUri","swagger":"{}"}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PATCH',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Web/customApis/{api_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', api_name='api_name_example'),
        headers=headers,
        json=custom_api,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

