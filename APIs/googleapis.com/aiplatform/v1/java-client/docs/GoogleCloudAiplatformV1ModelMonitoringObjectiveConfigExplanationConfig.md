

# GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigExplanationConfig

The config for integrating with Vertex Explainable AI. Only applicable if the Model has explanation_spec populated.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**enableFeatureAttributes** | **Boolean** | If want to analyze the Vertex Explainable AI feature attribute scores or not. If set to true, Vertex AI will log the feature attributions from explain response and do the skew/drift detection for them. |  [optional] |
|**explanationBaseline** | [**GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigExplanationConfigExplanationBaseline**](GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigExplanationConfigExplanationBaseline.md) |  |  [optional] |



