

# SpanContext

The context of a span. This is attached to an Exemplar in Distribution values during aggregation. It contains the name of a span with format: projects/[PROJECT_ID_OR_NUMBER]/traces/[TRACE_ID]/spans/[SPAN_ID]

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**spanName** | **String** | The resource name of the span. The format is: projects/[PROJECT_ID_OR_NUMBER]/traces/[TRACE_ID]/spans/[SPAN_ID] &#x60;[TRACE_ID]&#x60; is a unique identifier for a trace within a project; it is a 32-character hexadecimal encoding of a 16-byte array. &#x60;[SPAN_ID]&#x60; is a unique identifier for a span within a trace; it is a 16-character hexadecimal encoding of an 8-byte array. |  [optional] |



