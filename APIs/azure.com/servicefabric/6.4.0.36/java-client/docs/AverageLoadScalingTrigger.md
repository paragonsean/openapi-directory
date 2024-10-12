

# AverageLoadScalingTrigger

Describes the average load trigger used for auto scaling.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lowerLoadThreshold** | **Double** | Lower load threshold (if average load is below this threshold, service will scale down). |  |
|**metric** | [**AutoScalingMetric**](AutoScalingMetric.md) |  |  |
|**scaleIntervalInSeconds** | **Integer** | Scale interval that indicates how often will this trigger be checked. |  |
|**upperLoadThreshold** | **Double** | Upper load threshold (if average load is above this threshold, service will scale up). |  |



