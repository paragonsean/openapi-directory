# RubrikRestApi.VirtualMachineScriptDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**failureHandling** | **String** | Action to take if the script returns an error or times out. | 
**scriptPath** | **String** | The command to be run in VM guest OS. | 
**timeoutMs** | **Number** | Time (in ms) after which the script will be terminated if it has not completed. | 



## Enum: FailureHandlingEnum


* `abort` (value: `"abort"`)

* `continue` (value: `"continue"`)




