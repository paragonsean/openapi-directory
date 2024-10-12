# AzureMachineLearningWorkspaces.UpdateWorkspaceQuotas

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | Specifies the resource ID. | [optional] [readonly] 
**limit** | **Number** | The maximum permitted quota of the resource. | [optional] 
**status** | **String** | Status of update workspace quota. | [optional] 
**type** | **String** | Specifies the resource type. | [optional] [readonly] 
**unit** | **String** | An enum describing the unit of quota measurement. | [optional] [readonly] 



## Enum: StatusEnum


* `Undefined` (value: `"Undefined"`)

* `Success` (value: `"Success"`)

* `Failure` (value: `"Failure"`)

* `InvalidQuotaBelowClusterMinimum` (value: `"InvalidQuotaBelowClusterMinimum"`)

* `InvalidQuotaExceedsSubscriptionLimit` (value: `"InvalidQuotaExceedsSubscriptionLimit"`)

* `InvalidVMFamilyName` (value: `"InvalidVMFamilyName"`)





## Enum: UnitEnum


* `Count` (value: `"Count"`)




