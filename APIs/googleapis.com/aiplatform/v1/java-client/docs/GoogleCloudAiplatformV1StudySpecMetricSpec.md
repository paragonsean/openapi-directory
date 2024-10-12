

# GoogleCloudAiplatformV1StudySpecMetricSpec

Represents a metric to optimize.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**goal** | [**GoalEnum**](#GoalEnum) | Required. The optimization goal of the metric. |  [optional] |
|**metricId** | **String** | Required. The ID of the metric. Must not contain whitespaces and must be unique amongst all MetricSpecs. |  [optional] |
|**safetyConfig** | [**GoogleCloudAiplatformV1StudySpecMetricSpecSafetyMetricConfig**](GoogleCloudAiplatformV1StudySpecMetricSpecSafetyMetricConfig.md) |  |  [optional] |



## Enum: GoalEnum

| Name | Value |
|---- | -----|
| GOAL_TYPE_UNSPECIFIED | &quot;GOAL_TYPE_UNSPECIFIED&quot; |
| MAXIMIZE | &quot;MAXIMIZE&quot; |
| MINIMIZE | &quot;MINIMIZE&quot; |



