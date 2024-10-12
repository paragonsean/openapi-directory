

# GoogleCloudMlV1MetricSpec

MetricSpec contains the specifications to use to calculate the desired nodes count when autoscaling is enabled.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | [**NameEnum**](#NameEnum) | metric name. |  [optional] |
|**target** | **Integer** | Target specifies the target value for the given metric; once real metric deviates from the threshold by a certain percentage, the node count changes. |  [optional] |



## Enum: NameEnum

| Name | Value |
|---- | -----|
| METRIC_NAME_UNSPECIFIED | &quot;METRIC_NAME_UNSPECIFIED&quot; |
| CPU_USAGE | &quot;CPU_USAGE&quot; |
| GPU_DUTY_CYCLE | &quot;GPU_DUTY_CYCLE&quot; |



