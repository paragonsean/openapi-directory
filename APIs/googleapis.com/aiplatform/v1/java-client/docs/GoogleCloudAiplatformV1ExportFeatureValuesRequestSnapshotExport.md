

# GoogleCloudAiplatformV1ExportFeatureValuesRequestSnapshotExport

Describes exporting the latest Feature values of all entities of the EntityType between [start_time, snapshot_time].

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**snapshotTime** | **String** | Exports Feature values as of this timestamp. If not set, retrieve values as of now. Timestamp, if present, must not have higher than millisecond precision. |  [optional] |
|**startTime** | **String** | Excludes Feature values with feature generation timestamp before this timestamp. If not set, retrieve oldest values kept in Feature Store. Timestamp, if present, must not have higher than millisecond precision. |  [optional] |



