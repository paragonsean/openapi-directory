

# AveragePartitionLoadScalingTrigger

Represents a scaling trigger related to an average load of a metric/resource of a partition.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**lowerLoadThreshold** | **Double** | The lower limit of the load below which a scale in operation should be performed. |  |
|**metricName** | **String** | The name of the metric for which usage should be tracked. |  |
|**scaleIntervalInSeconds** | **Long** | The period in seconds on which a decision is made whether to scale or not. |  |
|**upperLoadThreshold** | **Double** | The upper limit of the load beyond which a scale out operation should be performed. |  |



