

# EventHubStreamInputDataSourceProperties

The properties that are associated with a Event Hub input containing stream data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consumerGroupName** | **String** | The name of an Event Hub Consumer Group that should be used to read events from the Event Hub. Specifying distinct consumer group names for multiple inputs allows each of those inputs to receive the same events from the Event Hub. If not specified, the input uses the Event Hub’s default consumer group. |  [optional] |
|**eventHubName** | **String** | The name of the Event Hub. Required on PUT (CreateOrReplace) requests. |  [optional] |
|**serviceBusNamespace** | **String** | The namespace that is associated with the desired Event Hub, Service Bus Queue, Service Bus Topic, etc. Required on PUT (CreateOrReplace) requests. |  [optional] |
|**sharedAccessPolicyKey** | **String** | The shared access policy key for the specified shared access policy. Required on PUT (CreateOrReplace) requests. |  [optional] |
|**sharedAccessPolicyName** | **String** | The shared access policy name for the Event Hub, Service Bus Queue, Service Bus Topic, etc. Required on PUT (CreateOrReplace) requests. |  [optional] |



