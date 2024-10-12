

# GoogleCloudAiplatformV1beta1FeaturestoreMonitoringConfigSnapshotAnalysis

Configuration of the Featurestore's Snapshot Analysis Based Monitoring. This type of analysis generates statistics for each Feature based on a snapshot of the latest feature value of each entities every monitoring_interval.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**disabled** | **Boolean** | The monitoring schedule for snapshot analysis. For EntityType-level config: unset / disabled &#x3D; true indicates disabled by default for Features under it; otherwise by default enable snapshot analysis monitoring with monitoring_interval for Features under it. Feature-level config: disabled &#x3D; true indicates disabled regardless of the EntityType-level config; unset monitoring_interval indicates going with EntityType-level config; otherwise run snapshot analysis monitoring with monitoring_interval regardless of the EntityType-level config. Explicitly Disable the snapshot analysis based monitoring. |  [optional] |
|**monitoringInterval** | **String** | Configuration of the snapshot analysis based monitoring pipeline running interval. The value is rolled up to full day. If both monitoring_interval_days and the deprecated &#x60;monitoring_interval&#x60; field are set when creating/updating EntityTypes/Features, monitoring_interval_days will be used. |  [optional] |
|**monitoringIntervalDays** | **Integer** | Configuration of the snapshot analysis based monitoring pipeline running interval. The value indicates number of days. |  [optional] |
|**stalenessDays** | **Integer** | Customized export features time window for snapshot analysis. Unit is one day. Default value is 3 weeks. Minimum value is 1 day. Maximum value is 4000 days. |  [optional] |



