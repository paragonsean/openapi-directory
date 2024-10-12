

# SnapshotSummary


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**date** | **OffsetDateTime** | Time at which the snapshot was taken. |  |
|**id** | **String** | ID of the snapshot. |  |
|**isCustomRetentionApplied** | **Boolean** | A Boolean value that indicates whether custom retention is applied to the specified snapshot. Value is true when custom retention is applied to the snapshot.  |  |
|**isRetentionLockApplied** | **Boolean** | Indicates whether the snapshot is protected by a Retention Locked SLA Domain.  |  |
|**snapshotRetentionInfo** | [**SnapshotRetentionInfo**](SnapshotRetentionInfo.md) |  |  |
|**snapshotType** | **UnmanagedSnapshotType** |  |  |



