# ServiceControlApi.TraceSpan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**attributes** | [**Attributes**](Attributes.md) |  | [optional] 
**childSpanCount** | **Number** | An optional number of child spans that were generated while this span was active. If set, allows implementation to detect missing child spans. | [optional] 
**displayName** | [**TruncatableString**](TruncatableString.md) |  | [optional] 
**endTime** | **String** | The end time of the span. On the client side, this is the time kept by the local machine where the span execution ends. On the server side, this is the time when the server application handler stops running. | [optional] 
**name** | **String** | The resource name of the span in the following format: projects/[PROJECT_ID]/traces/[TRACE_ID]/spans/SPAN_ID is a unique identifier for a trace within a project; it is a 32-character hexadecimal encoding of a 16-byte array. [SPAN_ID] is a unique identifier for a span within a trace; it is a 16-character hexadecimal encoding of an 8-byte array. | [optional] 
**parentSpanId** | **String** | The [SPAN_ID] of this span&#39;s parent span. If this is a root span, then this field must be empty. | [optional] 
**sameProcessAsParentSpan** | **Boolean** | (Optional) Set this parameter to indicate whether this span is in the same process as its parent. If you do not set this parameter, Stackdriver Trace is unable to take advantage of this helpful information. | [optional] 
**spanId** | **String** | The [SPAN_ID] portion of the span&#39;s resource name. | [optional] 
**spanKind** | **String** | Distinguishes between spans generated in a particular context. For example, two spans with the same name may be distinguished using &#x60;CLIENT&#x60; (caller) and &#x60;SERVER&#x60; (callee) to identify an RPC call. | [optional] 
**startTime** | **String** | The start time of the span. On the client side, this is the time kept by the local machine where the span execution starts. On the server side, this is the time when the server&#39;s application handler starts running. | [optional] 
**status** | [**Status**](Status.md) |  | [optional] 



## Enum: SpanKindEnum


* `SPAN_KIND_UNSPECIFIED` (value: `"SPAN_KIND_UNSPECIFIED"`)

* `INTERNAL` (value: `"INTERNAL"`)

* `SERVER` (value: `"SERVER"`)

* `CLIENT` (value: `"CLIENT"`)

* `PRODUCER` (value: `"PRODUCER"`)

* `CONSUMER` (value: `"CONSUMER"`)




