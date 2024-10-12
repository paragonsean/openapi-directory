

# IdentityErrorResponse

This is the response from an Identity operation in the case an error occurs.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**error** | [**ErrorEnum**](#ErrorEnum) | Error code |  [optional] |
|**errorDescription** | **String** | Error message indicating why the operation failed. |  [optional] |



## Enum: ErrorEnum

| Name | Value |
|---- | -----|
| INVALID_REQUEST | &quot;invalid_request&quot; |
| UNAUTHORIZED_CLIENT | &quot;unauthorized_client&quot; |
| ACCESS_DENIED | &quot;access_denied&quot; |
| UNSUPPORTED_RESPONSE_TYPE | &quot;unsupported_response_type&quot; |
| INVALID_SCOPE | &quot;invalid_scope&quot; |
| SERVER_ERROR | &quot;server_error&quot; |
| SERVICE_UNAVAILABLE | &quot;service_unavailable&quot; |
| BAD_REQUEST | &quot;bad_request&quot; |
| FORBIDDEN | &quot;forbidden&quot; |
| NOT_FOUND | &quot;not_found&quot; |
| METHOD_NOT_ALLOWED | &quot;method_not_allowed&quot; |
| TOO_MANY_REQUESTS | &quot;too_many_requests&quot; |



