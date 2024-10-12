# AppsScriptApi.ExecutionError

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorMessage** | **String** | The error message thrown by Apps Script, usually localized into the user&#39;s language. | [optional] 
**errorType** | **String** | The error type, for example &#x60;TypeError&#x60; or &#x60;ReferenceError&#x60;. If the error type is unavailable, this field is not included. | [optional] 
**scriptStackTraceElements** | [**[ScriptStackTraceElement]**](ScriptStackTraceElement.md) | An array of objects that provide a stack trace through the script to show where the execution failed, with the deepest call first. | [optional] 


