# KubernetesEngineApi.OperationProgress

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metrics** | [**[Metric]**](Metric.md) | Progress metric bundle, for example: metrics: [{name: \&quot;nodes done\&quot;, int_value: 15}, {name: \&quot;nodes total\&quot;, int_value: 32}] or metrics: [{name: \&quot;progress\&quot;, double_value: 0.56}, {name: \&quot;progress scale\&quot;, double_value: 1.0}] | [optional] 
**name** | **String** | A non-parameterized string describing an operation stage. Unset for single-stage operations. | [optional] 
**stages** | [**[OperationProgress]**](OperationProgress.md) | Substages of an operation or a stage. | [optional] 
**status** | **String** | Status of an operation stage. Unset for single-stage operations. | [optional] 



## Enum: StatusEnum


* `STATUS_UNSPECIFIED` (value: `"STATUS_UNSPECIFIED"`)

* `PENDING` (value: `"PENDING"`)

* `RUNNING` (value: `"RUNNING"`)

* `DONE` (value: `"DONE"`)

* `ABORTING` (value: `"ABORTING"`)




