# KubernetesEngineApi.StatusCondition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**canonicalCode** | **String** | Canonical code of the condition. | [optional] 
**code** | **String** | Machine-friendly representation of the condition Deprecated. Use canonical_code instead. | [optional] 
**message** | **String** | Human-friendly representation of the condition | [optional] 



## Enum: CanonicalCodeEnum


* `OK` (value: `"OK"`)

* `CANCELLED` (value: `"CANCELLED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `INVALID_ARGUMENT` (value: `"INVALID_ARGUMENT"`)

* `DEADLINE_EXCEEDED` (value: `"DEADLINE_EXCEEDED"`)

* `NOT_FOUND` (value: `"NOT_FOUND"`)

* `ALREADY_EXISTS` (value: `"ALREADY_EXISTS"`)

* `PERMISSION_DENIED` (value: `"PERMISSION_DENIED"`)

* `UNAUTHENTICATED` (value: `"UNAUTHENTICATED"`)

* `RESOURCE_EXHAUSTED` (value: `"RESOURCE_EXHAUSTED"`)

* `FAILED_PRECONDITION` (value: `"FAILED_PRECONDITION"`)

* `ABORTED` (value: `"ABORTED"`)

* `OUT_OF_RANGE` (value: `"OUT_OF_RANGE"`)

* `UNIMPLEMENTED` (value: `"UNIMPLEMENTED"`)

* `INTERNAL` (value: `"INTERNAL"`)

* `UNAVAILABLE` (value: `"UNAVAILABLE"`)

* `DATA_LOSS` (value: `"DATA_LOSS"`)





## Enum: CodeEnum


* `UNKNOWN` (value: `"UNKNOWN"`)

* `GCE_STOCKOUT` (value: `"GCE_STOCKOUT"`)

* `GKE_SERVICE_ACCOUNT_DELETED` (value: `"GKE_SERVICE_ACCOUNT_DELETED"`)

* `GCE_QUOTA_EXCEEDED` (value: `"GCE_QUOTA_EXCEEDED"`)

* `SET_BY_OPERATOR` (value: `"SET_BY_OPERATOR"`)

* `CLOUD_KMS_KEY_ERROR` (value: `"CLOUD_KMS_KEY_ERROR"`)

* `CA_EXPIRING` (value: `"CA_EXPIRING"`)




