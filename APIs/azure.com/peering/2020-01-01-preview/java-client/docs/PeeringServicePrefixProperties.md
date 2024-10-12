

# PeeringServicePrefixProperties

The peering service prefix properties class.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**errorMessage** | **String** | The error message for validation state |  [optional] [readonly] |
|**events** | [**List&lt;PeeringServicePrefixEvent&gt;**](PeeringServicePrefixEvent.md) | The list of events for peering service prefix |  [optional] [readonly] |
|**learnedType** | [**LearnedTypeEnum**](#LearnedTypeEnum) | The prefix learned type |  [optional] [readonly] |
|**peeringServicePrefixKey** | **String** | The peering service prefix key |  [optional] |
|**prefix** | **String** | The prefix from which your traffic originates. |  [optional] |
|**prefixValidationState** | [**PrefixValidationStateEnum**](#PrefixValidationStateEnum) | The prefix validation state |  [optional] [readonly] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state of the resource. |  [optional] [readonly] |



## Enum: LearnedTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| VIA_SERVICE_PROVIDER | &quot;ViaServiceProvider&quot; |
| VIA_SESSION | &quot;ViaSession&quot; |



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



