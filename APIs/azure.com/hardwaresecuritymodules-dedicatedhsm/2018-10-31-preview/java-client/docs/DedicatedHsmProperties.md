

# DedicatedHsmProperties

Properties of the dedicated hsm

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**networkProfile** | [**NetworkProfile**](NetworkProfile.md) |  |  [optional] |
|**provisioningState** | [**ProvisioningStateEnum**](#ProvisioningStateEnum) | Provisioning state. |  [optional] [readonly] |
|**stampId** | **String** | This field will be used when RP does not support Availability zones. |  [optional] |
|**statusMessage** | **String** | Resource Status Message. |  [optional] [readonly] |



## Enum: ProvisioningStateEnum

| Name | Value |
|---- | -----|
| SUCCEEDED | &quot;Succeeded&quot; |
| PROVISIONING | &quot;Provisioning&quot; |
| ALLOCATING | &quot;Allocating&quot; |
| CONNECTING | &quot;Connecting&quot; |
| FAILED | &quot;Failed&quot; |
| CHECKING_QUOTA | &quot;CheckingQuota&quot; |
| DELETING | &quot;Deleting&quot; |



