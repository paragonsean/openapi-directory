

# OSPolicyResourceExecResourceExec

A file or script to execute.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**args** | **List&lt;String&gt;** | Optional arguments to pass to the source during execution. |  [optional] |
|**_file** | [**OSPolicyResourceFile**](OSPolicyResourceFile.md) |  |  [optional] |
|**interpreter** | [**InterpreterEnum**](#InterpreterEnum) | Required. The script interpreter to use. |  [optional] |
|**outputFilePath** | **String** | Only recorded for enforce Exec. Path to an output file (that is created by this Exec) whose content will be recorded in OSPolicyResourceCompliance after a successful run. Absence or failure to read this file will result in this ExecResource being non-compliant. Output file size is limited to 100K bytes. |  [optional] |
|**script** | **String** | An inline script. The size of the script is limited to 32KiB. |  [optional] |



## Enum: InterpreterEnum

| Name | Value |
|---- | -----|
| INTERPRETER_UNSPECIFIED | &quot;INTERPRETER_UNSPECIFIED&quot; |
| NONE | &quot;NONE&quot; |
| SHELL | &quot;SHELL&quot; |
| POWERSHELL | &quot;POWERSHELL&quot; |



