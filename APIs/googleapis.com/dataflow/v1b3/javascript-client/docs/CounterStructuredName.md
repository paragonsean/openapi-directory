# DataflowApi.CounterStructuredName

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**componentStepName** | **String** | Name of the optimized step being executed by the workers. | [optional] 
**executionStepName** | **String** | Name of the stage. An execution step contains multiple component steps. | [optional] 
**inputIndex** | **Number** | Index of an input collection that&#39;s being read from/written to as a side input. The index identifies a step&#39;s side inputs starting by 1 (e.g. the first side input has input_index 1, the third has input_index 3). Side inputs are identified by a pair of (original_step_name, input_index). This field helps uniquely identify them. | [optional] 
**name** | **String** | Counter name. Not necessarily globally-unique, but unique within the context of the other fields. Required. | [optional] 
**origin** | **String** | One of the standard Origins defined above. | [optional] 
**originNamespace** | **String** | A string containing a more specific namespace of the counter&#39;s origin. | [optional] 
**originalRequestingStepName** | **String** | The step name requesting an operation, such as GBK. I.e. the ParDo causing a read/write from shuffle to occur, or a read from side inputs. | [optional] 
**originalStepName** | **String** | System generated name of the original step in the user&#39;s graph, before optimization. | [optional] 
**portion** | **String** | Portion of this counter, either key or value. | [optional] 
**workerId** | **String** | ID of a particular worker. | [optional] 



## Enum: OriginEnum


* `SYSTEM` (value: `"SYSTEM"`)

* `USER` (value: `"USER"`)





## Enum: PortionEnum


* `ALL` (value: `"ALL"`)

* `KEY` (value: `"KEY"`)

* `VALUE` (value: `"VALUE"`)




