# TimeSeriesInsightsClient.EventHubEventSourceCreationProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**sharedAccessKey** | **String** | The value of the shared access key that grants the Time Series Insights service read access to the event hub. This property is not shown in event source responses. | 
**consumerGroupName** | **String** | The name of the event hub&#39;s consumer group that holds the partitions from which events will be read. | 
**eventHubName** | **String** | The name of the event hub. | 
**keyName** | **String** | The name of the SAS key that grants the Time Series Insights service access to the event hub. The shared access policies for this key must grant &#39;Listen&#39; permissions to the event hub. | 
**serviceBusNamespace** | **String** | The name of the service bus that contains the event hub. | 
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




