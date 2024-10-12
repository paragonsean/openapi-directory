# ServiceFabricClientApis.BackupPolicyDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**autoRestoreOnDataLoss** | **Boolean** | Specifies whether to trigger restore automatically using the latest available backup in case the partition experiences a data loss event. | 
**maxIncrementalBackups** | **Number** | Defines the maximum number of incremental backups to be taken between two full backups. This is just the upper limit. A full backup may be taken before specified number of incremental backups are completed in one of the following conditions - The replica has never taken a full backup since it has become primary, - Some of the log records since the last backup has been truncated, or - Replica passed the MaxAccumulatedBackupLogSizeInMB limit. | 
**name** | **String** | The unique name identifying this backup policy. | 
**schedule** | [**BackupScheduleDescription**](BackupScheduleDescription.md) |  | 
**storage** | [**BackupStorageDescription**](BackupStorageDescription.md) |  | 


