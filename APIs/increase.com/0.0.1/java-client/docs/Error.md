

# Error


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**detail** | **String** |  |  |
|**status** | [**StatusEnum**](#StatusEnum) |  |  |
|**title** | **String** |  |  |
|**type** | [**TypeEnum**](#TypeEnum) |  |  |
|**errors** | **List&lt;Object&gt;** | All errors related to parsing the request parameters. |  |
|**retryAfter** | **Integer** |  |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| NUMBER_429 | 429 |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| API_METHOD_NOT_FOUND_ERROR | &quot;api_method_not_found_error&quot; |
| ENVIRONMENT_MISMATCH_ERROR | &quot;environment_mismatch_error&quot; |
| IDEMPOTENCY_CONFLICT_ERROR | &quot;idempotency_conflict_error&quot; |
| IDEMPOTENCY_UNPROCESSABLE_ERROR | &quot;idempotency_unprocessable_error&quot; |
| INSUFFICIENT_PERMISSIONS_ERROR | &quot;insufficient_permissions_error&quot; |
| INTERNAL_SERVER_ERROR | &quot;internal_server_error&quot; |
| INVALID_API_KEY_ERROR | &quot;invalid_api_key_error&quot; |
| INVALID_OPERATION_ERROR | &quot;invalid_operation_error&quot; |
| INVALID_PARAMETERS_ERROR | &quot;invalid_parameters_error&quot; |
| MALFORMED_REQUEST_ERROR | &quot;malformed_request_error&quot; |
| OBJECT_NOT_FOUND_ERROR | &quot;object_not_found_error&quot; |
| PRIVATE_FEATURE_ERROR | &quot;private_feature_error&quot; |
| RATE_LIMITED_ERROR | &quot;rate_limited_error&quot; |



