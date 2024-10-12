# StorSimple8000SeriesManagementClient.BackupProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupJobCreationType** | **String** | The backup job creation type. | [optional] 
**backupPolicyId** | **String** | The path ID of the backup policy. | [optional] 
**backupType** | **String** | The type of the backup. | [optional] 
**createdOn** | **Date** | The time when the backup was created. | 
**elements** | [**[BackupElement]**](BackupElement.md) | The backup elements. | 
**sizeInBytes** | **Number** | The backup size in bytes. | 
**ssmHostName** | **String** | The StorSimple Snapshot Manager host name. | [optional] 



## Enum: BackupJobCreationTypeEnum


* `Adhoc` (value: `"Adhoc"`)

* `BySchedule` (value: `"BySchedule"`)

* `BySSM` (value: `"BySSM"`)





## Enum: BackupTypeEnum


* `LocalSnapshot` (value: `"LocalSnapshot"`)

* `CloudSnapshot` (value: `"CloudSnapshot"`)




