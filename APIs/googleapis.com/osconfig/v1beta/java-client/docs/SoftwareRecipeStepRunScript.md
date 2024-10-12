

# SoftwareRecipeStepRunScript

Runs a script through an interpreter.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**allowedExitCodes** | **List&lt;Integer&gt;** | Return codes that indicate that the software installed or updated successfully. Behaviour defaults to [0] |  [optional] |
|**interpreter** | [**InterpreterEnum**](#InterpreterEnum) | The script interpreter to use to run the script. If no interpreter is specified the script is executed directly, which likely only succeed for scripts with [shebang lines](https://en.wikipedia.org/wiki/Shebang_\\(Unix\\)). |  [optional] |
|**script** | **String** | Required. The shell script to be executed. |  [optional] |



## Enum: InterpreterEnum

| Name | Value |
|---- | -----|
| INTERPRETER_UNSPECIFIED | &quot;INTERPRETER_UNSPECIFIED&quot; |
| SHELL | &quot;SHELL&quot; |
| POWERSHELL | &quot;POWERSHELL&quot; |



