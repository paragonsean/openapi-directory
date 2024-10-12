# ServiceFabricClientApis.GetBackupByStorageQueryDescription

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupEntity** | [**BackupEntity**](BackupEntity.md) |  | 
**endDateTimeFilter** | **Date** | Specifies the end date time in ISO8601 till which to enumerate backups. If not specified, backups are enumerated till the end. | [optional] 
**latest** | **Boolean** | If specified as true, gets the most recent backup (within the specified time range) for every partition under the specified backup entity. | [optional] [default to false]
**startDateTimeFilter** | **Date** | Specifies the start date time in ISO8601 from which to enumerate backups. If not specified, backups are enumerated from the beginning. | [optional] 
**storage** | [**BackupStorageDescription**](BackupStorageDescription.md) |  | 


