# coding: utf-8

import pytest
import json
from aiohttp import web

from openapi_server.models.error_details import ErrorDetails
from openapi_server.models.event_hub_consumer_group_info import EventHubConsumerGroupInfo
from openapi_server.models.iot_hub_description import IotHubDescription


pytestmark = pytest.mark.asyncio

async def test_iot_hub_resource_create_event_hub_consumer_group(client):
    """Test case for iot_hub_resource_create_event_hub_consumer_group

    Add a consumer group to an Event Hub-compatible endpoint in an IoT hub.
    """
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs/{resource_name}/eventHubEndpoints/{event_hub_endpoint_name}/ConsumerGroups/{name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example', event_hub_endpoint_name='event_hub_endpoint_name_example', name='name_example'),
        headers=headers,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')


pytestmark = pytest.mark.asyncio

async def test_iot_hub_resource_create_or_update(client):
    """Test case for iot_hub_resource_create_or_update

    Create or update the metadata of an IoT hub.
    """
    iot_hub_description = {"resourcegroup":"resourcegroup","etag":"etag","sku":{"tier":"Free","name":"F1","capacity":2},"subscriptionid":"subscriptionid","properties":{"hostName":"hostName","comments":"comments","ipFilterRules":[{"filterName":"filterName","ipMask":"ipMask","action":"Accept"},{"filterName":"filterName","ipMask":"ipMask","action":"Accept"}],"eventHubEndpoints":{"key":{"partitionCount":1,"path":"path","endpoint":"endpoint","retentionTimeInDays":5,"partitionIds":["partitionIds","partitionIds"]}},"operationsMonitoringProperties":{"events":{"key":"None"}},"provisioningState":"provisioningState","messagingEndpoints":{"key":{"ttlAsIso8601":"ttlAsIso8601","maxDeliveryCount":56,"lockDurationAsIso8601":"lockDurationAsIso8601"}},"features":"None","routing":{"fallbackRoute":{"condition":"condition","isEnabled":True,"source":"DeviceMessages","endpointNames":["endpointNames"]},"routes":[{"condition":"condition","isEnabled":True,"name":"name","source":"DeviceMessages","endpointNames":["endpointNames"]},{"condition":"condition","isEnabled":True,"name":"name","source":"DeviceMessages","endpointNames":["endpointNames"]}],"endpoints":{"eventHubs":[{"connectionString":"connectionString","resourceGroup":"resourceGroup","name":"name","subscriptionId":"subscriptionId"},{"connectionString":"connectionString","resourceGroup":"resourceGroup","name":"name","subscriptionId":"subscriptionId"}],"serviceBusTopics":[{"connectionString":"connectionString","resourceGroup":"resourceGroup","name":"name","subscriptionId":"subscriptionId"},{"connectionString":"connectionString","resourceGroup":"resourceGroup","name":"name","subscriptionId":"subscriptionId"}],"serviceBusQueues":[{"connectionString":"connectionString","resourceGroup":"resourceGroup","name":"name","subscriptionId":"subscriptionId"},{"connectionString":"connectionString","resourceGroup":"resourceGroup","name":"name","subscriptionId":"subscriptionId"}]}},"storageEndpoints":{"key":{"connectionString":"connectionString","sasTtlAsIso8601":"sasTtlAsIso8601","containerName":"containerName"}},"enableFileUploadNotifications":True,"authorizationPolicies":[{"secondaryKey":"secondaryKey","rights":"RegistryRead","keyName":"keyName","primaryKey":"primaryKey"},{"secondaryKey":"secondaryKey","rights":"RegistryRead","keyName":"keyName","primaryKey":"primaryKey"}],"cloudToDevice":{"feedback":{"ttlAsIso8601":"ttlAsIso8601","maxDeliveryCount":8,"lockDurationAsIso8601":"lockDurationAsIso8601"},"defaultTtlAsIso8601":"defaultTtlAsIso8601","maxDeliveryCount":60}}}
    params = [('api-version', 'api_version_example')]
    headers = { 
        'Accept': 'application/json',
        'Content-Type': 'application/json',
    }
    response = await client.request(
        method='PUT',
        path='/subscriptions/{subscription_id}/resourceGroups/{resource_group_name}/providers/Microsoft.Devices/IotHubs/{resource_name}'.format(subscription_id='subscription_id_example', resource_group_name='resource_group_name_example', resource_name='resource_name_example'),
        headers=headers,
        json=iot_hub_description,
        params=params,
        )
    assert response.status == 200, 'Response body is : ' + (await response.read()).decode('utf-8')

