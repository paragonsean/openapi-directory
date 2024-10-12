

# ApiManagementServiceIdentity

Identity properties of the Api Management service resource.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**principalId** | **UUID** | The principal id of the identity. |  [optional] [readonly] |
|**tenantId** | **UUID** | The client tenant id of the identity. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | The type of identity used for the resource. The type &#39;SystemAssigned, UserAssigned&#39; includes both an implicitly created identity and a set of user assigned identities. The type &#39;None&#39; will remove any identities from the service. |  |
|**userAssignedIdentities** | [**Map&lt;String, ApiManagementServiceIdentityUserAssignedIdentitiesValue&gt;**](ApiManagementServiceIdentityUserAssignedIdentitiesValue.md) |  |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| SYSTEM_ASSIGNED | &quot;SystemAssigned&quot; |
| USER_ASSIGNED | &quot;UserAssigned&quot; |
| SYSTEM_ASSIGNED_USER_ASSIGNED | &quot;SystemAssigned, UserAssigned&quot; |
| NONE | &quot;None&quot; |



