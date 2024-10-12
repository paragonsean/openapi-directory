

# GoogleCloudAiplatformV1beta1FeatureMonitoringStatsAnomaly

A list of historical SnapshotAnalysis or ImportFeaturesAnalysis stats requested by user, sorted by FeatureStatsAnomaly.start_time descending.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**featureStatsAnomaly** | [**GoogleCloudAiplatformV1beta1FeatureStatsAnomaly**](GoogleCloudAiplatformV1beta1FeatureStatsAnomaly.md) |  |  [optional] |
|**objective** | [**ObjectiveEnum**](#ObjectiveEnum) | Output only. The objective for each stats. |  [optional] [readonly] |



## Enum: ObjectiveEnum

| Name | Value |
|---- | -----|
| OBJECTIVE_UNSPECIFIED | &quot;OBJECTIVE_UNSPECIFIED&quot; |
| IMPORT_FEATURE_ANALYSIS | &quot;IMPORT_FEATURE_ANALYSIS&quot; |
| SNAPSHOT_ANALYSIS | &quot;SNAPSHOT_ANALYSIS&quot; |



