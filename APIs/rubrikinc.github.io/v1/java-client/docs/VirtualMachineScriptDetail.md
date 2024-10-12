

# VirtualMachineScriptDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**failureHandling** | [**FailureHandlingEnum**](#FailureHandlingEnum) | Action to take if the script returns an error or times out. |  |
|**scriptPath** | **String** | The command to be run in VM guest OS. |  |
|**timeoutMs** | **Long** | Time (in ms) after which the script will be terminated if it has not completed. |  |



## Enum: FailureHandlingEnum

| Name | Value |
|---- | -----|
| ABORT | &quot;abort&quot; |
| CONTINUE | &quot;continue&quot; |



