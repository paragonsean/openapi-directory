# GitHubV3RestApi.OrgMembership

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**organization** | [**OrganizationSimple**](OrganizationSimple.md) |  | 
**organizationUrl** | **String** |  | 
**permissions** | [**OrgMembershipPermissions**](OrgMembershipPermissions.md) |  | [optional] 
**role** | **String** | The user&#39;s membership type in the organization. | 
**state** | **String** | The state of the member in the organization. The &#x60;pending&#x60; state indicates the user has not yet accepted an invitation. | 
**url** | **String** |  | 
**user** | [**NullableSimpleUser**](NullableSimpleUser.md) |  | 



## Enum: RoleEnum


* `admin` (value: `"admin"`)

* `member` (value: `"member"`)

* `billing_manager` (value: `"billing_manager"`)





## Enum: StateEnum


* `active` (value: `"active"`)

* `pending` (value: `"pending"`)




