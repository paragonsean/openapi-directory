

# ImmutabilityPolicyProperty

The properties of an ImmutabilityPolicy of a blob container.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**immutabilityPeriodSinceCreationInDays** | **Integer** | The immutability period for the blobs in the container since the policy creation, in days. |  |
|**state** | [**StateEnum**](#StateEnum) | The ImmutabilityPolicy state of a blob container, possible values include: Locked and Unlocked. |  [optional] [readonly] |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| LOCKED | &quot;Locked&quot; |
| UNLOCKED | &quot;Unlocked&quot; |



