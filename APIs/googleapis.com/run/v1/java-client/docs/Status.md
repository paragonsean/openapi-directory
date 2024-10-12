

# Status

Status is a return value for calls that don't return other objects.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | **Integer** | Suggested HTTP return code for this status, 0 if not set. |  [optional] |
|**details** | [**StatusDetails**](StatusDetails.md) |  |  [optional] |
|**message** | **String** | A human-readable description of the status of this operation. |  [optional] |
|**metadata** | [**ListMeta**](ListMeta.md) |  |  [optional] |
|**reason** | **String** | A machine-readable description of why this operation is in the \&quot;Failure\&quot; status. If this value is empty there is no information available. A Reason clarifies an HTTP status code but does not override it. |  [optional] |
|**status** | **String** | Status of the operation. One of: \&quot;Success\&quot; or \&quot;Failure\&quot;. |  [optional] |



