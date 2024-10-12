# PeeringManagementClient.PeeringServicePrefixProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**learnedType** | **String** | The prefix learned type | [optional] 
**prefix** | **String** | Valid route prefix | [optional] 
**prefixValidationState** | **String** | The prefix validation state | [optional] 
**provisioningState** | **String** | The provisioning state of the resource. | [optional] [readonly] 



## Enum: LearnedTypeEnum


* `None` (value: `"None"`)

* `ViaPartner` (value: `"ViaPartner"`)

* `ViaSession` (value: `"ViaSession"`)





## Enum: PrefixValidationStateEnum


* `None` (value: `"None"`)

* `Invalid` (value: `"Invalid"`)

* `Verified` (value: `"Verified"`)

* `Failed` (value: `"Failed"`)

* `Pending` (value: `"Pending"`)

* `Unknown` (value: `"Unknown"`)





## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




