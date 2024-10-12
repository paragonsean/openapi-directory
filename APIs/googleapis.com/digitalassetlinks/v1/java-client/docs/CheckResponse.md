

# CheckResponse

Response message for the CheckAssetLinks call.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**debugString** | **String** | Human-readable message containing information intended to help end users understand, reproduce and debug the result. The message will be in English and we are currently not planning to offer any translations. Please note that no guarantees are made about the contents or format of this string. Any aspect of it may be subject to change without notice. You should not attempt to programmatically parse this data. For programmatic access, use the error_code field below. |  [optional] |
|**errorCode** | [**List&lt;ErrorCodeEnum&gt;**](#List&lt;ErrorCodeEnum&gt;) | Error codes that describe the result of the Check operation. |  [optional] |
|**linked** | **Boolean** | Set to true if the assets specified in the request are linked by the relation specified in the request. |  [optional] |
|**maxAge** | **String** | From serving time, how much longer the response should be considered valid barring further updates. REQUIRED |  [optional] |



## Enum: List&lt;ErrorCodeEnum&gt;

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



