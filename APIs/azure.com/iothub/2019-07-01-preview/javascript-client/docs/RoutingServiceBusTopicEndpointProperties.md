# IotHubClient.RoutingServiceBusTopicEndpointProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connectionString** | **String** | The connection string of the service bus topic endpoint. | 
**name** | **String** | The name that identifies this endpoint. The name can only include alphanumeric characters, periods, underscores, hyphens and has a maximum length of 64 characters. The following names are reserved:  events, fileNotifications, $default. Endpoint names must be unique across endpoint types.  The name need not be the same as the actual topic name. | 
**resourceGroup** | **String** | The name of the resource group of the service bus topic endpoint. | [optional] 
**subscriptionId** | **String** | The subscription identifier of the service bus topic endpoint. | [optional] 


