# CloudTraceApi.Link

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**Attributes**](Attributes.md) |  | [optional] 
**spanId** | **String** | The &#x60;[SPAN_ID]&#x60; for a span within a trace. | [optional] 
**traceId** | **String** | The &#x60;[TRACE_ID]&#x60; for a trace within a project. | [optional] 
**type** | **String** | The relationship of the current span relative to the linked span. | [optional] 



## Enum: TypeEnum


* `TYPE_UNSPECIFIED` (value: `"TYPE_UNSPECIFIED"`)

* `CHILD_LINKED_SPAN` (value: `"CHILD_LINKED_SPAN"`)

* `PARENT_LINKED_SPAN` (value: `"PARENT_LINKED_SPAN"`)




