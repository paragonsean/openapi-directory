# RubrikRestApi.MssqlBackup

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupId** | **String** | The unique identifier for the object. | 
**backupSize** | **Number** | The total uncompressed size of the files in bytes. | 
**backupType** | [**MssqlBackupType**](MssqlBackupType.md) |  | 
**date** | **Date** | Timestamp of the backup. | 
**lsn** | **String** | LSN of the backup. | 
**path** | **String** | The file path the backup will be stored at in downloaded zip files containing it. | 
**recoveryForkGuid** | **String** | GUID of the recovery fork attached to the LSN. | 


