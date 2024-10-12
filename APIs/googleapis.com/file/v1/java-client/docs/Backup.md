

# Backup

A Filestore backup.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**capacityGb** | **String** | Output only. Capacity of the source file share when the backup was created. |  [optional] [readonly] |
|**createTime** | **String** | Output only. The time when the backup was created. |  [optional] [readonly] |
|**description** | **String** | A description of the backup with 2048 characters or less. Requests with longer descriptions will be rejected. |  [optional] |
|**downloadBytes** | **String** | Output only. Amount of bytes that will be downloaded if the backup is restored. This may be different than storage bytes, since sequential backups of the same disk will share storage. |  [optional] [readonly] |
|**kmsKey** | **String** | Immutable. KMS key name used for data encryption. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Resource labels to represent user provided metadata. |  [optional] |
|**name** | **String** | Output only. The resource name of the backup, in the format &#x60;projects/{project_number}/locations/{location_id}/backups/{backup_id}&#x60;. |  [optional] [readonly] |
|**satisfiesPzi** | **Boolean** | Output only. Reserved for future use. |  [optional] [readonly] |
|**satisfiesPzs** | **Boolean** | Output only. Reserved for future use. |  [optional] [readonly] |
|**sourceFileShare** | **String** | Name of the file share in the source Filestore instance that the backup is created from. |  [optional] |
|**sourceInstance** | **String** | The resource name of the source Filestore instance, in the format &#x60;projects/{project_number}/locations/{location_id}/instances/{instance_id}&#x60;, used to create this backup. |  [optional] |
|**sourceInstanceTier** | [**SourceInstanceTierEnum**](#SourceInstanceTierEnum) | Output only. The service tier of the source Filestore instance that this backup is created from. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The backup state. |  [optional] [readonly] |
|**storageBytes** | **String** | Output only. The size of the storage used by the backup. As backups share storage, this number is expected to change with backup creation/deletion. |  [optional] [readonly] |



## Enum: SourceInstanceTierEnum

| Name | Value |
|---- | -----|
| TIER_UNSPECIFIED | &quot;TIER_UNSPECIFIED&quot; |
| STANDARD | &quot;STANDARD&quot; |
| PREMIUM | &quot;PREMIUM&quot; |
| BASIC_HDD | &quot;BASIC_HDD&quot; |
| BASIC_SSD | &quot;BASIC_SSD&quot; |
| HIGH_SCALE_SSD | &quot;HIGH_SCALE_SSD&quot; |
| ENTERPRISE | &quot;ENTERPRISE&quot; |
| ZONAL | &quot;ZONAL&quot; |
| REGIONAL | &quot;REGIONAL&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| FINALIZING | &quot;FINALIZING&quot; |
| READY | &quot;READY&quot; |
| DELETING | &quot;DELETING&quot; |
| INVALID | &quot;INVALID&quot; |



