# VertexAiApi.GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigTrainingPredictionSkewDetectionConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributionScoreSkewThresholds** | [**{String: GoogleCloudAiplatformV1ThresholdConfig}**](GoogleCloudAiplatformV1ThresholdConfig.md) | Key is the feature name and value is the threshold. The threshold here is against attribution score distance between the training and prediction feature. | [optional] 
**defaultSkewThreshold** | [**GoogleCloudAiplatformV1ThresholdConfig**](GoogleCloudAiplatformV1ThresholdConfig.md) |  | [optional] 
**skewThresholds** | [**{String: GoogleCloudAiplatformV1ThresholdConfig}**](GoogleCloudAiplatformV1ThresholdConfig.md) | Key is the feature name and value is the threshold. If a feature needs to be monitored for skew, a value threshold must be configured for that feature. The threshold here is against feature distribution distance between the training and prediction feature. | [optional] 


