

# TraceSpan

A span represents a single timed event within a trace. Spans can be nested and form a trace tree. Often, a trace contains a root span that describes the end-to-end latency of an operation and, optionally, one or more subspans for its suboperations. Spans do not need to be contiguous. There may be gaps between spans in a trace.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**endTime** | **String** | End time of the span in seconds and nanoseconds from the UNIX epoch. |  [optional] |
|**kind** | [**KindEnum**](#KindEnum) | Distinguishes between spans generated in a particular context. For example, two spans with the same name may be distinguished using &#x60;RPC_CLIENT&#x60; and &#x60;RPC_SERVER&#x60; to identify queueing latency associated with the span. |  [optional] |
|**labels** | **Map&lt;String, String&gt;** | Collection of labels associated with the span. Label keys must be less than 128 bytes. Label values must be less than 16 kilobytes (10MB for &#x60;/stacktrace&#x60; values). Some predefined label keys exist, or you may create your own. When creating your own, we recommend the following formats: * &#x60;/category/product/key&#x60; for agents of well-known products (e.g. &#x60;/db/mongodb/read_size&#x60;). * &#x60;short_host/path/key&#x60; for domain-specific keys (e.g. &#x60;foo.com/myproduct/bar&#x60;) Predefined labels include: * &#x60;/agent&#x60; * &#x60;/component&#x60; * &#x60;/error/message&#x60; * &#x60;/error/name&#x60; * &#x60;/http/client_city&#x60; * &#x60;/http/client_country&#x60; * &#x60;/http/client_protocol&#x60; * &#x60;/http/client_region&#x60; * &#x60;/http/host&#x60; * &#x60;/http/method&#x60; * &#x60;/http/path&#x60; * &#x60;/http/redirected_url&#x60; * &#x60;/http/request/size&#x60; * &#x60;/http/response/size&#x60; * &#x60;/http/route&#x60; * &#x60;/http/status_code&#x60; * &#x60;/http/url&#x60; * &#x60;/http/user_agent&#x60; * &#x60;/pid&#x60; * &#x60;/stacktrace&#x60; * &#x60;/tid&#x60; |  [optional] |
|**name** | **String** | Name of the span. Must be less than 128 bytes. The span name is sanitized and displayed in the Trace tool in the Google Cloud Platform Console. The name may be a method name or some other per-call site name. For the same executable and the same call point, a best practice is to use a consistent name, which makes it easier to correlate cross-trace spans. |  [optional] |
|**parentSpanId** | **String** | Optional. ID of the parent span, if any. |  [optional] |
|**spanId** | **String** | Identifier for the span. Must be a 64-bit integer other than 0 and unique within a trace. For example, &#x60;2205310701640571284&#x60;. |  [optional] |
|**startTime** | **String** | Start time of the span in seconds and nanoseconds from the UNIX epoch. |  [optional] |



## Enum: KindEnum

| Name | Value |
|---- | -----|
| SPAN_KIND_UNSPECIFIED | &quot;SPAN_KIND_UNSPECIFIED&quot; |
| RPC_SERVER | &quot;RPC_SERVER&quot; |
| RPC_CLIENT | &quot;RPC_CLIENT&quot; |



