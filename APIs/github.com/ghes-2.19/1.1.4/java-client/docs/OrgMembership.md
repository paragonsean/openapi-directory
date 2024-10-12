

# OrgMembership

Org Membership

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**organization** | [**OrganizationSimple**](OrganizationSimple.md) |  |  |
|**organizationUrl** | **URI** |  |  |
|**permissions** | [**OrgMembershipPermissions**](OrgMembershipPermissions.md) |  |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) | The user&#39;s membership type in the organization. |  |
|**state** | [**StateEnum**](#StateEnum) | The state of the member in the organization. The &#x60;pending&#x60; state indicates the user has not yet accepted an invitation. |  |
|**url** | **URI** |  |  |
|**user** | [**NullableSimpleUser**](NullableSimpleUser.md) |  |  |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| ADMIN | &quot;admin&quot; |
| MEMBER | &quot;member&quot; |
| BILLING_MANAGER | &quot;billing_manager&quot; |



## Enum: StateEnum

| Name | Value |
|---- | -----|
| ACTIVE | &quot;active&quot; |
| PENDING | &quot;pending&quot; |



