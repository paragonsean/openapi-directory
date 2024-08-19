

# GoogleCloudAiplatformV1ExplanationMetadataOverride

The ExplanationMetadata entries that can be overridden at online explanation time.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**inputs** | [**Map&lt;String, GoogleCloudAiplatformV1ExplanationMetadataOverrideInputMetadataOverride&gt;**](GoogleCloudAiplatformV1ExplanationMetadataOverrideInputMetadataOverride.md) | Required. Overrides the input metadata of the features. The key is the name of the feature to be overridden. The keys specified here must exist in the input metadata to be overridden. If a feature is not specified here, the corresponding feature&#39;s input metadata is not overridden. |  [optional] |



