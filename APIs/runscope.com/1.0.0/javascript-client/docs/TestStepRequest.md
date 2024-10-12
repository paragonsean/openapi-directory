# RunscopeApi.TestStepRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**stepType** | **String** | Type of test step -- request, pause, condition, ghost-inspector, or subtest. | [optional] 
**assertions** | [**[Assertion]**](Assertion.md) | A list of assertions to apply to the HTTP response from this request. | [optional] 
**auth** | **Object** | An authentication object with either basic, oauth1, or client_certificate credentials for authenticating this request. | [optional] 
**beforeScripts** | **[String]** | A list of pre-request scripts to run before this request. | [optional] 
**body** | **String** | A string to use as the body of the request. | [optional] 
**form** | **Object** | An object with keys as form post parameter names matched to their values. Values can either be a single string or an array of strings. | [optional] 
**headers** | **Object** | An object with keys as header names matched to their values. Values can either be a single string or an array of strings. | [optional] 
**method** | **String** | The HTTP method for this request step. E.g. GET, POST, PUT, DELETE, etc. | [optional] 
**note** | **String** | A description or note for this request step. | [optional] 
**scripts** | **[String]** | A list of post-response scripts to run after this request. | [optional] 
**url** | **String** | The URL to make a request to for this step. This may contain both query string parameters and variables. | [optional] 
**variables** | [**[Variable]**](Variable.md) | A list of variables to extract out of the HTTP response from this request. | [optional] 


