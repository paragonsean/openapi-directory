# AzureMachineLearningWorkspaces.Compute

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**computeLocation** | **String** | Location for the underlying compute | [optional] 
**computeType** | [**ComputeType**](ComputeType.md) |  | 
**createdOn** | **Date** | The date and time when the compute was created. | [optional] [readonly] 
**description** | **String** | The description of the Machine Learning compute. | [optional] 
**isAttachedCompute** | **Boolean** | Indicating whether the compute was provisioned by user and brought from outside if true, or machine learning service provisioned it if false. | [optional] [readonly] 
**modifiedOn** | **Date** | The date and time when the compute was last modified. | [optional] [readonly] 
**provisioningErrors** | [**[MachineLearningServiceError]**](MachineLearningServiceError.md) | Errors during provisioning | [optional] [readonly] 
**provisioningState** | **String** | The provision state of the cluster. Valid values are Unknown, Updating, Provisioning, Succeeded, and Failed. | [optional] [readonly] 
**resourceId** | **String** | ARM resource id of the underlying compute | [optional] 



## Enum: ProvisioningStateEnum


* `Unknown` (value: `"Unknown"`)

* `Updating` (value: `"Updating"`)

* `Creating` (value: `"Creating"`)

* `Deleting` (value: `"Deleting"`)

* `Succeeded` (value: `"Succeeded"`)

* `Failed` (value: `"Failed"`)

* `Canceled` (value: `"Canceled"`)




