# CloudFilestoreApi.Snapshot

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**createTime** | **String** | Output only. The time when the snapshot was created. | [optional] [readonly] 
**description** | **String** | A description of the snapshot with 2048 characters or less. Requests with longer descriptions will be rejected. | [optional] 
**filesystemUsedBytes** | **String** | Output only. The amount of bytes needed to allocate a full copy of the snapshot content | [optional] [readonly] 
**labels** | **{String: String}** | Resource labels to represent user provided metadata. | [optional] 
**name** | **String** | Output only. The resource name of the snapshot, in the format &#x60;projects/{project_id}/locations/{location_id}/instances/{instance_id}/snapshots/{snapshot_id}&#x60;. | [optional] [readonly] 
**state** | **String** | Output only. The snapshot state. | [optional] [readonly] 



## Enum: StateEnum


* `STATE_UNSPECIFIED` (value: `"STATE_UNSPECIFIED"`)

* `CREATING` (value: `"CREATING"`)

* `READY` (value: `"READY"`)

* `DELETING` (value: `"DELETING"`)




