# OsConfigApi.OSPolicyResourceExecResourceExec

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**args** | **[String]** | Optional arguments to pass to the source during execution. | [optional] 
**file** | [**OSPolicyResourceFile**](OSPolicyResourceFile.md) |  | [optional] 
**interpreter** | **String** | Required. The script interpreter to use. | [optional] 
**outputFilePath** | **String** | Only recorded for enforce Exec. Path to an output file (that is created by this Exec) whose content will be recorded in OSPolicyResourceCompliance after a successful run. Absence or failure to read this file will result in this ExecResource being non-compliant. Output file size is limited to 100K bytes. | [optional] 
**script** | **String** | An inline script. The size of the script is limited to 32KiB. | [optional] 



## Enum: InterpreterEnum


* `INTERPRETER_UNSPECIFIED` (value: `"INTERPRETER_UNSPECIFIED"`)

* `NONE` (value: `"NONE"`)

* `SHELL` (value: `"SHELL"`)

* `POWERSHELL` (value: `"POWERSHELL"`)




