

# IoTHubStreamInputDataSourceProperties

The properties that are associated with a IoT Hub input containing stream data.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**consumerGroupName** | **String** | The name of an IoT Hub Consumer Group that should be used to read events from the IoT Hub. If not specified, the input uses the Iot Hub’s default consumer group. |  [optional] |
|**endpoint** | **String** | The IoT Hub endpoint to connect to (ie. messages/events, messages/operationsMonitoringEvents, etc.). |  [optional] |
|**iotHubNamespace** | **String** | The name or the URI of the IoT Hub. Required on PUT (CreateOrReplace) requests. |  [optional] |
|**sharedAccessPolicyKey** | **String** | The shared access policy key for the specified shared access policy. Required on PUT (CreateOrReplace) requests. |  [optional] |
|**sharedAccessPolicyName** | **String** | The shared access policy name for the IoT Hub. This policy must contain at least the Service connect permission. Required on PUT (CreateOrReplace) requests. |  [optional] |



