# ComputeManagementClient.VirtualMachineIdentity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**identityIds** | **[String]** | The list of user identities associated with the Virtual Machine. The user identity references will be ARM resource ids in the form: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/identities/{identityName}&#39;. | [optional] 
**principalId** | **String** | The principal id of virtual machine identity. This property will only be provided for a system assigned identity. | [optional] [readonly] 
**tenantId** | **String** | The tenant id associated with the virtual machine. This property will only be provided for a system assigned identity. | [optional] [readonly] 
**type** | **String** | The type of identity used for the virtual machine. The type &#39;SystemAssigned, UserAssigned&#39; includes both an implicitly created identity and a set of user assigned identities. The type &#39;None&#39; will remove any identities from the virtual machine. | [optional] 



## Enum: TypeEnum


* `SystemAssigned` (value: `"SystemAssigned"`)

* `UserAssigned` (value: `"UserAssigned"`)

* `SystemAssigned, UserAssigned` (value: `"SystemAssigned, UserAssigned"`)

* `None` (value: `"None"`)




