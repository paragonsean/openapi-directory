# TimeSeriesInsightsClient.EventSourceCommonProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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




