

# CheckError

Defines the errors to be returned in google.api.servicecontrol.v1.CheckResponse.check_errors.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**code** | [**CodeEnum**](#CodeEnum) | The error code. |  [optional] |
|**detail** | **String** | Free-form text providing details on the error cause of the error. |  [optional] |
|**status** | [**Status**](Status.md) |  |  [optional] |
|**subject** | **String** | Subject to whom this error applies. See the specific code enum for more details on this field. For example: - \&quot;project:\&quot; - \&quot;folder:\&quot; - \&quot;organization:\&quot; |  [optional] |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| ERROR_CODE_UNSPECIFIED | &quot;ERROR_CODE_UNSPECIFIED&quot; |
| NOT_FOUND | &quot;NOT_FOUND&quot; |
| PERMISSION_DENIED | &quot;PERMISSION_DENIED&quot; |
| RESOURCE_EXHAUSTED | &quot;RESOURCE_EXHAUSTED&quot; |
| BUDGET_EXCEEDED | &quot;BUDGET_EXCEEDED&quot; |
| DENIAL_OF_SERVICE_DETECTED | &quot;DENIAL_OF_SERVICE_DETECTED&quot; |
| LOAD_SHEDDING | &quot;LOAD_SHEDDING&quot; |
| ABUSER_DETECTED | &quot;ABUSER_DETECTED&quot; |
| SERVICE_NOT_ACTIVATED | &quot;SERVICE_NOT_ACTIVATED&quot; |
| VISIBILITY_DENIED | &quot;VISIBILITY_DENIED&quot; |
| BILLING_DISABLED | &quot;BILLING_DISABLED&quot; |
| PROJECT_DELETED | &quot;PROJECT_DELETED&quot; |
| PROJECT_INVALID | &quot;PROJECT_INVALID&quot; |
| CONSUMER_INVALID | &quot;CONSUMER_INVALID&quot; |
| IP_ADDRESS_BLOCKED | &quot;IP_ADDRESS_BLOCKED&quot; |
| REFERER_BLOCKED | &quot;REFERER_BLOCKED&quot; |
| CLIENT_APP_BLOCKED | &quot;CLIENT_APP_BLOCKED&quot; |
| API_TARGET_BLOCKED | &quot;API_TARGET_BLOCKED&quot; |
| API_KEY_INVALID | &quot;API_KEY_INVALID&quot; |
| API_KEY_EXPIRED | &quot;API_KEY_EXPIRED&quot; |
| API_KEY_NOT_FOUND | &quot;API_KEY_NOT_FOUND&quot; |
| SPATULA_HEADER_INVALID | &quot;SPATULA_HEADER_INVALID&quot; |
| LOAS_ROLE_INVALID | &quot;LOAS_ROLE_INVALID&quot; |
| NO_LOAS_PROJECT | &quot;NO_LOAS_PROJECT&quot; |
| LOAS_PROJECT_DISABLED | &quot;LOAS_PROJECT_DISABLED&quot; |
| SECURITY_POLICY_VIOLATED | &quot;SECURITY_POLICY_VIOLATED&quot; |
| INVALID_CREDENTIAL | &quot;INVALID_CREDENTIAL&quot; |
| LOCATION_POLICY_VIOLATED | &quot;LOCATION_POLICY_VIOLATED&quot; |
| NAMESPACE_LOOKUP_UNAVAILABLE | &quot;NAMESPACE_LOOKUP_UNAVAILABLE&quot; |
| SERVICE_STATUS_UNAVAILABLE | &quot;SERVICE_STATUS_UNAVAILABLE&quot; |
| BILLING_STATUS_UNAVAILABLE | &quot;BILLING_STATUS_UNAVAILABLE&quot; |
| QUOTA_CHECK_UNAVAILABLE | &quot;QUOTA_CHECK_UNAVAILABLE&quot; |
| LOAS_PROJECT_LOOKUP_UNAVAILABLE | &quot;LOAS_PROJECT_LOOKUP_UNAVAILABLE&quot; |
| CLOUD_RESOURCE_MANAGER_BACKEND_UNAVAILABLE | &quot;CLOUD_RESOURCE_MANAGER_BACKEND_UNAVAILABLE&quot; |
| SECURITY_POLICY_BACKEND_UNAVAILABLE | &quot;SECURITY_POLICY_BACKEND_UNAVAILABLE&quot; |
| LOCATION_POLICY_BACKEND_UNAVAILABLE | &quot;LOCATION_POLICY_BACKEND_UNAVAILABLE&quot; |
| INJECTED_ERROR | &quot;INJECTED_ERROR&quot; |



