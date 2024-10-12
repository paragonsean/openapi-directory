# CloudFilestoreApi.Backup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacityGb** | **String** | Output only. Capacity of the source file share when the backup was created. | [optional] [readonly] 
**createTime** | **String** | Output only. The time when the backup was created. | [optional] [readonly] 
**description** | **String** | A description of the backup with 2048 characters or less. Requests with longer descriptions will be rejected. | [optional] 
**downloadBytes** | **String** | Output only. Amount of bytes that will be downloaded if the backup is restored | [optional] [readonly] 
**kmsKeyName** | **String** | Immutable. KMS key name used for data encryption. | [optional] 
**labels** | **{String: String}** | Resource labels to represent user provided metadata. | [optional] 
**name** | **String** | Output only. The resource name of the backup, in the format &#x60;projects/{project_id}/locations/{location_id}/backups/{backup_id}&#x60;. | [optional] [readonly] 
**satisfiesPzi** | **Boolean** | Output only. Reserved for future use. | [optional] [readonly] 
**satisfiesPzs** | **Boolean** | Output only. Reserved for future use. | [optional] [readonly] 
**sourceFileShare** | **String** | Name of the file share in the source Filestore instance that the backup is created from. | [optional] 
**sourceInstance** | **String** | The resource name of the source Filestore instance, in the format &#x60;projects/{project_id}/locations/{location_id}/instances/{instance_id}&#x60;, used to create this backup. | [optional] 
**sourceInstanceTier** | **String** | Output only. The service tier of the source Filestore instance that this backup is created from. | [optional] [readonly] 
**state** | **String** | Output only. The backup state. | [optional] [readonly] 
**storageBytes** | **String** | Output only. The size of the storage used by the backup. As backups share storage, this number is expected to change with backup creation/deletion. | [optional] [readonly] 



## Enum: SourceInstanceTierEnum


* `TIER_UNSPECIFIED` (value: `"TIER_UNSPECIFIED"`)

* `STANDARD` (value: `"STANDARD"`)

* `PREMIUM` (value: `"PREMIUM"`)

* `BASIC_HDD` (value: `"BASIC_HDD"`)

* `BASIC_SSD` (value: `"BASIC_SSD"`)

* `HIGH_SCALE_SSD` (value: `"HIGH_SCALE_SSD"`)

* `ENTERPRISE` (value: `"ENTERPRISE"`)

* `ZONAL` (value: `"ZONAL"`)

* `REGIONAL` (value: `"REGIONAL"`)





## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `FINALIZING` (value: `"FINALIZING"`)

* `READY` (value: `"READY"`)

* `DELETING` (value: `"DELETING"`)

* `INVALID` (value: `"INVALID"`)




