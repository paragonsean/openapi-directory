# TimeSeriesInsightsClient.AzureEventSourceProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**eventSourceResourceId** | **String** | The resource id of the event source in Azure Resource Manager. | 
**timestampPropertyName** | **String** | The event property that will be used as the event source&#39;s timestamp. If a value isn&#39;t specified for timestampPropertyName, or if null or empty-string is specified, the event creation time will be used. | [optional] 
**creationTime** | **Date** | The time the resource was created. | [optional] [readonly] 
**provisioningState** | [**ProvisioningState**](ProvisioningState.md) |  | [optional] 


