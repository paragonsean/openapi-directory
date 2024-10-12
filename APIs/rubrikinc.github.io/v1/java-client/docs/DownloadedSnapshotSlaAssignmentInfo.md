

# DownloadedSnapshotSlaAssignmentInfo


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**objectId** | **String** | The managed ID of the object that owns the downloaded snapshots in the provided list. |  |
|**slaDomainId** | **String** | The ID of the SLA Domain to assign to the provided list of downloaded snapshots. |  |
|**snapshotIds** | **List&lt;String&gt;** | A list of snapshot IDs. The SLA Domain manages retention for the downloaded copy of the snapshots assigned to the snapshot IDs. If a snapshot in the list has no downloaded copy, its retention period remains unchanged. |  |



