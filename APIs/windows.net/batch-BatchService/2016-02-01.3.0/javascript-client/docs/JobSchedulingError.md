# BatchService.JobSchedulingError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | The category of the job scheduling error. | 
**code** | **String** | An identifier for the job scheduling error. Codes are invariant and are intended to be consumed programmatically. | [optional] 
**details** | [**[NameValuePair]**](NameValuePair.md) | A list of additional error details related to the scheduling error. | [optional] 
**message** | **String** | A message describing the job scheduling error, intended to be suitable for display in a user interface. | [optional] 



## Enum: CategoryEnum


* `usererror` (value: `"usererror"`)

* `servererror` (value: `"servererror"`)

* `unmapped` (value: `"unmapped"`)




