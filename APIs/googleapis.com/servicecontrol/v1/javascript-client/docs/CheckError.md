# ServiceControlApi.CheckError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **String** | The error code. | [optional] 
**detail** | **String** | Free-form text providing details on the error cause of the error. | [optional] 
**status** | [**Status**](Status.md) |  | [optional] 
**subject** | **String** | Subject to whom this error applies. See the specific code enum for more details on this field. For example: - \&quot;project:\&quot; - \&quot;folder:\&quot; - \&quot;organization:\&quot; | [optional] 



## Enum: CodeEnum


* `ERROR_CODE_UNSPECIFIED` (value: `"ERROR_CODE_UNSPECIFIED"`)

* `NOT_FOUND` (value: `"NOT_FOUND"`)

* `PERMISSION_DENIED` (value: `"PERMISSION_DENIED"`)

* `RESOURCE_EXHAUSTED` (value: `"RESOURCE_EXHAUSTED"`)

* `BUDGET_EXCEEDED` (value: `"BUDGET_EXCEEDED"`)

* `DENIAL_OF_SERVICE_DETECTED` (value: `"DENIAL_OF_SERVICE_DETECTED"`)

* `LOAD_SHEDDING` (value: `"LOAD_SHEDDING"`)

* `ABUSER_DETECTED` (value: `"ABUSER_DETECTED"`)

* `SERVICE_NOT_ACTIVATED` (value: `"SERVICE_NOT_ACTIVATED"`)

* `VISIBILITY_DENIED` (value: `"VISIBILITY_DENIED"`)

* `BILLING_DISABLED` (value: `"BILLING_DISABLED"`)

* `PROJECT_DELETED` (value: `"PROJECT_DELETED"`)

* `PROJECT_INVALID` (value: `"PROJECT_INVALID"`)

* `CONSUMER_INVALID` (value: `"CONSUMER_INVALID"`)

* `IP_ADDRESS_BLOCKED` (value: `"IP_ADDRESS_BLOCKED"`)

* `REFERER_BLOCKED` (value: `"REFERER_BLOCKED"`)

* `CLIENT_APP_BLOCKED` (value: `"CLIENT_APP_BLOCKED"`)

* `API_TARGET_BLOCKED` (value: `"API_TARGET_BLOCKED"`)

* `API_KEY_INVALID` (value: `"API_KEY_INVALID"`)

* `API_KEY_EXPIRED` (value: `"API_KEY_EXPIRED"`)

* `API_KEY_NOT_FOUND` (value: `"API_KEY_NOT_FOUND"`)

* `SPATULA_HEADER_INVALID` (value: `"SPATULA_HEADER_INVALID"`)

* `LOAS_ROLE_INVALID` (value: `"LOAS_ROLE_INVALID"`)

* `NO_LOAS_PROJECT` (value: `"NO_LOAS_PROJECT"`)

* `LOAS_PROJECT_DISABLED` (value: `"LOAS_PROJECT_DISABLED"`)

* `SECURITY_POLICY_VIOLATED` (value: `"SECURITY_POLICY_VIOLATED"`)

* `INVALID_CREDENTIAL` (value: `"INVALID_CREDENTIAL"`)

* `LOCATION_POLICY_VIOLATED` (value: `"LOCATION_POLICY_VIOLATED"`)

* `NAMESPACE_LOOKUP_UNAVAILABLE` (value: `"NAMESPACE_LOOKUP_UNAVAILABLE"`)

* `SERVICE_STATUS_UNAVAILABLE` (value: `"SERVICE_STATUS_UNAVAILABLE"`)

* `BILLING_STATUS_UNAVAILABLE` (value: `"BILLING_STATUS_UNAVAILABLE"`)

* `QUOTA_CHECK_UNAVAILABLE` (value: `"QUOTA_CHECK_UNAVAILABLE"`)

* `LOAS_PROJECT_LOOKUP_UNAVAILABLE` (value: `"LOAS_PROJECT_LOOKUP_UNAVAILABLE"`)

* `CLOUD_RESOURCE_MANAGER_BACKEND_UNAVAILABLE` (value: `"CLOUD_RESOURCE_MANAGER_BACKEND_UNAVAILABLE"`)

* `SECURITY_POLICY_BACKEND_UNAVAILABLE` (value: `"SECURITY_POLICY_BACKEND_UNAVAILABLE"`)

* `LOCATION_POLICY_BACKEND_UNAVAILABLE` (value: `"LOCATION_POLICY_BACKEND_UNAVAILABLE"`)

* `INJECTED_ERROR` (value: `"INJECTED_ERROR"`)




