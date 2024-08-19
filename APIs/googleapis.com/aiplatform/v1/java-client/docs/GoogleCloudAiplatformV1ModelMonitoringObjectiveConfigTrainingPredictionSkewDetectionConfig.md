

# GoogleCloudAiplatformV1ModelMonitoringObjectiveConfigTrainingPredictionSkewDetectionConfig

The config for Training & Prediction data skew detection. It specifies the training dataset sources and the skew detection parameters.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributionScoreSkewThresholds** | [**Map&lt;String, GoogleCloudAiplatformV1ThresholdConfig&gt;**](GoogleCloudAiplatformV1ThresholdConfig.md) | Key is the feature name and value is the threshold. The threshold here is against attribution score distance between the training and prediction feature. |  [optional] |
|**defaultSkewThreshold** | [**GoogleCloudAiplatformV1ThresholdConfig**](GoogleCloudAiplatformV1ThresholdConfig.md) |  |  [optional] |
|**skewThresholds** | [**Map&lt;String, GoogleCloudAiplatformV1ThresholdConfig&gt;**](GoogleCloudAiplatformV1ThresholdConfig.md) | Key is the feature name and value is the threshold. If a feature needs to be monitored for skew, a value threshold must be configured for that feature. The threshold here is against feature distribution distance between the training and prediction feature. |  [optional] |



