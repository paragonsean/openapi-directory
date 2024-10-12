

# JobSchedulingError

An error encountered by the Batch service when scheduling a job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**category** | [**CategoryEnum**](#CategoryEnum) | Gets or sets the category of the job scheduling error. |  |
|**code** | **String** | Gets or sets an identifier for the job scheduling error.  Codes are invariant and are intended to be consumed programmatically. |  [optional] |
|**details** | [**List&lt;NameValuePair&gt;**](NameValuePair.md) | Gets or sets a list of additional error details related to the scheduling error. |  [optional] |
|**message** | **String** | Gets or sets a message describing the job scheduling error, intended to be suitable for display in a user interface. |  [optional] |



## Enum: CategoryEnum

| Name | Value |
|---- | -----|
| USERERROR | &quot;usererror&quot; |
| SERVERERROR | &quot;servererror&quot; |
| UNMAPPED | &quot;unmapped&quot; |



