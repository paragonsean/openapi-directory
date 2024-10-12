# BatchService.JobSchedulingError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **String** | Gets or sets the category of the job scheduling error. | 
**code** | **String** | Gets or sets an identifier for the job scheduling error.  Codes are invariant and are intended to be consumed programmatically. | [optional] 
**details** | [**[NameValuePair]**](NameValuePair.md) | Gets or sets a list of additional error details related to the scheduling error. | [optional] 
**message** | **String** | Gets or sets a message describing the job scheduling error, intended to be suitable for display in a user interface. | [optional] 



## Enum: CategoryEnum


* `usererror` (value: `"usererror"`)

* `servererror` (value: `"servererror"`)

* `unmapped` (value: `"unmapped"`)




