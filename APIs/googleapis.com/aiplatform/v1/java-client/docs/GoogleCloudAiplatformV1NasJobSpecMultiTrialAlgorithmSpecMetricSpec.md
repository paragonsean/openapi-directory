

# GoogleCloudAiplatformV1NasJobSpecMultiTrialAlgorithmSpecMetricSpec

Represents a metric to optimize.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**goal** | [**GoalEnum**](#GoalEnum) | Required. The optimization goal of the metric. |  [optional] |
|**metricId** | **String** | Required. The ID of the metric. Must not contain whitespaces. |  [optional] |



## Enum: GoalEnum

| Name | Value |
|---- | -----|
| GOAL_TYPE_UNSPECIFIED | &quot;GOAL_TYPE_UNSPECIFIED&quot; |
| MAXIMIZE | &quot;MAXIMIZE&quot; |
| MINIMIZE | &quot;MINIMIZE&quot; |



