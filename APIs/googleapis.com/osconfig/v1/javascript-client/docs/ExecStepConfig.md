# OsConfigApi.ExecStepConfig

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allowedSuccessCodes** | **[Number]** | Defaults to [0]. A list of possible return values that the execution can return to indicate a success. | [optional] 
**gcsObject** | [**GcsObject**](GcsObject.md) |  | [optional] 
**interpreter** | **String** | The script interpreter to use to run the script. If no interpreter is specified the script will be executed directly, which will likely only succeed for scripts with [shebang lines] (https://en.wikipedia.org/wiki/Shebang_\\(Unix\\)). | [optional] 
**localPath** | **String** | An absolute path to the executable on the VM. | [optional] 



## Enum: InterpreterEnum


* `INTERPRETER_UNSPECIFIED` (value: `"INTERPRETER_UNSPECIFIED"`)

* `NONE` (value: `"NONE"`)

* `SHELL` (value: `"SHELL"`)

* `POWERSHELL` (value: `"POWERSHELL"`)




