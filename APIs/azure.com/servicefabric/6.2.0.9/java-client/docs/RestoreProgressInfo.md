

# RestoreProgressInfo

Describes the progress of a restore operation on a partition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**failureError** | [**FabricErrorError**](FabricErrorError.md) |  |  [optional] |
|**restoreState** | **RestoreState** |  |  [optional] |
|**restoredEpoch** | [**BackupEpoch**](BackupEpoch.md) |  |  [optional] |
|**restoredLsn** | **String** | Restored LSN. |  [optional] |
|**timeStampUtc** | **OffsetDateTime** | Timestamp when operation succeeded or failed. |  [optional] |



