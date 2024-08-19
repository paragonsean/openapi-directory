# VertexAiApi.GoogleCloudAiplatformV1beta1ModelMonitoringStatsAnomalies

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anomalyCount** | **Number** | Number of anomalies within all stats. | [optional] 
**deployedModelId** | **String** | Deployed Model ID. | [optional] 
**featureStats** | [**[GoogleCloudAiplatformV1beta1ModelMonitoringStatsAnomaliesFeatureHistoricStatsAnomalies]**](GoogleCloudAiplatformV1beta1ModelMonitoringStatsAnomaliesFeatureHistoricStatsAnomalies.md) | A list of historical Stats and Anomalies generated for all Features. | [optional] 
**objective** | **String** | Model Monitoring Objective those stats and anomalies belonging to. | [optional] 



## Enum: ObjectiveEnum


* `MODEL_DEPLOYMENT_MONITORING_OBJECTIVE_TYPE_UNSPECIFIED` (value: `"MODEL_DEPLOYMENT_MONITORING_OBJECTIVE_TYPE_UNSPECIFIED"`)

* `RAW_FEATURE_SKEW` (value: `"RAW_FEATURE_SKEW"`)

* `RAW_FEATURE_DRIFT` (value: `"RAW_FEATURE_DRIFT"`)

* `FEATURE_ATTRIBUTION_SKEW` (value: `"FEATURE_ATTRIBUTION_SKEW"`)

* `FEATURE_ATTRIBUTION_DRIFT` (value: `"FEATURE_ATTRIBUTION_DRIFT"`)




