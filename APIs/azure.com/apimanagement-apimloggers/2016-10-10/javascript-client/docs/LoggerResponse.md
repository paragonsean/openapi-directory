# ApiManagementClient.LoggerResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**credentials** | **{String: String}** | The name and SendRule connection string of the event hub. | 
**description** | **String** | Logger description. | [optional] 
**id** | **String** | Uniquely identifies the logger within the current API Management service instance. The value is a valid relative URL in the format of /loggers/{loggerId} where {loggerId} is a logger identifier. | [optional] [readonly] 
**isBuffered** | **Boolean** | Whether records are buffered in the logger before publishing. Default is assumed to be true. | [optional] [default to true]
**type** | **String** | Logger type. | 



## Enum: TypeEnum


* `AzureEventHub` (value: `"AzureEventHub"`)




