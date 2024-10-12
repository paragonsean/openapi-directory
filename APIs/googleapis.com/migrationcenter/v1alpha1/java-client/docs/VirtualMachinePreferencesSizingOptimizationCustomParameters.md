

# VirtualMachinePreferencesSizingOptimizationCustomParameters

Custom data to use for sizing optimizations.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**aggregationMethod** | [**AggregationMethodEnum**](#AggregationMethodEnum) | Optional. Type of statistical aggregation of a resource utilization data, on which to base the sizing metrics. |  [optional] |
|**cpuUsagePercentage** | **Integer** | Optional. Desired percentage of CPU usage. Must be in the interval [1, 100] (or 0 for default value). |  [optional] |
|**memoryUsagePercentage** | **Integer** | Optional. Desired percentage of memory usage. Must be in the interval [1, 100] (or 0 for default value). |  [optional] |
|**storageMultiplier** | **Double** | Optional. Desired increase factor of storage, relative to currently used storage. Must be in the interval [1.0, 2.0] (or 0 for default value). |  [optional] |



## Enum: AggregationMethodEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;AGGREGATION_METHOD_UNSPECIFIED&quot; |
| AVERAGE | &quot;AGGREGATION_METHOD_AVERAGE&quot; |
| MEDIAN | &quot;AGGREGATION_METHOD_MEDIAN&quot; |
| NINETY_FIFTH_PERCENTILE | &quot;AGGREGATION_METHOD_NINETY_FIFTH_PERCENTILE&quot; |
| PEAK | &quot;AGGREGATION_METHOD_PEAK&quot; |



