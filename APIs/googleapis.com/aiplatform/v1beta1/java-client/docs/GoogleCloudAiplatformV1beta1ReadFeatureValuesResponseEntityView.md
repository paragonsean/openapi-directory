

# GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseEntityView

Entity view with Feature values.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | [**List&lt;GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseEntityViewData&gt;**](GoogleCloudAiplatformV1beta1ReadFeatureValuesResponseEntityViewData.md) | Each piece of data holds the k requested values for one requested Feature. If no values for the requested Feature exist, the corresponding cell will be empty. This has the same size and is in the same order as the features from the header ReadFeatureValuesResponse.header. |  [optional] |
|**entityId** | **String** | ID of the requested entity. |  [optional] |



