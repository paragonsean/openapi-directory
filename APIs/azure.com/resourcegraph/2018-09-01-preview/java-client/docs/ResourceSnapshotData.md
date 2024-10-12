

# ResourceSnapshotData

Data on a specific resource snapshot.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**content** | **Object** | The resource snapshot content (in resourceChangeDetails response only). |  [optional] |
|**timestamp** | **OffsetDateTime** | The time when the snapshot was created. The snapshot timestamp provides an approximation as to when a modification to a resource was detected.  There can be a difference between the actual modification time and the detection time.  This is due to differences in how operations that modify a resource are processed, versus how operation that record resource snapshots are processed. |  |



