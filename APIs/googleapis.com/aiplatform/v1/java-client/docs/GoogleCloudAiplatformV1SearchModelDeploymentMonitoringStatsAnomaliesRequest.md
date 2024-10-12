

# GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesRequest

Request message for JobService.SearchModelDeploymentMonitoringStatsAnomalies.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**deployedModelId** | **String** | Required. The DeployedModel ID of the [ModelDeploymentMonitoringObjectiveConfig.deployed_model_id]. |  [optional] |
|**endTime** | **String** | The latest timestamp of stats being generated. If not set, indicates feching stats till the latest possible one. |  [optional] |
|**featureDisplayName** | **String** | The feature display name. If specified, only return the stats belonging to this feature. Format: ModelMonitoringStatsAnomalies.FeatureHistoricStatsAnomalies.feature_display_name, example: \&quot;user_destination\&quot;. |  [optional] |
|**objectives** | [**List&lt;GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesRequestStatsAnomaliesObjective&gt;**](GoogleCloudAiplatformV1SearchModelDeploymentMonitoringStatsAnomaliesRequestStatsAnomaliesObjective.md) | Required. Objectives of the stats to retrieve. |  [optional] |
|**pageSize** | **Integer** | The standard list page size. |  [optional] |
|**pageToken** | **String** | A page token received from a previous JobService.SearchModelDeploymentMonitoringStatsAnomalies call. |  [optional] |
|**startTime** | **String** | The earliest timestamp of stats being generated. If not set, indicates fetching stats till the earliest possible one. |  [optional] |



