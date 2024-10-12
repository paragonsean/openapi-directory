

# ExecutionError

An object that provides information about the nature of an error resulting from an attempted execution of a script function using the Apps Script API. If a run call succeeds but the script function (or Apps Script itself) throws an exception, the response body's error field contains a Status object. The `Status` object's `details` field contains an array with a single one of these `ExecutionError` objects.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorMessage** | **String** | The error message thrown by Apps Script, usually localized into the user&#39;s language. |  [optional] |
|**errorType** | **String** | The error type, for example &#x60;TypeError&#x60; or &#x60;ReferenceError&#x60;. If the error type is unavailable, this field is not included. |  [optional] |
|**scriptStackTraceElements** | [**List&lt;ScriptStackTraceElement&gt;**](ScriptStackTraceElement.md) | An array of objects that provide a stack trace through the script to show where the execution failed, with the deepest call first. |  [optional] |



