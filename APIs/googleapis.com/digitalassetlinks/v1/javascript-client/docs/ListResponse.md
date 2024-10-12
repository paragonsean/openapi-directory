# DigitalAssetLinksApi.ListResponse

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**debugString** | **String** | Human-readable message containing information intended to help end users understand, reproduce and debug the result. The message will be in English and we are currently not planning to offer any translations. Please note that no guarantees are made about the contents or format of this string. Any aspect of it may be subject to change without notice. You should not attempt to programmatically parse this data. For programmatic access, use the error_code field below. | [optional] 
**errorCode** | **[String]** | Error codes that describe the result of the List operation. | [optional] 
**maxAge** | **String** | From serving time, how much longer the response should be considered valid barring further updates. REQUIRED | [optional] 
**statements** | [**[Statement]**](Statement.md) | A list of all the matching statements that have been found. | [optional] 



## Enum: [ErrorCodeEnum]


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




