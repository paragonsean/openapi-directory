

# BasicAutoscalingAlgorithm

Basic algorithm for autoscaling.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**cooldownPeriod** | **String** | Optional. Duration between scaling events. A scaling period starts after the update operation from the previous event has completed.Bounds: 2m, 1d. Default: 2m. |  [optional] |
|**sparkStandaloneConfig** | [**SparkStandaloneAutoscalingConfig**](SparkStandaloneAutoscalingConfig.md) |  |  [optional] |
|**yarnConfig** | [**BasicYarnAutoscalingConfig**](BasicYarnAutoscalingConfig.md) |  |  [optional] |



