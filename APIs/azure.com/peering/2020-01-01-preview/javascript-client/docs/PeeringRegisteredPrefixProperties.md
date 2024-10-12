# PeeringManagementClient.PeeringRegisteredPrefixProperties

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errorMessage** | **String** | The error message associated with the validation state, if any. | [optional] [readonly] 
**peeringServicePrefixKey** | **String** | The peering service prefix key that is to be shared with the customer. | [optional] [readonly] 
**prefix** | **String** | The customer&#39;s prefix from which traffic originates. | [optional] 
**prefixValidationState** | **String** | The prefix validation state. | [optional] [readonly] 
**provisioningState** | **String** | The provisioning state of the resource. | [optional] [readonly] 



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




