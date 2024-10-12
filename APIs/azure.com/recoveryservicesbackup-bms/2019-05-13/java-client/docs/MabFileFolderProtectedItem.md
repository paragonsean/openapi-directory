

# MabFileFolderProtectedItem

MAB workload-specific backup item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**computerName** | **String** | Name of the computer associated with this backup item. |  [optional] |
|**deferredDeleteSyncTimeInUTC** | **Long** | Sync time for deferred deletion in UTC |  [optional] |
|**extendedInfo** | [**MabFileFolderProtectedItemExtendedInfo**](MabFileFolderProtectedItemExtendedInfo.md) |  |  [optional] |
|**friendlyName** | **String** | Friendly name of this backup item. |  [optional] |
|**lastBackupStatus** | **String** | Status of last backup operation. |  [optional] |
|**lastBackupTime** | **OffsetDateTime** | Timestamp of the last backup operation on this backup item. |  [optional] |
|**protectionState** | **String** | Protected, ProtectionStopped, IRPending or ProtectionError |  [optional] |



