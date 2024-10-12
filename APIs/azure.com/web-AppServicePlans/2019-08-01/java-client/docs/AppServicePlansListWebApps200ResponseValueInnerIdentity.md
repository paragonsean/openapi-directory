

# AppServicePlansListWebApps200ResponseValueInnerIdentity

Managed service identity.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**principalId** | **String** | Principal Id of managed service identity. |  [optional] [readonly] |
|**tenantId** | **String** | Tenant of managed service identity. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of managed service identity. |  [optional] |
|**userAssignedIdentities** | [**Map&lt;String, AppServicePlansListWebApps200ResponseValueInnerIdentityUserAssignedIdentitiesValue&gt;**](AppServicePlansListWebApps200ResponseValueInnerIdentityUserAssignedIdentitiesValue.md) | The list of user assigned identities associated with the resource. The user identity dictionary key references will be ARM resource ids in the form: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName} |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| SYSTEM_ASSIGNED | &quot;SystemAssigned&quot; |
| USER_ASSIGNED | &quot;UserAssigned&quot; |



