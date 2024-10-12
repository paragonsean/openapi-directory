

# GoogleRpcPreconditionFailureViolation

A message type used to describe a single precondition failure.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**description** | **String** | A description of how the precondition failed. Developers can use this description to understand how to fix the failure. For example: \&quot;Terms of service not accepted\&quot;. |  [optional] |
|**subject** | **String** | The subject, relative to the type, that failed. For example, \&quot;google.com/cloud\&quot; relative to the \&quot;TOS\&quot; type would indicate which terms of service is being referenced. |  [optional] |
|**type** | **String** | The type of PreconditionFailure. We recommend using a service-specific enum type to define the supported precondition violation subjects. For example, \&quot;TOS\&quot; for \&quot;Terms of Service violation\&quot;. |  [optional] |



