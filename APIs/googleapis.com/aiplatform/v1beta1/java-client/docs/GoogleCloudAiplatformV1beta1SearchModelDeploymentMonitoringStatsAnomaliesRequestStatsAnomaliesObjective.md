

# GoogleCloudAiplatformV1beta1SearchModelDeploymentMonitoringStatsAnomaliesRequestStatsAnomaliesObjective

Stats requested for specific objective.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**topFeatureCount** | **Integer** | If set, all attribution scores between SearchModelDeploymentMonitoringStatsAnomaliesRequest.start_time and SearchModelDeploymentMonitoringStatsAnomaliesRequest.end_time are fetched, and page token doesn&#39;t take effect in this case. Only used to retrieve attribution score for the top Features which has the highest attribution score in the latest monitoring run. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| MODEL_DEPLOYMENT_MONITORING_OBJECTIVE_TYPE_UNSPECIFIED | &quot;MODEL_DEPLOYMENT_MONITORING_OBJECTIVE_TYPE_UNSPECIFIED&quot; |
| RAW_FEATURE_SKEW | &quot;RAW_FEATURE_SKEW&quot; |
| RAW_FEATURE_DRIFT | &quot;RAW_FEATURE_DRIFT&quot; |
| FEATURE_ATTRIBUTION_SKEW | &quot;FEATURE_ATTRIBUTION_SKEW&quot; |
| FEATURE_ATTRIBUTION_DRIFT | &quot;FEATURE_ATTRIBUTION_DRIFT&quot; |



