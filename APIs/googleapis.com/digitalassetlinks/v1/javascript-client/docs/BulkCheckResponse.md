# DigitalAssetLinksApi.BulkCheckResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bulkErrorCode** | **String** | Error code for the entire request. Present only if the entire request failed. Individual check errors will not trigger the presence of this field. | [optional] 
**checkResults** | [**[CheckResponse]**](CheckResponse.md) | List of results for each check request. Results are returned in the same order in which they were sent in the request. | [optional] 



## Enum: BulkErrorCodeEnum


* `UNSPECIFIED` (value: `"ERROR_CODE_UNSPECIFIED"`)

* `INVALID_QUERY` (value: `"ERROR_CODE_INVALID_QUERY"`)

* `FETCH_ERROR` (value: `"ERROR_CODE_FETCH_ERROR"`)

* `FAILED_SSL_VALIDATION` (value: `"ERROR_CODE_FAILED_SSL_VALIDATION"`)

* `REDIRECT` (value: `"ERROR_CODE_REDIRECT"`)

* `TOO_LARGE` (value: `"ERROR_CODE_TOO_LARGE"`)

* `MALFORMED_HTTP_RESPONSE` (value: `"ERROR_CODE_MALFORMED_HTTP_RESPONSE"`)

* `WRONG_CONTENT_TYPE` (value: `"ERROR_CODE_WRONG_CONTENT_TYPE"`)

* `MALFORMED_CONTENT` (value: `"ERROR_CODE_MALFORMED_CONTENT"`)

* `SECURE_ASSET_INCLUDES_INSECURE` (value: `"ERROR_CODE_SECURE_ASSET_INCLUDES_INSECURE"`)

* `FETCH_BUDGET_EXHAUSTED` (value: `"ERROR_CODE_FETCH_BUDGET_EXHAUSTED"`)




