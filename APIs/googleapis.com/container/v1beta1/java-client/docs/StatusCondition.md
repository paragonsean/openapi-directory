

# StatusCondition

StatusCondition describes why a cluster or a node pool has a certain status (e.g., ERROR or DEGRADED).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**canonicalCode** | [**CanonicalCodeEnum**](#CanonicalCodeEnum) | Canonical code of the condition. |  [optional] |
|**code** | [**CodeEnum**](#CodeEnum) | Machine-friendly representation of the condition Deprecated. Use canonical_code instead. |  [optional] |
|**message** | **String** | Human-friendly representation of the condition |  [optional] |



## Enum: CanonicalCodeEnum

| Name | Value |
|---- | -----|
| OK | &quot;OK&quot; |
| CANCELLED | &quot;CANCELLED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| INVALID_ARGUMENT | &quot;INVALID_ARGUMENT&quot; |
| DEADLINE_EXCEEDED | &quot;DEADLINE_EXCEEDED&quot; |
| NOT_FOUND | &quot;NOT_FOUND&quot; |
| ALREADY_EXISTS | &quot;ALREADY_EXISTS&quot; |
| PERMISSION_DENIED | &quot;PERMISSION_DENIED&quot; |
| UNAUTHENTICATED | &quot;UNAUTHENTICATED&quot; |
| RESOURCE_EXHAUSTED | &quot;RESOURCE_EXHAUSTED&quot; |
| FAILED_PRECONDITION | &quot;FAILED_PRECONDITION&quot; |
| ABORTED | &quot;ABORTED&quot; |
| OUT_OF_RANGE | &quot;OUT_OF_RANGE&quot; |
| UNIMPLEMENTED | &quot;UNIMPLEMENTED&quot; |
| INTERNAL | &quot;INTERNAL&quot; |
| UNAVAILABLE | &quot;UNAVAILABLE&quot; |
| DATA_LOSS | &quot;DATA_LOSS&quot; |



## Enum: CodeEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;UNKNOWN&quot; |
| GCE_STOCKOUT | &quot;GCE_STOCKOUT&quot; |
| GKE_SERVICE_ACCOUNT_DELETED | &quot;GKE_SERVICE_ACCOUNT_DELETED&quot; |
| GCE_QUOTA_EXCEEDED | &quot;GCE_QUOTA_EXCEEDED&quot; |
| SET_BY_OPERATOR | &quot;SET_BY_OPERATOR&quot; |
| CLOUD_KMS_KEY_ERROR | &quot;CLOUD_KMS_KEY_ERROR&quot; |
| CA_EXPIRING | &quot;CA_EXPIRING&quot; |



