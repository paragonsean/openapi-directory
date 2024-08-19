

# VirtualMachineScaleSetIdentity

Identity for the virtual machine scale set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**principalId** | **String** | The principal id of virtual machine scale set identity. |  [optional] [readonly] |
|**tenantId** | **String** | The tenant id associated with the virtual machine scale set. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of identity used for the virtual machine scale set. Currently, the only supported type is &#39;SystemAssigned&#39;, which implicitly creates an identity. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SYSTEM_ASSIGNED | &quot;SystemAssigned&quot; |



