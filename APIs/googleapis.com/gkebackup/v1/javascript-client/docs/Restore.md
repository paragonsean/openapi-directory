# BackupForGkeApi.Restore

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backup** | **String** | Required. Immutable. A reference to the Backup used as the source from which this Restore will restore. Note that this Backup must be a sub-resource of the RestorePlan&#39;s backup_plan. Format: &#x60;projects/_*_/locations/_*_/backupPlans/_*_/backups/_*&#x60;. | [optional] 
**cluster** | **String** | Output only. The target cluster into which this Restore will restore data. Valid formats: - &#x60;projects/_*_/locations/_*_/clusters/_*&#x60; - &#x60;projects/_*_/zones/_*_/clusters/_*&#x60; Inherited from parent RestorePlan&#39;s cluster value. | [optional] [readonly] 
**completeTime** | **String** | Output only. Timestamp of when the restore operation completed. | [optional] [readonly] 
**createTime** | **String** | Output only. The timestamp when this Restore resource was created. | [optional] [readonly] 
**description** | **String** | User specified descriptive string for this Restore. | [optional] 
**etag** | **String** | Output only. &#x60;etag&#x60; is used for optimistic concurrency control as a way to help prevent simultaneous updates of a restore from overwriting each other. It is strongly suggested that systems make use of the &#x60;etag&#x60; in the read-modify-write cycle to perform restore updates in order to avoid race conditions: An &#x60;etag&#x60; is returned in the response to &#x60;GetRestore&#x60;, and systems are expected to put that etag in the request to &#x60;UpdateRestore&#x60; or &#x60;DeleteRestore&#x60; to ensure that their change will be applied to the same version of the resource. | [optional] [readonly] 
**labels** | **{String: String}** | A set of custom labels supplied by user. | [optional] 
**name** | **String** | Output only. The full name of the Restore resource. Format: &#x60;projects/_*_/locations/_*_/restorePlans/_*_/restores/_*&#x60; | [optional] [readonly] 
**resourcesExcludedCount** | **Number** | Output only. Number of resources excluded during the restore execution. | [optional] [readonly] 
**resourcesFailedCount** | **Number** | Output only. Number of resources that failed to be restored during the restore execution. | [optional] [readonly] 
**resourcesRestoredCount** | **Number** | Output only. Number of resources restored during the restore execution. | [optional] [readonly] 
**restoreConfig** | [**RestoreConfig**](RestoreConfig.md) |  | [optional] 
**state** | **String** | Output only. The current state of the Restore. | [optional] [readonly] 
**stateReason** | **String** | Output only. Human-readable description of why the Restore is in its current state. | [optional] [readonly] 
**uid** | **String** | Output only. Server generated global unique identifier of [UUID](https://en.wikipedia.org/wiki/Universally_unique_identifier) format. | [optional] [readonly] 
**updateTime** | **String** | Output only. The timestamp when this Restore resource was last updated. | [optional] [readonly] 
**volumesRestoredCount** | **Number** | Output only. Number of volumes restored during the restore execution. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `IN_PROGRESS` (value: `"IN_PROGRESS"`)

* `SUCCEEDED` (value: `"SUCCEEDED"`)

* `FAILED` (value: `"FAILED"`)

* `DELETING` (value: `"DELETING"`)




