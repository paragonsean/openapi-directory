

# ManagedServiceIdentity

Managed Service Identity

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**principalId** | **String** | Azure Active Directory principal ID associated with this Identity. |  [optional] |
|**tenantId** | **String** | ID of the Azure Active Directory. |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the Managed Service Identity. |  |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| NONE | &quot;None&quot; |
| SYSTEM_ASSIGNED | &quot;SystemAssigned&quot; |
| USER_ASSIGNED | &quot;UserAssigned&quot; |



