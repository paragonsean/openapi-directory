

# GoogleCloudAiplatformV1beta1ExportFeatureValuesRequestFullExport

Describes exporting all historical Feature values of all entities of the EntityType between [start_time, end_time].

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **String** | Exports Feature values as of this timestamp. If not set, retrieve values as of now. Timestamp, if present, must not have higher than millisecond precision. |  [optional] |
|**startTime** | **String** | Excludes Feature values with feature generation timestamp before this timestamp. If not set, retrieve oldest values kept in Feature Store. Timestamp, if present, must not have higher than millisecond precision. |  [optional] |



