

# Backup

Represents a request to perform a single point-in-time capture of some portion of the state of a GKE cluster, the record of the backup operation itself, and an anchor for the underlying artifacts that comprise the Backup (the config backup and VolumeBackups). Next id: 29

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allNamespaces** | **Boolean** | Output only. If True, all namespaces were included in the Backup. |  [optional] [readonly] |
|**clusterMetadata** | [**ClusterMetadata**](ClusterMetadata.md) |  |  [optional] |
|**completeTime** | **String** | Output only. Completion time of the Backup |  [optional] [readonly] |
|**configBackupSizeBytes** | **String** | Output only. The size of the config backup in bytes. |  [optional] [readonly] |
|**containsSecrets** | **Boolean** | Output only. Whether or not the Backup contains Kubernetes Secrets. Controlled by the parent BackupPlan&#39;s include_secrets value. |  [optional] [readonly] |
|**containsVolumeData** | **Boolean** | Output only. Whether or not the Backup contains volume data. Controlled by the parent BackupPlan&#39;s include_volume_data value. |  [optional] [readonly] |
|**createTime** | **String** | Output only. The timestamp when this Backup resource was created. |  [optional] [readonly] |
|**deleteLockDays** | **Integer** | Optional. Minimum age for this Backup (in days). If this field is set to a non-zero value, the Backup will be \&quot;locked\&quot; against deletion (either manual or automatic deletion) for the number of days provided (measured from the creation time of the Backup). MUST be an integer value between 0-90 (inclusive). Defaults to parent BackupPlan&#39;s backup_delete_lock_days setting and may only be increased (either at creation time or in a subsequent update). |  [optional] |
|**deleteLockExpireTime** | **String** | Output only. The time at which an existing delete lock will expire for this backup (calculated from create_time + delete_lock_days). |  [optional] [readonly] |
|**description** | **String** | Optional. User specified descriptive string for this Backup. |  [optional] |
|**encryptionKey** | [**EncryptionKey**](EncryptionKey.md) |  |  [optional] |
|**etag** | **String** | Output only. &#x60;etag&#x60; is used for optimistic concurrency control as a way to help prevent simultaneous updates of a backup from overwriting each other. It is strongly suggested that systems make use of the &#x60;etag&#x60; in the read-modify-write cycle to perform backup updates in order to avoid race conditions: An &#x60;etag&#x60; is returned in the response to &#x60;GetBackup&#x60;, and systems are expected to put that etag in the request to &#x60;UpdateBackup&#x60; or &#x60;DeleteBackup&#x60; to ensure that their change will be applied to the same version of the resource. |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | Optional. A set of custom labels supplied by user. |  [optional] |
|**manual** | **Boolean** | Output only. This flag indicates whether this Backup resource was created manually by a user or via a schedule in the BackupPlan. A value of True means that the Backup was created manually. |  [optional] [readonly] |
|**name** | **String** | Output only. The fully qualified name of the Backup. &#x60;projects/_*_/locations/_*_/backupPlans/_*_/backups/_*&#x60; |  [optional] [readonly] |
|**podCount** | **Integer** | Output only. The total number of Kubernetes Pods contained in the Backup. |  [optional] [readonly] |
|**resourceCount** | **Integer** | Output only. The total number of Kubernetes resources included in the Backup. |  [optional] [readonly] |
|**retainDays** | **Integer** | Optional. The age (in days) after which this Backup will be automatically deleted. Must be an integer value &gt;&#x3D; 0: - If 0, no automatic deletion will occur for this Backup. - If not 0, this must be &gt;&#x3D; delete_lock_days and &lt;&#x3D; 365. Once a Backup is created, this value may only be increased. Defaults to the parent BackupPlan&#39;s backup_retain_days value. |  [optional] |
|**retainExpireTime** | **String** | Output only. The time at which this Backup will be automatically deleted (calculated from create_time + retain_days). |  [optional] [readonly] |
|**selectedApplications** | [**NamespacedNames**](NamespacedNames.md) |  |  [optional] |
|**selectedNamespaces** | [**Namespaces**](Namespaces.md) |  |  [optional] |
|**sizeBytes** | **String** | Output only. The total size of the Backup in bytes &#x3D; config backup size + sum(volume backup sizes) |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. Current state of the Backup |  [optional] [readonly] |
|**stateReason** | **String** | Output only. Human-readable description of why the backup is in the current &#x60;state&#x60;. |  [optional] [readonly] |
|**uid** | **String** | Output only. Server generated global unique identifier of [UUID4](https://en.wikipedia.org/wiki/Universally_unique_identifier) |  [optional] [readonly] |
|**updateTime** | **String** | Output only. The timestamp when this Backup resource was last updated. |  [optional] [readonly] |
|**volumeCount** | **Integer** | Output only. The total number of volume backups contained in the Backup. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| IN_PROGRESS | &quot;IN_PROGRESS&quot; |
| SUCCEEDED | &quot;SUCCEEDED&quot; |
| FAILED | &quot;FAILED&quot; |
| DELETING | &quot;DELETING&quot; |



