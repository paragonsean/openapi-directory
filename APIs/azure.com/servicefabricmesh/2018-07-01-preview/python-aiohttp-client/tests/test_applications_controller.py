# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.application_resource_description import ApplicationResourceDescription
from openapi_server.models.application_resource_description_list import ApplicationResourceDescriptionList
from openapi_server.models.error_model import ErrorModel


pytestmark = pytest.mark.asyncio

async def test_application_create(client):
    """Test case for application_create

    Creates or updates an application resource.
    """
    application_resource_description = {"properties":{"unhealthyEvaluation":"unhealthyEvaluation","diagnostics":{"sinks":[{"kind":"Invalid","name":"name","description":"description"},{"kind":"Invalid","name":"name","description":"description"}],"defaultSinkRefs":["defaultSinkRefs","defaultSinkRefs"],"enabled":True},"debugParams":"debugParams","healthState":"Invalid","description":"description","statusDetails":"statusDetails","provisioningState":"provisioningState","services":[{"properties":{"codePackages":[{"image":"image","settings":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"endpoints":[{"port":0,"name":"name"},{"port":0,"name":"name"}],"imageRegistryCredential":{"server":"server","password":"password","username":"username"},"resources":{"requests":{"cpu":2.3021358869347655,"memoryInGB":7.061401241503109},"limits":{"cpu":5.962133916683182,"memoryInGB":5.637376656633329}},"volumeRefs":[{"name":"name","readOnly":True,"destinationPath":"destinationPath"},{"name":"name","readOnly":True,"destinationPath":"destinationPath"}],"labels":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"diagnostics":{"sinkRefs":["sinkRefs","sinkRefs"],"enabled":True},"instanceView":{"restartCount":1,"currentState":{"detailStatus":"detailStatus","finishTime":"2000-01-23T04:56:07.000+00:00","exitCode":"exitCode","startTime":"2000-01-23T04:56:07.000+00:00","state":"state"},"events":[{"firstTimestamp":"firstTimestamp","lastTimestamp":"lastTimestamp","count":6,"name":"name","message":"message","type":"type"},{"firstTimestamp":"firstTimestamp","lastTimestamp":"lastTimestamp","count":6,"name":"name","message":"message","type":"type"}],"previousState":{"detailStatus":"detailStatus","finishTime":"2000-01-23T04:56:07.000+00:00","exitCode":"exitCode","startTime":"2000-01-23T04:56:07.000+00:00","state":"state"}},"entrypoint":"entrypoint","environmentVariables":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"name":"name","commands":["commands","commands"]},{"image":"image","settings":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"endpoints":[{"port":0,"name":"name"},{"port":0,"name":"name"}],"imageRegistryCredential":{"server":"server","password":"password","username":"username"},"resources":{"requests":{"cpu":2.3021358869347655,"memoryInGB":7.061401241503109},"limits":{"cpu":5.962133916683182,"memoryInGB":5.637376656633329}},"volumeRefs":[{"name":"name","readOnly":True,"destinationPath":"destinationPath"},{"name":"name","readOnly":True,"destinationPath":"destinationPath"}],"labels":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"diagnostics":{"sinkRefs":["sinkRefs","sinkRefs"],"enabled":True},"instanceView":{"restartCount":1,"currentState":{"detailStatus":"detailStatus","finishTime":"2000-01-23T04:56:07.000+00:00","exitCode":"exitCode","startTime":"2000-01-23T04:56:07.000+00:00","state":"state"},"events":[{"firstTimestamp":"firstTimestamp","lastTimestamp":"lastTimestamp","count":6,"name":"name","message":"message","type":"type"},{"firstTimestamp":"firstTimestamp","lastTimestamp":"lastTimestamp","count":6,"name":"name","message":"message","type":"type"}],"previousState":{"detailStatus":"detailStatus","finishTime":"2000-01-23T04:56:07.000+00:00","exitCode":"exitCode","startTime":"2000-01-23T04:56:07.000+00:00","state":"state"}},"entrypoint":"entrypoint","environmentVariables":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"name":"name","commands":["commands","commands"]}],"diagnostics":{"sinkRefs":["sinkRefs","sinkRefs"],"enabled":True},"replicaCount":9,"osType":"Linux","description":"description","networkRefs":[{"name":"name"},{"name":"name"}],"status":"Unknown"}},{"properties":{"codePackages":[{"image":"image","settings":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"endpoints":[{"port":0,"name":"name"},{"port":0,"name":"name"}],"imageRegistryCredential":{"server":"server","password":"password","username":"username"},"resources":{"requests":{"cpu":2.3021358869347655,"memoryInGB":7.061401241503109},"limits":{"cpu":5.962133916683182,"memoryInGB":5.637376656633329}},"volumeRefs":[{"name":"name","readOnly":True,"destinationPath":"destinationPath"},{"name":"name","readOnly":True,"destinationPath":"destinationPath"}],"labels":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"diagnostics":{"sinkRefs":["sinkRefs","sinkRefs"],"enabled":True},"instanceView":{"restartCount":1,"currentState":{"detailStatus":"detailStatus","finishTime":"2000-01-23T04:56:07.000+00:00","exitCode":"exitCode","startTime":"2000-01-23T04:56:07.000+00:00","state":"state"},"events":[{"firstTimestamp":"firstTimestamp","lastTimestamp":"lastTimestamp","count":6,"name":"name","message":"message","type":"type"},{"firstTimestamp":"firstTimestamp","lastTimestamp":"lastTimestamp","count":6,"name":"name","message":"message","type":"type"}],"previousState":{"detailStatus":"detailStatus","finishTime":"2000-01-23T04:56:07.000+00:00","exitCode":"exitCode","startTime":"2000-01-23T04:56:07.000+00:00","state":"state"}},"entrypoint":"entrypoint","environmentVariables":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"name":"name","commands":["commands","commands"]},{"image":"image","settings":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"endpoints":[{"port":0,"name":"name"},{"port":0,"name":"name"}],"imageRegistryCredential":{"server":"server","password":"password","username":"username"},"resources":{"requests":{"cpu":2.3021358869347655,"memoryInGB":7.061401241503109},"limits":{"cpu":5.962133916683182,"memoryInGB":5.637376656633329}},"volumeRefs":[{"name":"name","readOnly":True,"destinationPath":"destinationPath"},{"name":"name","readOnly":True,"destinationPath":"destinationPath"}],"labels":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"diagnostics":{"sinkRefs":["sinkRefs","sinkRefs"],"enabled":True},"instanceView":{"restartCount":1,"currentState":{"detailStatus":"detailStatus","finishTime":"2000-01-23T04:56:07.000+00:00","exitCode":"exitCode","startTime":"2000-01-23T04:56:07.000+00:00","state":"state"},"events":[{"firstTimestamp":"firstTimestamp","lastTimestamp":"lastTimestamp","count":6,"name":"name","message":"message","type":"type"},{"firstTimestamp":"firstTimestamp","lastTimestamp":"lastTimestamp","count":6,"name":"name","message":"message","type":"type"}],"previousState":{"detailStatus":"detailStatus","finishTime":"2000-01-23T04:56:07.000+00:00","exitCode":"exitCode","startTime":"2000-01-23T04:56:07.000+00:00","state":"state"}},"entrypoint":"entrypoint","environmentVariables":[{"name":"name","value":"value"},{"name":"name","value":"value"}],"name":"name","commands":["commands","commands"]}],"diagnostics":{"sinkRefs":["sinkRefs","sinkRefs"],"enabled":True},"replicaCount":9,"osType":"Linux","description":"description","networkRefs":[{"name":"name"},{"name":"name"}],"status":"Unknown"}}],"serviceNames":["serviceNames","serviceNames"],"status":"Invalid"}}
    params = [('api-version', 2018-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/applications/{application_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', application_name='application_name_example'),
        headers=headers,
        json=application_resource_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_delete(client):
    """Test case for application_delete

    Deletes the application resource.
    """
    params = [('api-version', 2018-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='DELETE',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/applications/{application_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_get(client):
    """Test case for application_get

    Gets the application resource.
    """
    params = [('api-version', 2018-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/applications/{application_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', application_name='application_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_list_by_resource_group(client):
    """Test case for application_list_by_resource_group

    Gets all the application resources in a given resource group.
    """
    params = [('api-version', 2018-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.ServiceFabricMesh/applications'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_application_list_by_subscription(client):
    """Test case for application_list_by_subscription

    Gets all the application resources in a given subscription.
    """
    params = [('api-version', 2018-07-01-preview)]
    headers = { 
        'Accept': 'application/json',
        'Authorization': 'Bearer special-key',
    }
    response = await client.request(
        method='GET',
        path='/subscriptions/{subscription_id}/providers/Microsoft.ServiceFabricMesh/applications'.format(subscription_id='subscription_id_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

