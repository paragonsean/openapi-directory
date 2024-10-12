

# SyncSessionStatus

Sync Session status object.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**filesNotSyncingErrors** | [**List&lt;FilesNotSyncingError&gt;**](FilesNotSyncingError.md) | Array of per-item errors coming from the last sync session. Reserved for future use. |  [optional] [readonly] |
|**lastSyncPerItemErrorCount** | **Long** | Last sync per item error count. |  [optional] [readonly] |
|**lastSyncResult** | **Integer** | Last sync result (HResult) |  [optional] [readonly] |
|**lastSyncSuccessTimestamp** | **OffsetDateTime** | Last sync success timestamp |  [optional] [readonly] |
|**lastSyncTimestamp** | **OffsetDateTime** | Last sync timestamp |  [optional] [readonly] |
|**persistentFilesNotSyncingCount** | **Long** | Count of persistent files not syncing. Reserved for future use. |  [optional] [readonly] |
|**transientFilesNotSyncingCount** | **Long** | Count of transient files not syncing. Reserved for future use. |  [optional] [readonly] |



