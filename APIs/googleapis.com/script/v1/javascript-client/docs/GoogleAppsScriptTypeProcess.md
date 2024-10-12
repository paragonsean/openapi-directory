# AppsScriptApi.GoogleAppsScriptTypeProcess

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **String** | Duration the execution spent executing. | [optional] 
**functionName** | **String** | Name of the function the started the execution. | [optional] 
**processStatus** | **String** | The executions status. | [optional] 
**processType** | **String** | The executions type. | [optional] 
**projectName** | **String** | Name of the script being executed. | [optional] 
**runtimeVersion** | **String** | Which version of maestro to use to execute the script. | [optional] 
**startTime** | **String** | Time the execution started. | [optional] 
**userAccessLevel** | **String** | The executing users access level to the script. | [optional] 



## Enum: ProcessStatusEnum


* `PROCESS_STATUS_UNSPECIFIED` (value: `"PROCESS_STATUS_UNSPECIFIED"`)

* `RUNNING` (value: `"RUNNING"`)

* `PAUSED` (value: `"PAUSED"`)

* `COMPLETED` (value: `"COMPLETED"`)

* `CANCELED` (value: `"CANCELED"`)

* `FAILED` (value: `"FAILED"`)

* `TIMED_OUT` (value: `"TIMED_OUT"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `DELAYED` (value: `"DELAYED"`)

* `EXECUTION_DISABLED` (value: `"EXECUTION_DISABLED"`)





## Enum: ProcessTypeEnum


* `PROCESS_TYPE_UNSPECIFIED` (value: `"PROCESS_TYPE_UNSPECIFIED"`)

* `ADD_ON` (value: `"ADD_ON"`)

* `EXECUTION_API` (value: `"EXECUTION_API"`)

* `TIME_DRIVEN` (value: `"TIME_DRIVEN"`)

* `TRIGGER` (value: `"TRIGGER"`)

* `WEBAPP` (value: `"WEBAPP"`)

* `EDITOR` (value: `"EDITOR"`)

* `SIMPLE_TRIGGER` (value: `"SIMPLE_TRIGGER"`)

* `MENU` (value: `"MENU"`)

* `BATCH_TASK` (value: `"BATCH_TASK"`)





## Enum: RuntimeVersionEnum


* `RUNTIME_VERSION_UNSPECIFIED` (value: `"RUNTIME_VERSION_UNSPECIFIED"`)

* `DEPRECATED_ES5` (value: `"DEPRECATED_ES5"`)

* `V8` (value: `"V8"`)





## Enum: UserAccessLevelEnum


* `USER_ACCESS_LEVEL_UNSPECIFIED` (value: `"USER_ACCESS_LEVEL_UNSPECIFIED"`)

* `NONE` (value: `"NONE"`)

* `READ` (value: `"READ"`)

* `WRITE` (value: `"WRITE"`)

* `OWNER` (value: `"OWNER"`)




