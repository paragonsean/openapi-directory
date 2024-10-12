

# GoogleAppsScriptTypeProcess

Representation of a single script process execution that was started from the script editor, a trigger, an application, or using the Apps Script API. This is distinct from the `Operation` resource, which only represents executions started via the Apps Script API.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**duration** | **String** | Duration the execution spent executing. |  [optional] |
|**functionName** | **String** | Name of the function the started the execution. |  [optional] |
|**processStatus** | [**ProcessStatusEnum**](#ProcessStatusEnum) | The executions status. |  [optional] |
|**processType** | [**ProcessTypeEnum**](#ProcessTypeEnum) | The executions type. |  [optional] |
|**projectName** | **String** | Name of the script being executed. |  [optional] |
|**runtimeVersion** | [**RuntimeVersionEnum**](#RuntimeVersionEnum) | Which version of maestro to use to execute the script. |  [optional] |
|**startTime** | **String** | Time the execution started. |  [optional] |
|**userAccessLevel** | [**UserAccessLevelEnum**](#UserAccessLevelEnum) | The executing users access level to the script. |  [optional] |



## Enum: ProcessStatusEnum

| Name | Value |
|---- | -----|
| PROCESS_STATUS_UNSPECIFIED | &quot;PROCESS_STATUS_UNSPECIFIED&quot; |
| RUNNING | &quot;RUNNING&quot; |
| PAUSED | &quot;PAUSED&quot; |
| COMPLETED | &quot;COMPLETED&quot; |
| CANCELED | &quot;CANCELED&quot; |
| FAILED | &quot;FAILED&quot; |
| TIMED_OUT | &quot;TIMED_OUT&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| DELAYED | &quot;DELAYED&quot; |
| EXECUTION_DISABLED | &quot;EXECUTION_DISABLED&quot; |



## Enum: ProcessTypeEnum

| Name | Value |
|---- | -----|
| PROCESS_TYPE_UNSPECIFIED | &quot;PROCESS_TYPE_UNSPECIFIED&quot; |
| ADD_ON | &quot;ADD_ON&quot; |
| EXECUTION_API | &quot;EXECUTION_API&quot; |
| TIME_DRIVEN | &quot;TIME_DRIVEN&quot; |
| TRIGGER | &quot;TRIGGER&quot; |
| WEBAPP | &quot;WEBAPP&quot; |
| EDITOR | &quot;EDITOR&quot; |
| SIMPLE_TRIGGER | &quot;SIMPLE_TRIGGER&quot; |
| MENU | &quot;MENU&quot; |
| BATCH_TASK | &quot;BATCH_TASK&quot; |



## Enum: RuntimeVersionEnum

| Name | Value |
|---- | -----|
| RUNTIME_VERSION_UNSPECIFIED | &quot;RUNTIME_VERSION_UNSPECIFIED&quot; |
| DEPRECATED_ES5 | &quot;DEPRECATED_ES5&quot; |
| V8 | &quot;V8&quot; |



## Enum: UserAccessLevelEnum

| Name | Value |
|---- | -----|
| USER_ACCESS_LEVEL_UNSPECIFIED | &quot;USER_ACCESS_LEVEL_UNSPECIFIED&quot; |
| NONE | &quot;NONE&quot; |
| READ | &quot;READ&quot; |
| WRITE | &quot;WRITE&quot; |
| OWNER | &quot;OWNER&quot; |



