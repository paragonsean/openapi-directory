# OsConfigApi.SoftwareRecipeStepRunScript

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedExitCodes** | **[Number]** | Return codes that indicate that the software installed or updated successfully. Behaviour defaults to [0] | [optional] 
**interpreter** | **String** | The script interpreter to use to run the script. If no interpreter is specified the script is executed directly, which likely only succeed for scripts with [shebang lines](https://en.wikipedia.org/wiki/Shebang_\\(Unix\\)). | [optional] 
**script** | **String** | Required. The shell script to be executed. | [optional] 



## Enum: InterpreterEnum


* `INTERPRETER_UNSPECIFIED` (value: `"INTERPRETER_UNSPECIFIED"`)

* `SHELL` (value: `"SHELL"`)

* `POWERSHELL` (value: `"POWERSHELL"`)




