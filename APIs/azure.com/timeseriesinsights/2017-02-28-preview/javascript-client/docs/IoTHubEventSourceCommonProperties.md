# TimeSeriesInsightsClient.IoTHubEventSourceCommonProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**consumerGroupName** | **String** | The name of the iot hub&#39;s consumer group that holds the partitions from which events will be read. | 
**iotHubName** | **String** | The name of the iot hub. | 
**keyName** | **String** | The name of the Shared Access Policy key that grants the Time Series Insights service access to the iot hub. This shared access policy key must grant &#39;service connect&#39; permissions to the iot hub. | 
**eventSourceResourceId** | **String** | The resource id of the event source in Azure Resource Manager. | 
**timestampPropertyName** | **String** | The event property that will be used as the event source&#39;s timestamp. If a value isn&#39;t specified for timestampPropertyName, or if null or empty-string is specified, the event creation time will be used. | [optional] 
**creationTime** | **Date** | The time the resource was created. | [optional] [readonly] 
**provisioningState** | **String** | Provisioning state of the resource. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Accepted` (value: `"Accepted"`)

* `Creating` (value: `"Creating"`)

* `Updating` (value: `"Updating"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Deleting` (value: `"Deleting"`)




