

# VirtualMachineScaleSetIdentity

Identity for the virtual machine scale set.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**principalId** | **String** | The principal id of virtual machine scale set identity. This property will only be provided for a system assigned identity. |  [optional] [readonly] |
|**tenantId** | **String** | The tenant id associated with the virtual machine scale set. This property will only be provided for a system assigned identity. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of identity used for the virtual machine scale set. The type &#39;SystemAssigned, UserAssigned&#39; includes both an implicitly created identity and a set of user assigned identities. The type &#39;None&#39; will remove any identities from the virtual machine scale set. |  [optional] |
|**userAssignedIdentities** | [**Map&lt;String, VirtualMachineIdentityUserAssignedIdentitiesValue&gt;**](VirtualMachineIdentityUserAssignedIdentitiesValue.md) | The list of user identities associated with the virtual machine scale set. The user identity dictionary key references will be ARM resource ids in the form: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}&#39;. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SYSTEM_ASSIGNED | &quot;SystemAssigned&quot; |
| USER_ASSIGNED | &quot;UserAssigned&quot; |
| SYSTEM_ASSIGNED_USER_ASSIGNED | &quot;SystemAssigned, UserAssigned&quot; |
| NONE | &quot;None&quot; |



