# LinodeApi.Backup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**available** | **Boolean** | Whether this Backup is available for restoration.  Backups undergoing maintenance are not available for restoration.  | [optional] [readonly] 
**configs** | **[String]** | A list of the labels of the Configuration profiles that are part of the Backup.  | [optional] [readonly] 
**created** | **Date** | The date the Backup was taken. | [optional] [readonly] 
**disks** | [**[BackupDisksInner]**](BackupDisksInner.md) | A list of the disks that are part of the Backup.  | [optional] [readonly] 
**finished** | **Date** | The date the Backup completed. | [optional] [readonly] 
**id** | **Number** | The unique ID of this Backup. | [optional] [readonly] 
**label** | **String** | A label for Backups that are of type &#x60;snapshot&#x60;. | [optional] 
**status** | **String** | The current state of a specific Backup. | [optional] [readonly] 
**type** | **String** | This indicates whether the Backup is an automatic Backup or manual snapshot taken by the User at a specific point in time.  | [optional] [readonly] 
**updated** | **Date** | The date the Backup was most recently updated. | [optional] [readonly] 



## Enum: StatusEnum


* `paused` (value: `"paused"`)

* `pending` (value: `"pending"`)

* `running` (value: `"running"`)

* `needsPostProcessing` (value: `"needsPostProcessing"`)

* `successful` (value: `"successful"`)

* `failed` (value: `"failed"`)

* `userAborted` (value: `"userAborted"`)





## Enum: TypeEnum


* `auto` (value: `"auto"`)

* `snapshot` (value: `"snapshot"`)




