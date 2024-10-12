# IotHubClient.RoutingEndpoints

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eventHubs** | [**[RoutingEventHubProperties]**](RoutingEventHubProperties.md) | The list of Event Hubs endpoints that IoT hub routes messages to, based on the routing rules. This list does not include the built-in Event Hubs endpoint. | [optional] 
**serviceBusQueues** | [**[RoutingServiceBusQueueEndpointProperties]**](RoutingServiceBusQueueEndpointProperties.md) | The list of Service Bus queue endpoints that IoT hub routes the messages to, based on the routing rules. | [optional] 
**serviceBusTopics** | [**[RoutingServiceBusTopicEndpointProperties]**](RoutingServiceBusTopicEndpointProperties.md) | The list of Service Bus topic endpoints that the IoT hub routes the messages to, based on the routing rules. | [optional] 
**storageContainers** | [**[RoutingStorageContainerProperties]**](RoutingStorageContainerProperties.md) | The list of storage container endpoints that IoT hub routes messages to, based on the routing rules. | [optional] 


