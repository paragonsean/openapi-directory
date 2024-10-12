

# BackupProgressInfo

Describes the progress of a partition's backup.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**backupId** | **UUID** | Unique ID of the newly created backup. |  [optional] |
|**backupLocation** | **String** | Location, relative to the backup store, of the newly created backup. |  [optional] |
|**backupState** | **BackupState** |  |  [optional] |
|**epochOfLastBackupRecord** | [**BackupEpoch**](BackupEpoch.md) |  |  [optional] |
|**failureError** | [**FabricErrorError**](FabricErrorError.md) |  |  [optional] |
|**lsnOfLastBackupRecord** | **String** | The LSN of last record included in backup. |  [optional] |
|**timeStampUtc** | **OffsetDateTime** | TimeStamp in UTC when operation succeeded or failed. |  [optional] |



