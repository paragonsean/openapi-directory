

# EventHubProperties

The properties of the provisioned Event Hub-compatible endpoint used by the IoT hub.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endpoint** | **String** | The Event Hub-compatible endpoint. |  [optional] [readonly] |
|**partitionCount** | **Integer** | The number of partitions for receiving device-to-cloud messages in the Event Hub-compatible endpoint. See: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging#device-to-cloud-messages. |  [optional] |
|**partitionIds** | **List&lt;String&gt;** | The partition ids in the Event Hub-compatible endpoint. |  [optional] [readonly] |
|**path** | **String** | The Event Hub-compatible name. |  [optional] [readonly] |
|**retentionTimeInDays** | **Long** | The retention time for device-to-cloud messages in days. See: https://docs.microsoft.com/azure/iot-hub/iot-hub-devguide-messaging#device-to-cloud-messages |  [optional] |



