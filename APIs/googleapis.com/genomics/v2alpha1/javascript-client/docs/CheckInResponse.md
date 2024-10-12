# GenomicsApi.CheckInResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**deadline** | **String** | The deadline by which the worker must request an extension. The backend will allow for network transmission time and other delays, but the worker must attempt to transmit the extension request no later than the deadline. | [optional] 
**features** | **{String: Object}** | Feature configuration for the operation. | [optional] 
**metadata** | **{String: Object}** | The metadata that describes the operation assigned to the worker. | [optional] 


