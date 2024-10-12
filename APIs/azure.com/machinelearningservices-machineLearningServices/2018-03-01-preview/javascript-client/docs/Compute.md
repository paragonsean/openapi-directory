# AzureMachineLearningWorkspaces.Compute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computeLocation** | **String** | Location for the underlying compute | [optional] 
**computeType** | [**ComputeType**](ComputeType.md) |  | 
**createdOn** | **Date** | The date and time when the compute was created. | [optional] [readonly] 
**description** | **String** | The description of the Machine Learning compute. | [optional] 
**modifiedOn** | **Date** | The date and time when the compute was last modified. | [optional] [readonly] 
**provisioningErrors** | [**[MachineLearningServiceError]**](MachineLearningServiceError.md) | Errors during provisioning | [optional] [readonly] 
**provisioningState** | **String** | The provision state of the cluster. Valid values are Unknown, Updating, Provisioning, Succeeded, and Failed. | [optional] [readonly] 
**resourceId** | **String** | ARM resource id of the compute | [optional] 



## Enum: ProvisioningStateEnum


* `Unknown` (value: `"Unknown"`)

* `Updating` (value: `"Updating"`)

* `Creating` (value: `"Creating"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)




