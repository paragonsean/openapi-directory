# ApiManagementClient.LoggerCreateParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | **{String: String}** | The name and SendRule connection string of the event hub. | 
**description** | **String** | Logger description. | [optional] 
**isBuffered** | **Boolean** | Whether records are buffered in the logger before publishing. Default is assumed to be true. | [optional] 
**type** | **String** | Logger type. | 



## Enum: TypeEnum


* `AzureEventHub` (value: `"AzureEventHub"`)




