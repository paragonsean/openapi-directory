# BlueprintClient.AssignmentProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blueprintId** | **String** | ID of the published version of a blueprint definition. | [optional] 
**locks** | [**AssignmentLockSettings**](AssignmentLockSettings.md) |  | [optional] 
**parameters** | [**{String: ParameterValue}**](ParameterValue.md) | A dictionary for parameters and their corresponding values. | 
**provisioningState** | **String** | State of the blueprint assignment. | [optional] [readonly] 
**resourceGroups** | [**{String: ResourceGroupValue}**](ResourceGroupValue.md) | A dictionary which maps resource group placeholders to the resource groups which will be created. | 
**status** | [**AssignmentStatus**](AssignmentStatus.md) |  | [optional] 
**description** | **String** | Multi-line explain this resource. | [optional] 
**displayName** | **String** | One-liner string explain this resource. | [optional] 



## Enum: ProvisioningStateEnum


* `creating` (value: `"creating"`)

* `validating` (value: `"validating"`)

* `waiting` (value: `"waiting"`)

* `deploying` (value: `"deploying"`)

* `cancelling` (value: `"cancelling"`)

* `locking` (value: `"locking"`)

* `succeeded` (value: `"succeeded"`)

* `failed` (value: `"failed"`)

* `canceled` (value: `"canceled"`)

* `deleting` (value: `"deleting"`)




