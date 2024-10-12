# ServiceFabricClientApis.BackupProgressInfo

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backupId** | **String** | Unique ID of the newly created backup. | [optional] 
**backupLocation** | **String** | Location, relative to the backup store, of the newly created backup. | [optional] 
**backupState** | [**BackupState**](BackupState.md) |  | [optional] 
**epochOfLastBackupRecord** | [**Epoch**](Epoch.md) |  | [optional] 
**failureError** | [**FabricErrorError**](FabricErrorError.md) |  | [optional] 
**lsnOfLastBackupRecord** | **String** | The LSN of last record included in backup. | [optional] 
**timeStampUtc** | **Date** | TimeStamp in UTC when operation succeeded or failed. | [optional] 


