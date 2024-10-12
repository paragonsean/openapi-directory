

# Link

A pointer from the current span to another span in the same trace or in a different trace. For example, this can be used in batching operations, where a single batch handler processes multiple requests from different traces or when the handler receives a request from a different project.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**attributes** | [**Attributes**](Attributes.md) |  |  [optional] |
|**spanId** | **String** | The &#x60;[SPAN_ID]&#x60; for a span within a trace. |  [optional] |
|**traceId** | **String** | The &#x60;[TRACE_ID]&#x60; for a trace within a project. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | The relationship of the current span relative to the linked span. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| TYPE_UNSPECIFIED | &quot;TYPE_UNSPECIFIED&quot; |
| CHILD_LINKED_SPAN | &quot;CHILD_LINKED_SPAN&quot; |
| PARENT_LINKED_SPAN | &quot;PARENT_LINKED_SPAN&quot; |



