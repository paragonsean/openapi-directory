

# GoogleCloudAiplatformV1beta1SearchModelDeploymentMonitoringStatsAnomaliesResponse

Response message for JobService.SearchModelDeploymentMonitoringStatsAnomalies.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**monitoringStats** | [**List&lt;GoogleCloudAiplatformV1beta1ModelMonitoringStatsAnomalies&gt;**](GoogleCloudAiplatformV1beta1ModelMonitoringStatsAnomalies.md) | Stats retrieved for requested objectives. There are at most 1000 ModelMonitoringStatsAnomalies.FeatureHistoricStatsAnomalies.prediction_stats in the response. |  [optional] |
|**nextPageToken** | **String** | The page token that can be used by the next JobService.SearchModelDeploymentMonitoringStatsAnomalies call. |  [optional] |



