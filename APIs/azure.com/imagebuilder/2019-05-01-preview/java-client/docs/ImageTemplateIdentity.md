

# ImageTemplateIdentity

Identity for the image template.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**type** | [**TypeEnum**](#TypeEnum) | The type of identity used for the image template. The type &#39;None&#39; will remove any identities from the image template. |  [optional] |
|**userAssignedIdentities** | [**Map&lt;String, ImageTemplateIdentityUserAssignedIdentitiesValue&gt;**](ImageTemplateIdentityUserAssignedIdentitiesValue.md) | The list of user identities associated with the image template. The user identity dictionary key references will be ARM resource ids in the form: &#39;/subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/Microsoft.ManagedIdentity/userAssignedIdentities/{identityName}&#39;. |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| USER_ASSIGNED | &quot;UserAssigned&quot; |
| NONE | &quot;None&quot; |



