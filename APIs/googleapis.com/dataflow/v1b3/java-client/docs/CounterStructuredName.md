

# CounterStructuredName

Identifies a counter within a per-job namespace. Counters whose structured names are the same get merged into a single value for the job.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**componentStepName** | **String** | Name of the optimized step being executed by the workers. |  [optional] |
|**executionStepName** | **String** | Name of the stage. An execution step contains multiple component steps. |  [optional] |
|**inputIndex** | **Integer** | Index of an input collection that&#39;s being read from/written to as a side input. The index identifies a step&#39;s side inputs starting by 1 (e.g. the first side input has input_index 1, the third has input_index 3). Side inputs are identified by a pair of (original_step_name, input_index). This field helps uniquely identify them. |  [optional] |
|**name** | **String** | Counter name. Not necessarily globally-unique, but unique within the context of the other fields. Required. |  [optional] |
|**origin** | [**OriginEnum**](#OriginEnum) | One of the standard Origins defined above. |  [optional] |
|**originNamespace** | **String** | A string containing a more specific namespace of the counter&#39;s origin. |  [optional] |
|**originalRequestingStepName** | **String** | The step name requesting an operation, such as GBK. I.e. the ParDo causing a read/write from shuffle to occur, or a read from side inputs. |  [optional] |
|**originalStepName** | **String** | System generated name of the original step in the user&#39;s graph, before optimization. |  [optional] |
|**portion** | [**PortionEnum**](#PortionEnum) | Portion of this counter, either key or value. |  [optional] |
|**workerId** | **String** | ID of a particular worker. |  [optional] |



## Enum: OriginEnum

| Name | Value |
|---- | -----|
| SYSTEM | &quot;SYSTEM&quot; |
| USER | &quot;USER&quot; |



## Enum: PortionEnum

| Name | Value |
|---- | -----|
| ALL | &quot;ALL&quot; |
| KEY | &quot;KEY&quot; |
| VALUE | &quot;VALUE&quot; |



