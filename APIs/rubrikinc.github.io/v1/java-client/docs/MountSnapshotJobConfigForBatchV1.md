

# MountSnapshotJobConfigForBatchV1


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**config** | [**MountSnapshotJobConfigV1**](MountSnapshotJobConfigV1.md) |  |  |
|**snapshotAfterDate** | **OffsetDateTime** | Mounts the oldest snapshot taken after the specified date. This parameter is only evaluated when no values are set for snapshotId and snapshotBeforeDate. |  [optional] |
|**snapshotBeforeDate** | **OffsetDateTime** | Mounts the most recent snapshot taken prior to the specified date. This parameter is only evaluated when no value is set for snapshotId. |  [optional] |
|**snapshotId** | **String** | The ID of the snapshot to export. This parameter is optional if either of the &#x60;snapshotBeforeDate&#x60; or &#x60;snapshotAfterDate&#x60; parameters is configured. |  [optional] |
|**vmId** | **String** | ID of the virtual machine whose snapshot needs to be mounted. |  |



