

# Snapshot

Represents a snapshot of a job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**creationTime** | **String** | The time this snapshot was created. |  [optional] |
|**description** | **String** | User specified description of the snapshot. Maybe empty. |  [optional] |
|**diskSizeBytes** | **String** | The disk byte size of the snapshot. Only available for snapshots in READY state. |  [optional] |
|**id** | **String** | The unique ID of this snapshot. |  [optional] |
|**projectId** | **String** | The project this snapshot belongs to. |  [optional] |
|**pubsubMetadata** | [**List&lt;PubsubSnapshotMetadata&gt;**](PubsubSnapshotMetadata.md) | Pub/Sub snapshot metadata. |  [optional] |
|**region** | **String** | Cloud region where this snapshot lives in, e.g., \&quot;us-central1\&quot;. |  [optional] |
|**sourceJobId** | **String** | The job this snapshot was created from. |  [optional] |
|**state** | [**StateEnum**](#StateEnum) | State of the snapshot. |  [optional] |
|**ttl** | **String** | The time after which this snapshot will be automatically deleted. |  [optional] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| UNKNOWN_SNAPSHOT_STATE | &quot;UNKNOWN_SNAPSHOT_STATE&quot; |
| PENDING | &quot;PENDING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| READY | &quot;READY&quot; |
| FAILED | &quot;FAILED&quot; |
| DELETED | &quot;DELETED&quot; |



