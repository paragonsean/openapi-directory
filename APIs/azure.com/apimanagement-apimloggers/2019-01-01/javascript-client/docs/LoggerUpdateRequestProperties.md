# ApiManagementClient.LoggerUpdateRequestProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | **{String: String}** | Logger credentials. | [optional] 
**description** | **String** | Logger description. | [optional] 
**isBuffered** | **Boolean** | Whether records are buffered in the logger before publishing. Default is assumed to be true. | [optional] 
**loggerType** | **String** | Logger type. | [optional] 



## Enum: LoggerTypeEnum


* `azureEventHub` (value: `"azureEventHub"`)

* `applicationInsights` (value: `"applicationInsights"`)




