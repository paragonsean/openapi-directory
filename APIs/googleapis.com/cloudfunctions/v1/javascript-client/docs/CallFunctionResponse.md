# CloudFunctionsApi.CallFunctionResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**error** | **String** | Either system or user-function generated error. Set if execution was not successful. | [optional] 
**executionId** | **String** | Execution id of function invocation. | [optional] 
**result** | **String** | Result populated for successful execution of synchronous function. Will not be populated if function does not return a result through context. | [optional] 


