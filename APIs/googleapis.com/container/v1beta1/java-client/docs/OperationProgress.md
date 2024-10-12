

# OperationProgress

Information about operation (or operation stage) progress.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**metrics** | [**List&lt;Metric&gt;**](Metric.md) | Progress metric bundle, for example: metrics: [{name: \&quot;nodes done\&quot;, int_value: 15}, {name: \&quot;nodes total\&quot;, int_value: 32}] or metrics: [{name: \&quot;progress\&quot;, double_value: 0.56}, {name: \&quot;progress scale\&quot;, double_value: 1.0}] |  [optional] |
|**name** | **String** | A non-parameterized string describing an operation stage. Unset for single-stage operations. |  [optional] |
|**stages** | [**List&lt;OperationProgress&gt;**](OperationProgress.md) | Substages of an operation or a stage. |  [optional] |
|**status** | [**StatusEnum**](#StatusEnum) | Status of an operation stage. Unset for single-stage operations. |  [optional] |



## Enum: StatusEnum

| Name | Value |
|---- | -----|
| STATUS_UNSPECIFIED | &quot;STATUS_UNSPECIFIED&quot; |
| PENDING | &quot;PENDING&quot; |
| RUNNING | &quot;RUNNING&quot; |
| DONE | &quot;DONE&quot; |
| ABORTING | &quot;ABORTING&quot; |



