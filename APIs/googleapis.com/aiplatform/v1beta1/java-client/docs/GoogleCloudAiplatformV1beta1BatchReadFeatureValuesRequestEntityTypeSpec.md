

# GoogleCloudAiplatformV1beta1BatchReadFeatureValuesRequestEntityTypeSpec

Selects Features of an EntityType to read values of and specifies read settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**entityTypeId** | **String** | Required. ID of the EntityType to select Features. The EntityType id is the entity_type_id specified during EntityType creation. |  [optional] |
|**featureSelector** | [**GoogleCloudAiplatformV1beta1FeatureSelector**](GoogleCloudAiplatformV1beta1FeatureSelector.md) |  |  [optional] |
|**settings** | [**List&lt;GoogleCloudAiplatformV1beta1DestinationFeatureSetting&gt;**](GoogleCloudAiplatformV1beta1DestinationFeatureSetting.md) | Per-Feature settings for the batch read. |  [optional] |



