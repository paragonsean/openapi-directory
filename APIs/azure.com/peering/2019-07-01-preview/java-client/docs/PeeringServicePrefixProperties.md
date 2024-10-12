

# PeeringServicePrefixProperties

The peering service prefix properties class.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**learnedType** | [**LearnedTypeEnum**](#LearnedTypeEnum) | The prefix learned type |  [optional] |
|**prefix** | **String** | Valid route prefix |  [optional] |
|**prefixValidationState** | [**PrefixValidationStateEnum**](#PrefixValidationStateEnum) | The prefix validation state |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | The provisioning state of the resource. |  [optional] [readonly] |



## Enum: LearnedTypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| VIA_PARTNER | &quot;ViaPartner&quot; |
| VIA_SESSION | &quot;ViaSession&quot; |



## Enum: PrefixValidationStateEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| INVALID | &quot;Invalid&quot; |
| VERIFIED | &quot;Verified&quot; |
| FAILED | &quot;Failed&quot; |
| PENDING | &quot;Pending&quot; |
| UNKNOWN | &quot;Unknown&quot; |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| UPDATING | &quot;Updating&quot; |
| DELETING | &quot;Deleting&quot; |
| FAILED | &quot;Failed&quot; |



