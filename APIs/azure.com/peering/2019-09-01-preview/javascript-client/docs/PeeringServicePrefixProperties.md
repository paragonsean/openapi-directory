# PeeringManagementClient.PeeringServicePrefixProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorMessage** | **String** | The error message for validation state | [optional] [readonly] 
**events** | [**[PeeringServicePrefixEvent]**](PeeringServicePrefixEvent.md) | The list of events for peering service prefix | [optional] [readonly] 
**learnedType** | **String** | The prefix learned type | [optional] [readonly] 
**prefix** | **String** | The prefix from which your traffic originates. | [optional] 
**prefixValidationState** | **String** | The prefix validation state | [optional] [readonly] 
**provisioningState** | **String** | The provisioning state of the resource. | [optional] [readonly] 



## Enum: LearnedTypeEnum


* `None` (value: `"None"`)

* `ViaServiceProvider` (value: `"ViaServiceProvider"`)

* `ViaSession` (value: `"ViaSession"`)





## Enum: PrefixValidationStateEnum


* `None` (value: `"None"`)

* `Invalid` (value: `"Invalid"`)

* `Verified` (value: `"Verified"`)

* `Failed` (value: `"Failed"`)

* `Pending` (value: `"Pending"`)

* `Warning` (value: `"Warning"`)

* `Unknown` (value: `"Unknown"`)





## Enum: ProvisioningStateEnum


* `Succeeded` (value: `"Succeeded"`)

* `Updating` (value: `"Updating"`)

* `Deleting` (value: `"Deleting"`)

* `Failed` (value: `"Failed"`)




