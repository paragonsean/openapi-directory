# VertexAiApi.GoogleCloudAiplatformV1FeaturestoreMonitoringConfigSnapshotAnalysis

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disabled** | **Boolean** | The monitoring schedule for snapshot analysis. For EntityType-level config: unset / disabled &#x3D; true indicates disabled by default for Features under it; otherwise by default enable snapshot analysis monitoring with monitoring_interval for Features under it. Feature-level config: disabled &#x3D; true indicates disabled regardless of the EntityType-level config; unset monitoring_interval indicates going with EntityType-level config; otherwise run snapshot analysis monitoring with monitoring_interval regardless of the EntityType-level config. Explicitly Disable the snapshot analysis based monitoring. | [optional] 
**monitoringIntervalDays** | **Number** | Configuration of the snapshot analysis based monitoring pipeline running interval. The value indicates number of days. | [optional] 
**stalenessDays** | **Number** | Customized export features time window for snapshot analysis. Unit is one day. Default value is 3 weeks. Minimum value is 1 day. Maximum value is 4000 days. | [optional] 


