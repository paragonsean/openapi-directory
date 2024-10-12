

# RestorePlan

The configuration of a potential series of Restore operations to be performed against Backups belong to a particular BackupPlan. Next id: 13

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupPlan** | **String** | Required. Immutable. A reference to the BackupPlan from which Backups may be used as the source for Restores created via this RestorePlan. Format: &#x60;projects/_*_/locations/_*_/backupPlans/_*&#x60;. |  [optional] |
|**cluster** | **String** | Required. Immutable. The target cluster into which Restores created via this RestorePlan will restore data. NOTE: the cluster&#39;s region must be the same as the RestorePlan. Valid formats: - &#x60;projects/_*_/locations/_*_/clusters/_*&#x60; - &#x60;projects/_*_/zones/_*_/clusters/_*&#x60; |  [optional] |
|**createTime** | **String** | Output only. The timestamp when this RestorePlan resource was created. |  [optional] [readonly] |
|**description** | **String** | Optional. User specified descriptive string for this RestorePlan. |  [optional] |
|**etag** | **String** | Output only. &#x60;etag&#x60; is used for optimistic concurrency control as a way to help prevent simultaneous updates of a restore from overwriting each other. It is strongly suggested that systems make use of the &#x60;etag&#x60; in the read-modify-write cycle to perform restore updates in order to avoid race conditions: An &#x60;etag&#x60; is returned in the response to &#x60;GetRestorePlan&#x60;, and systems are expected to put that etag in the request to &#x60;UpdateRestorePlan&#x60; or &#x60;DeleteRestorePlan&#x60; to ensure that their change will be applied to the same version of the resource. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | Optional. A set of custom labels supplied by user. |  [optional] |
|**name** | **String** | Output only. The full name of the RestorePlan resource. Format: &#x60;projects/_*_/locations/_*_/restorePlans/_*&#x60;. |  [optional] [readonly] |
|**restoreConfig** | [**RestoreConfig**](RestoreConfig.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the RestorePlan. This State field reflects the various stages a RestorePlan can be in during the Create operation. |  [optional] [readonly] |
|**stateReason** | **String** | Output only. Human-readable description of why RestorePlan is in the current &#x60;state&#x60; |  [optional] [readonly] |
|**uid** | **String** | Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The timestamp when this RestorePlan resource was last updated. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CLUSTER_PENDING | &quot;CLUSTER_PENDING&quot; |
| READY | &quot;READY&quot; |
| FAILED | &quot;FAILED&quot; |
| DELETING | &quot;DELETING&quot; |



