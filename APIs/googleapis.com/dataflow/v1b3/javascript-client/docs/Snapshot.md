# DataflowApi.Snapshot

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**creationTime** | **String** | The time this snapshot was created. | [optional] 
**description** | **String** | User specified description of the snapshot. Maybe empty. | [optional] 
**diskSizeBytes** | **String** | The disk byte size of the snapshot. Only available for snapshots in READY state. | [optional] 
**id** | **String** | The unique ID of this snapshot. | [optional] 
**projectId** | **String** | The project this snapshot belongs to. | [optional] 
**pubsubMetadata** | [**[PubsubSnapshotMetadata]**](PubsubSnapshotMetadata.md) | Pub/Sub snapshot metadata. | [optional] 
**region** | **String** | Cloud region where this snapshot lives in, e.g., \&quot;us-central1\&quot;. | [optional] 
**sourceJobId** | **String** | The job this snapshot was created from. | [optional] 
**state** | **String** | State of the snapshot. | [optional] 
**ttl** | **String** | The time after which this snapshot will be automatically deleted. | [optional] 



## Enum: StateEnum


* `UNKNOWN_SNAPSHOT_STATE` (value: `"UNKNOWN_SNAPSHOT_STATE"`)

* `PENDING` (value: `"PENDING"`)

* `RUNNING` (value: `"RUNNING"`)

* `READY` (value: `"READY"`)

* `FAILED` (value: `"FAILED"`)

* `DELETED` (value: `"DELETED"`)




