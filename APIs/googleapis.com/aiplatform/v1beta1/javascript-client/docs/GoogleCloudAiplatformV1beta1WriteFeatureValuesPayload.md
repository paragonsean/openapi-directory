# VertexAiApi.GoogleCloudAiplatformV1beta1WriteFeatureValuesPayload

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entityId** | **String** | Required. The ID of the entity. | [optional] 
**featureValues** | [**{String: GoogleCloudAiplatformV1beta1FeatureValue}**](GoogleCloudAiplatformV1beta1FeatureValue.md) | Required. Feature values to be written, mapping from Feature ID to value. Up to 100,000 &#x60;feature_values&#x60; entries may be written across all payloads. The feature generation time, aligned by days, must be no older than five years (1825 days) and no later than one year (366 days) in the future. | [optional] 


