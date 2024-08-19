# AzureDedicatedHsmResourceProvider.DedicatedHsmProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**networkProfile** | [**NetworkProfile**](NetworkProfile.md) |  | [optional] 
**provisioningState** | **String** | Provisioning state. | [optional] [readonly] 
**stampId** | **String** | This field will be used when RP does not support Availability zones. | [optional] 
**statusMessage** | **String** | Resource Status Message. | [optional] [readonly] 



## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Provisioning` (value: `"Provisioning"`)

* `Allocating` (value: `"Allocating"`)

* `Connecting` (value: `"Connecting"`)

* `Failed` (value: `"Failed"`)

* `CheckingQuota` (value: `"CheckingQuota"`)

* `Deleting` (value: `"Deleting"`)




