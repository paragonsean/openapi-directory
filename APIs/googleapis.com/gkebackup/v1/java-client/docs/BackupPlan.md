

# BackupPlan

Defines the configuration and scheduling for a \"line\" of Backups.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupConfig** | [**BackupConfig**](BackupConfig.md) |  |  [optional] |
|**backupSchedule** | [**Schedule**](Schedule.md) |  |  [optional] |
|**cluster** | **String** | Required. Immutable. The source cluster from which Backups will be created via this BackupPlan. Valid formats: - &#x60;projects/_*_/locations/_*_/clusters/_*&#x60; - &#x60;projects/_*_/zones/_*_/clusters/_*&#x60; |  [optional] |
|**createTime** | **String** | Output only. The timestamp when this BackupPlan resource was created. |  [optional] [readonly] |
|**deactivated** | **Boolean** | Optional. This flag indicates whether this BackupPlan has been deactivated. Setting this field to True locks the BackupPlan such that no further updates will be allowed (except deletes), including the deactivated field itself. It also prevents any new Backups from being created via this BackupPlan (including scheduled Backups). Default: False |  [optional] |
|**description** | **String** | Optional. User specified descriptive string for this BackupPlan. |  [optional] |
|**etag** | **String** | Output only. &#x60;etag&#x60; is used for optimistic concurrency control as a way to help prevent simultaneous updates of a backup plan from overwriting each other. It is strongly suggested that systems make use of the &#39;etag&#39; in the read-modify-write cycle to perform BackupPlan updates in order to avoid race conditions: An &#x60;etag&#x60; is returned in the response to &#x60;GetBackupPlan&#x60;, and systems are expected to put that etag in the request to &#x60;UpdateBackupPlan&#x60; or &#x60;DeleteBackupPlan&#x60; to ensure that their change will be applied to the same version of the resource. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | Optional. A set of custom labels supplied by user. |  [optional] |
|**name** | **String** | Output only. The full name of the BackupPlan resource. Format: &#x60;projects/_*_/locations/_*_/backupPlans/_*&#x60; |  [optional] [readonly] |
|**protectedPodCount** | **Integer** | Output only. The number of Kubernetes Pods backed up in the last successful Backup created via this BackupPlan. |  [optional] [readonly] |
|**retentionPolicy** | [**RetentionPolicy**](RetentionPolicy.md) |  |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | Output only. State of the BackupPlan. This State field reflects the various stages a BackupPlan can be in during the Create operation. It will be set to \&quot;DEACTIVATED\&quot; if the BackupPlan is deactivated on an Update |  [optional] [readonly] |
|**stateReason** | **String** | Output only. Human-readable description of why BackupPlan is in the current &#x60;state&#x60; |  [optional] [readonly] |
|**uid** | **String** | Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format. |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The timestamp when this BackupPlan resource was last updated. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CLUSTER_PENDING | &quot;CLUSTER_PENDING&quot; |
| PROVISIONING | &quot;PROVISIONING&quot; |
| READY | &quot;READY&quot; |
| FAILED | &quot;FAILED&quot; |
| DEACTIVATED | &quot;DEACTIVATED&quot; |
| DELETING | &quot;DELETING&quot; |



