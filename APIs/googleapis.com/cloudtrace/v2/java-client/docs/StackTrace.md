

# StackTrace

A call stack appearing in a trace.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**stackFrames** | [**StackFrames**](StackFrames.md) |  |  [optional] |
|**stackTraceHashId** | **String** | The hash ID is used to conserve network bandwidth for duplicate stack traces within a single trace. Often multiple spans will have identical stack traces. The first occurrence of a stack trace should contain both the &#x60;stackFrame&#x60; content and a value in &#x60;stackTraceHashId&#x60;. Subsequent spans within the same request can refer to that stack trace by only setting &#x60;stackTraceHashId&#x60;. |  [optional] |



