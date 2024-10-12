# MigrationCenterApi.VirtualMachinePreferencesSizingOptimizationCustomParameters

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aggregationMethod** | **String** | Optional. Type of statistical aggregation of a resource utilization data, on which to base the sizing metrics. | [optional] 
**cpuUsagePercentage** | **Number** | Optional. Desired percentage of CPU usage. Must be in the interval [1, 100] (or 0 for default value). | [optional] 
**memoryUsagePercentage** | **Number** | Optional. Desired percentage of memory usage. Must be in the interval [1, 100] (or 0 for default value). | [optional] 
**storageMultiplier** | **Number** | Optional. Desired increase factor of storage, relative to currently used storage. Must be in the interval [1.0, 2.0] (or 0 for default value). | [optional] 



## Enum: AggregationMethodEnum


* `UNSPECIFIED` (value: `"AGGREGATION_METHOD_UNSPECIFIED"`)

* `AVERAGE` (value: `"AGGREGATION_METHOD_AVERAGE"`)

* `MEDIAN` (value: `"AGGREGATION_METHOD_MEDIAN"`)

* `NINETY_FIFTH_PERCENTILE` (value: `"AGGREGATION_METHOD_NINETY_FIFTH_PERCENTILE"`)

* `PEAK` (value: `"AGGREGATION_METHOD_PEAK"`)




