

# AutoscalingSettings

Settings for WorkerPool autoscaling.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**algorithm** | [**AlgorithmEnum**](#AlgorithmEnum) | The algorithm to use for autoscaling. |  [optional] |
|**maxNumWorkers** | **Integer** | The maximum number of workers to cap scaling at. |  [optional] |



## Enum: AlgorithmEnum

| Name | Value |
|---- | -----|
| UNKNOWN | &quot;AUTOSCALING_ALGORITHM_UNKNOWN&quot; |
| NONE | &quot;AUTOSCALING_ALGORITHM_NONE&quot; |
| BASIC | &quot;AUTOSCALING_ALGORITHM_BASIC&quot; |



