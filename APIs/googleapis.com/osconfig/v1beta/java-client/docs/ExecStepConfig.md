

# ExecStepConfig

Common configurations for an ExecStep.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedSuccessCodes** | **List&lt;Integer&gt;** | Defaults to [0]. A list of possible return values that the execution can return to indicate a success. |  [optional] |
|**gcsObject** | [**GcsObject**](GcsObject.md) |  |  [optional] |
|**interpreter** | [**InterpreterEnum**](#InterpreterEnum) | The script interpreter to use to run the script. If no interpreter is specified the script will be executed directly, which will likely only succeed for scripts with [shebang lines] (https://en.wikipedia.org/wiki/Shebang_\\(Unix\\)). |  [optional] |
|**localPath** | **String** | An absolute path to the executable on the VM. |  [optional] |



## Enum: InterpreterEnum

| Name | Value |
|---- | -----|
| INTERPRETER_UNSPECIFIED | &quot;INTERPRETER_UNSPECIFIED&quot; |
| NONE | &quot;NONE&quot; |
| SHELL | &quot;SHELL&quot; |
| POWERSHELL | &quot;POWERSHELL&quot; |



