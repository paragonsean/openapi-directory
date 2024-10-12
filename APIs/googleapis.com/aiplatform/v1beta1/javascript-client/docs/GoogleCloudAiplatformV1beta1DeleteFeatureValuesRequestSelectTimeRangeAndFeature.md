# VertexAiApi.GoogleCloudAiplatformV1beta1DeleteFeatureValuesRequestSelectTimeRangeAndFeature

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**featureSelector** | [**GoogleCloudAiplatformV1beta1FeatureSelector**](GoogleCloudAiplatformV1beta1FeatureSelector.md) |  | [optional] 
**skipOnlineStorageDelete** | **Boolean** | If set, data will not be deleted from online storage. When time range is older than the data in online storage, setting this to be true will make the deletion have no impact on online serving. | [optional] 
**timeRange** | [**GoogleTypeInterval**](GoogleTypeInterval.md) |  | [optional] 


