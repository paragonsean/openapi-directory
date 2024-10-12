

# SyncWorkspaceResponse

A response after synchronizing the workspace to the latest container version.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**mergeConflict** | [**List&lt;MergeConflict&gt;**](MergeConflict.md) | The merge conflict after sync. If this field is not empty, the sync is still treated as successful. But a version cannot be created until all conflicts are resolved. |  [optional] |
|**syncStatus** | [**SyncStatus**](SyncStatus.md) |  |  [optional] |



