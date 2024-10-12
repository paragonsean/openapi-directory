

# PeeringRegisteredPrefixProperties

The properties that define a registered prefix.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorMessage** | **String** | The error message associated with the validation state, if any. |  [optional] [readonly] |
|**peeringServicePrefixKey** | **String** | The peering service prefix key that is to be shared with the customer. |  [optional] [readonly] |
|**prefix** | **String** | The customer&#39;s prefix from which traffic originates. |  [optional] |
|**prefixValidationState** | [**PrefixValidationStateEnum**](#PrefixValidationStateEnum) | The prefix validation state. |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state of the resource. |  [optional] [readonly] |



## Enum: PrefixValidationStateEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| INVALID | &quot;Invalid&quot; |
| VERIFIED | &quot;Verified&quot; |
| FAILED | &quot;Failed&quot; |
| PENDING | &quot;Pending&quot; |
| WARNING | &quot;Warning&quot; |
| UNKNOWN | &quot;Unknown&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



