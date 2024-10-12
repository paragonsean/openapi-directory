

# Trace

A trace describes how long it takes for an application to perform an operation. It consists of a set of spans, each of which represent a single timed event within the operation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**projectId** | **String** | Project ID of the Cloud project where the trace data is stored. |  [optional] |
|**spans** | [**List&lt;TraceSpan&gt;**](TraceSpan.md) | Collection of spans in the trace. |  [optional] |
|**traceId** | **String** | Globally unique identifier for the trace. This identifier is a 128-bit numeric value formatted as a 32-byte hex string. For example, &#x60;382d4f4c6b7bb2f4a972559d9085001d&#x60;. The numeric value should not be zero. |  [optional] |



