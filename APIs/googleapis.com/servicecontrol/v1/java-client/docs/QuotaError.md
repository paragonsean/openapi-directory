

# QuotaError

Represents error information for QuotaOperation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | Error code. |  [optional] |
|**description** | **String** | Free-form text that provides details on the cause of the error. |  [optional] |
|**status** | [**Status**](Status.md) |  |  [optional] |
|**subject** | **String** | Subject to whom this error applies. See the specific enum for more details on this field. For example, \&quot;clientip:\&quot; or \&quot;project:\&quot;. |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| RESOURCE_EXHAUSTED | &quot;RESOURCE_EXHAUSTED&quot; |
| OUT_OF_RANGE | &quot;OUT_OF_RANGE&quot; |
| BILLING_NOT_ACTIVE | &quot;BILLING_NOT_ACTIVE&quot; |
| PROJECT_DELETED | &quot;PROJECT_DELETED&quot; |
| API_KEY_INVALID | &quot;API_KEY_INVALID&quot; |
| API_KEY_EXPIRED | &quot;API_KEY_EXPIRED&quot; |
| SPATULA_HEADER_INVALID | &quot;SPATULA_HEADER_INVALID&quot; |
| LOAS_ROLE_INVALID | &quot;LOAS_ROLE_INVALID&quot; |
| NO_LOAS_PROJECT | &quot;NO_LOAS_PROJECT&quot; |
| PROJECT_STATUS_UNAVAILABLE | &quot;PROJECT_STATUS_UNAVAILABLE&quot; |
| SERVICE_STATUS_UNAVAILABLE | &quot;SERVICE_STATUS_UNAVAILABLE&quot; |
| BILLING_STATUS_UNAVAILABLE | &quot;BILLING_STATUS_UNAVAILABLE&quot; |
| QUOTA_SYSTEM_UNAVAILABLE | &quot;QUOTA_SYSTEM_UNAVAILABLE&quot; |



