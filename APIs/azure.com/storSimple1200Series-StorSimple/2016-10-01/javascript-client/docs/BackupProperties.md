# StorSimpleManagementClient.BackupProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createdTime** | **Date** | The time when the backup was created. | [optional] 
**deviceId** | **String** | The Device Identifier. | 
**elements** | [**[BackupElement]**](BackupElement.md) | The backup elements. | 
**expirationTime** | **Date** | The time when the backup will expire. | [optional] 
**initiatedBy** | **String** | Indicates how the backup was initiated \&quot;Manual | Scheduled\&quot;. | 
**sizeInBytes** | **Number** | The backup size in bytes. | 
**targetId** | **String** | The path id of the target FileServer or IscsiServer for which the backup was taken. | [optional] 
**targetType** | **String** | Type of target, FileServer or IscsiServer | [optional] 



## Enum: InitiatedByEnum


* `Manual` (value: `"Manual"`)

* `Scheduled` (value: `"Scheduled"`)




