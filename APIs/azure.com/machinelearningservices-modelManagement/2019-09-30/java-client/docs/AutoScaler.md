

# AutoScaler

The Auto Scaler properties.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**autoscaleEnabled** | **Boolean** | Option to enable/disable auto scaling. |  [optional] |
|**maxReplicas** | **Integer** | The maximum number of replicas in the cluster. |  [optional] |
|**minReplicas** | **Integer** | The minimum number of replicas to scale down to. |  [optional] |
|**refreshPeriodInSeconds** | **Integer** | The amount of seconds to wait between auto scale updates. |  [optional] |
|**targetUtilization** | **Integer** | The target utilization percentage to use for determining whether to scale the cluster. |  [optional] |



