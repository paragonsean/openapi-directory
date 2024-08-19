

# GoogleCloudAiplatformV1CreateFeatureRequest

Request message for FeaturestoreService.CreateFeature. Request message for FeatureRegistryService.CreateFeature.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**feature** | [**GoogleCloudAiplatformV1Feature**](GoogleCloudAiplatformV1Feature.md) |  |  [optional] |
|**featureId** | **String** | Required. The ID to use for the Feature, which will become the final component of the Feature&#39;s resource name. This value may be up to 128 characters, and valid characters are &#x60;[a-z0-9_]&#x60;. The first character cannot be a number. The value must be unique within an EntityType/FeatureGroup. |  [optional] |
|**parent** | **String** | Required. The resource name of the EntityType or FeatureGroup to create a Feature. Format for entity_type as parent: &#x60;projects/{project}/locations/{location}/featurestores/{featurestore}/entityTypes/{entity_type}&#x60; Format for feature_group as parent: &#x60;projects/{project}/locations/{location}/featureGroups/{feature_group}&#x60; |  [optional] |



