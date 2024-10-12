# ApiManagementClient.LoggerListByService200ResponseValueInnerProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | **{String: String}** | The name and SendRule connection string of the event hub for azureEventHub logger. Instrumentation key for applicationInsights logger. | 
**description** | **String** | Logger description. | [optional] 
**isBuffered** | **Boolean** | Whether records are buffered in the logger before publishing. Default is assumed to be true. | [optional] 
**loggerType** | **String** | Logger type. | 
**resourceId** | **String** | Azure Resource Id of a log target (either Azure Event Hub resource or Azure Application Insights resource). | [optional] 



## Enum: LoggerTypeEnum


* `azureEventHub` (value: `"azureEventHub"`)

* `applicationInsights` (value: `"applicationInsights"`)




