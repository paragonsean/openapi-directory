

# StackFrame

Represents a single stack frame in a stack trace.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**columnNumber** | **String** | The column number where the function call appears, if available. This is important in JavaScript because of its anonymous functions. |  [optional] |
|**fileName** | [**TruncatableString**](TruncatableString.md) |  |  [optional] |
|**functionName** | [**TruncatableString**](TruncatableString.md) |  |  [optional] |
|**lineNumber** | **String** | The line number in &#x60;file_name&#x60; where the function call appears. |  [optional] |
|**loadModule** | [**Module**](Module.md) |  |  [optional] |
|**originalFunctionName** | [**TruncatableString**](TruncatableString.md) |  |  [optional] |
|**sourceVersion** | [**TruncatableString**](TruncatableString.md) |  |  [optional] |



