# StorSimple8000SeriesManagementClient.BackupPolicyProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupPolicyCreationType** | **String** | The backup policy creation type. Indicates whether this was created through SaaS or through StorSimple Snapshot Manager. | [optional] [readonly] 
**lastBackupTime** | **Date** | The time of the last backup for the backup policy. | [optional] [readonly] 
**nextBackupTime** | **Date** | The time of the next backup for the backup policy. | [optional] [readonly] 
**scheduledBackupStatus** | **String** | Indicates whether at least one of the schedules in the backup policy is active or not. | [optional] [readonly] 
**schedulesCount** | **Number** | The count of schedules the backup policy contains. | [optional] [readonly] 
**ssmHostName** | **String** | If the backup policy was created by StorSimple Snapshot Manager, then this field indicates the hostname of the StorSimple Snapshot Manager. | [optional] [readonly] 
**volumeIds** | **[String]** | The path IDs of the volumes which are part of the backup policy. | 



## Enum: BackupPolicyCreationTypeEnum


* `BySaaS` (value: `"BySaaS"`)

* `BySSM` (value: `"BySSM"`)





## Enum: ScheduledBackupStatusEnum


* `Disabled` (value: `"Disabled"`)

* `Enabled` (value: `"Enabled"`)




