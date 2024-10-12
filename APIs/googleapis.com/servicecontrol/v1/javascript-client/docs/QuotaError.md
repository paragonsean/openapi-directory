# ServiceControlApi.QuotaError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | Error code. | [optional] 
**description** | **String** | Free-form text that provides details on the cause of the error. | [optional] 
**status** | [**Status**](Status.md) |  | [optional] 
**subject** | **String** | Subject to whom this error applies. See the specific enum for more details on this field. For example, \&quot;clientip:\&quot; or \&quot;project:\&quot;. | [optional] 



## Enum: CodeEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `RESOURCE_EXHAUSTED` (value: `"RESOURCE_EXHAUSTED"`)

* `OUT_OF_RANGE` (value: `"OUT_OF_RANGE"`)

* `BILLING_NOT_ACTIVE` (value: `"BILLING_NOT_ACTIVE"`)

* `PROJECT_DELETED` (value: `"PROJECT_DELETED"`)

* `API_KEY_INVALID` (value: `"API_KEY_INVALID"`)

* `API_KEY_EXPIRED` (value: `"API_KEY_EXPIRED"`)

* `SPATULA_HEADER_INVALID` (value: `"SPATULA_HEADER_INVALID"`)

* `LOAS_ROLE_INVALID` (value: `"LOAS_ROLE_INVALID"`)

* `NO_LOAS_PROJECT` (value: `"NO_LOAS_PROJECT"`)

* `PROJECT_STATUS_UNAVAILABLE` (value: `"PROJECT_STATUS_UNAVAILABLE"`)

* `SERVICE_STATUS_UNAVAILABLE` (value: `"SERVICE_STATUS_UNAVAILABLE"`)

* `BILLING_STATUS_UNAVAILABLE` (value: `"BILLING_STATUS_UNAVAILABLE"`)

* `QUOTA_SYSTEM_UNAVAILABLE` (value: `"QUOTA_SYSTEM_UNAVAILABLE"`)




