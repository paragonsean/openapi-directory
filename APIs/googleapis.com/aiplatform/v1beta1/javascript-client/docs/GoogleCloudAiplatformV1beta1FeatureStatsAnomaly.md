# VertexAiApi.GoogleCloudAiplatformV1beta1FeatureStatsAnomaly

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**anomalyDetectionThreshold** | **Number** | This is the threshold used when detecting anomalies. The threshold can be changed by user, so this one might be different from ThresholdConfig.value. | [optional] 
**anomalyUri** | **String** | Path of the anomaly file for current feature values in Cloud Storage bucket. Format: gs:////anomalies. Example: gs://monitoring_bucket/feature_name/anomalies. Stats are stored as binary format with Protobuf message Anoamlies are stored as binary format with Protobuf message [tensorflow.metadata.v0.AnomalyInfo] (https://github.com/tensorflow/metadata/blob/master/tensorflow_metadata/proto/v0/anomalies.proto). | [optional] 
**distributionDeviation** | **Number** | Deviation from the current stats to baseline stats. 1. For categorical feature, the distribution distance is calculated by L-inifinity norm. 2. For numerical feature, the distribution distance is calculated by Jensen–Shannon divergence. | [optional] 
**endTime** | **String** | The end timestamp of window where stats were generated. For objectives where time window doesn&#39;t make sense (e.g. Featurestore Snapshot Monitoring), end_time indicates the timestamp of the data used to generate stats (e.g. timestamp we take snapshots for feature values). | [optional] 
**score** | **Number** | Feature importance score, only populated when cross-feature monitoring is enabled. For now only used to represent feature attribution score within range [0, 1] for ModelDeploymentMonitoringObjectiveType.FEATURE_ATTRIBUTION_SKEW and ModelDeploymentMonitoringObjectiveType.FEATURE_ATTRIBUTION_DRIFT. | [optional] 
**startTime** | **String** | The start timestamp of window where stats were generated. For objectives where time window doesn&#39;t make sense (e.g. Featurestore Snapshot Monitoring), start_time is only used to indicate the monitoring intervals, so it always equals to (end_time - monitoring_interval). | [optional] 
**statsUri** | **String** | Path of the stats file for current feature values in Cloud Storage bucket. Format: gs:////stats. Example: gs://monitoring_bucket/feature_name/stats. Stats are stored as binary format with Protobuf message [tensorflow.metadata.v0.FeatureNameStatistics](https://github.com/tensorflow/metadata/blob/master/tensorflow_metadata/proto/v0/statistics.proto). | [optional] 


