# CdnManagementClient.ResponseBasedOriginErrorDetectionParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**httpErrorRanges** | [**[HttpErrorRangeParameters]**](HttpErrorRangeParameters.md) | The list of Http status code ranges that are considered as server errors for origin and it is marked as unhealthy. | [optional] 
**responseBasedDetectedErrorTypes** | **String** | Type of response errors for real user requests for which origin will be deemed unhealthy | [optional] 
**responseBasedFailoverThresholdPercentage** | **Number** | The percentage of failed requests in the sample where failover should trigger. | [optional] 



## Enum: ResponseBasedDetectedErrorTypesEnum


* `None` (value: `"None"`)

* `TcpErrorsOnly` (value: `"TcpErrorsOnly"`)

* `TcpAndHttpErrors` (value: `"TcpAndHttpErrors"`)




