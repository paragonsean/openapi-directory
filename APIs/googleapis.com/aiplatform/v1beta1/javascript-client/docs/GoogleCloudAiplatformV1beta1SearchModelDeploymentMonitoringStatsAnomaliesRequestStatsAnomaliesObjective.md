# VertexAiApi.GoogleCloudAiplatformV1beta1SearchModelDeploymentMonitoringStatsAnomaliesRequestStatsAnomaliesObjective

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**topFeatureCount** | **Number** | If set, all attribution scores between SearchModelDeploymentMonitoringStatsAnomaliesRequest.start_time and SearchModelDeploymentMonitoringStatsAnomaliesRequest.end_time are fetched, and page token doesn&#39;t take effect in this case. Only used to retrieve attribution score for the top Features which has the highest attribution score in the latest monitoring run. | [optional] 
**type** | **String** |  | [optional] 



## Enum: TypeEnum


* `MODEL_DEPLOYMENT_MONITORING_OBJECTIVE_TYPE_UNSPECIFIED` (value: `"MODEL_DEPLOYMENT_MONITORING_OBJECTIVE_TYPE_UNSPECIFIED"`)

* `RAW_FEATURE_SKEW` (value: `"RAW_FEATURE_SKEW"`)

* `RAW_FEATURE_DRIFT` (value: `"RAW_FEATURE_DRIFT"`)

* `FEATURE_ATTRIBUTION_SKEW` (value: `"FEATURE_ATTRIBUTION_SKEW"`)

* `FEATURE_ATTRIBUTION_DRIFT` (value: `"FEATURE_ATTRIBUTION_DRIFT"`)




