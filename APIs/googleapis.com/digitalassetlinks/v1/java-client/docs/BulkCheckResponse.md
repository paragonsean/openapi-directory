

# BulkCheckResponse

Response for BulkCheck call. Results are sent in a list in the same order in which they were sent. Individual check errors are described in the appropriate check_results entry. If the entire call fails, the response will include a bulk_error_code field describing the error.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bulkErrorCode** | [**BulkErrorCodeEnum**](#BulkErrorCodeEnum) | Error code for the entire request. Present only if the entire request failed. Individual check errors will not trigger the presence of this field. |  [optional] |
|**checkResults** | [**List&lt;CheckResponse&gt;**](CheckResponse.md) | List of results for each check request. Results are returned in the same order in which they were sent in the request. |  [optional] |



## Enum: BulkErrorCodeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;ERROR_CODE_UNSPECIFIED&quot; |
| INVALID_QUERY | &quot;ERROR_CODE_INVALID_QUERY&quot; |
| FETCH_ERROR | &quot;ERROR_CODE_FETCH_ERROR&quot; |
| FAILED_SSL_VALIDATION | &quot;ERROR_CODE_FAILED_SSL_VALIDATION&quot; |
| REDIRECT | &quot;ERROR_CODE_REDIRECT&quot; |
| TOO_LARGE | &quot;ERROR_CODE_TOO_LARGE&quot; |
| MALFORMED_HTTP_RESPONSE | &quot;ERROR_CODE_MALFORMED_HTTP_RESPONSE&quot; |
| WRONG_CONTENT_TYPE | &quot;ERROR_CODE_WRONG_CONTENT_TYPE&quot; |
| MALFORMED_CONTENT | &quot;ERROR_CODE_MALFORMED_CONTENT&quot; |
| SECURE_ASSET_INCLUDES_INSECURE | &quot;ERROR_CODE_SECURE_ASSET_INCLUDES_INSECURE&quot; |
| FETCH_BUDGET_EXHAUSTED | &quot;ERROR_CODE_FETCH_BUDGET_EXHAUSTED&quot; |



