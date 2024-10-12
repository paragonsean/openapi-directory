# SandboxApi.RuntimeResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**body** | **String** | The body of the given response. | [optional] 
**durationMillis** | **Number** | Duration in milliseconds of the processing time in Sandbox. | [optional] 
**error** | [**Error**](Error.md) |  | [optional] 
**headers** | **{String: String}** | Transport headers for the given response. | [optional] 
**respondedTimestamp** | **Number** | The epoch time in milliseconds when the response was sent. | [optional] 
**responseDelay** | **Number** | Duration in milliseconds of the response delay. | [optional] 
**transport** | **String** | Which transport the request was for, &#39;HTTP&#39;. | [optional] 


