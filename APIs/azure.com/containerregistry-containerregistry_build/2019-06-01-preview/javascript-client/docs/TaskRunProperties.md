# ContainerRegistryManagementClient.TaskRunProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**forceUpdateTag** | **String** | How the run should be forced to rerun even if the run request configuration has not changed | [optional] 
**provisioningState** | **String** | The provisioning state of this task run | [optional] [readonly] 
**runRequest** | [**RunRequest**](RunRequest.md) |  | [optional] 
**runResult** | [**Run**](Run.md) |  | [optional] 



## Enum: ProvisioningStateEnum


* `Creating` (value: `"Creating"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)




