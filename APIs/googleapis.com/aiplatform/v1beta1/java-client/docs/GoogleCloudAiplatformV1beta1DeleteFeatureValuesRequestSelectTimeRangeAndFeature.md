

# GoogleCloudAiplatformV1beta1DeleteFeatureValuesRequestSelectTimeRangeAndFeature

Message to select time range and feature. Values of the selected feature generated within an inclusive time range will be deleted. Using this option permanently deletes the feature values from the specified feature IDs within the specified time range. This might include data from the online storage. If you want to retain any deleted historical data in the online storage, you must re-ingest it.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**featureSelector** | [**GoogleCloudAiplatformV1beta1FeatureSelector**](GoogleCloudAiplatformV1beta1FeatureSelector.md) |  |  [optional] |
|**skipOnlineStorageDelete** | **Boolean** | If set, data will not be deleted from online storage. When time range is older than the data in online storage, setting this to be true will make the deletion have no impact on online serving. |  [optional] |
|**timeRange** | [**GoogleTypeInterval**](GoogleTypeInterval.md) |  |  [optional] |



