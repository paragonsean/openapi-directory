

# Snapshot

A Filestore snapshot.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**createTime** | **String** | Output only. The time when the snapshot was created. |  [optional] [readonly] |
|**description** | **String** | A description of the snapshot with 2048 characters or less. Requests with longer descriptions will be rejected. |  [optional] |
|**filesystemUsedBytes** | **String** | Output only. The amount of bytes needed to allocate a full copy of the snapshot content |  [optional] [readonly] |
|**labels** | **Map&lt;String, String&gt;** | Resource labels to represent user provided metadata. |  [optional] |
|**name** | **String** | Output only. The resource name of the snapshot, in the format &#x60;projects/{project_id}/locations/{location_id}/instances/{instance_id}/snapshots/{snapshot_id}&#x60;. |  [optional] [readonly] |
|**state** | [**StateEnum**](#StateEnum) | Output only. The snapshot state. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| STATE_UNSPECIFIED | &quot;STATE_UNSPECIFIED&quot; |
| CREATING | &quot;CREATING&quot; |
| READY | &quot;READY&quot; |
| DELETING | &quot;DELETING&quot; |



