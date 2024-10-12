# GoogleMyBusinessApi.Account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountName** | **String** | The name of the account. *Note:* For an account with AccountType &#x60;PERSONAL&#x60;, this is the first and last name of the user account. | [optional] 
**accountNumber** | **String** | Account reference number if provisioned. | [optional] 
**name** | **String** | The resource name, in the format &#x60;accounts/{account_id}&#x60;. | [optional] 
**organizationInfo** | [**OrganizationInfo**](OrganizationInfo.md) |  | [optional] 
**permissionLevel** | **String** | Output only. Specifies the PermissionLevel the caller has for this account. | [optional] 
**role** | **String** | Output only. Specifies the AccountRole the caller has for this account. | [optional] 
**state** | [**AccountState**](AccountState.md) |  | [optional] 
**type** | **String** | Output only. Specifies the AccountType of this account. | [optional] 



## Enum: PermissionLevelEnum


* `PERMISSION_LEVEL_UNSPECIFIED` (value: `"PERMISSION_LEVEL_UNSPECIFIED"`)

* `OWNER_LEVEL` (value: `"OWNER_LEVEL"`)

* `MEMBER_LEVEL` (value: `"MEMBER_LEVEL"`)





## Enum: RoleEnum


* `ACCOUNT_ROLE_UNSPECIFIED` (value: `"ACCOUNT_ROLE_UNSPECIFIED"`)

* `OWNER` (value: `"OWNER"`)

* `CO_OWNER` (value: `"CO_OWNER"`)

* `MANAGER` (value: `"MANAGER"`)

* `COMMUNITY_MANAGER` (value: `"COMMUNITY_MANAGER"`)





## Enum: TypeEnum


* `ACCOUNT_TYPE_UNSPECIFIED` (value: `"ACCOUNT_TYPE_UNSPECIFIED"`)

* `PERSONAL` (value: `"PERSONAL"`)

* `LOCATION_GROUP` (value: `"LOCATION_GROUP"`)

* `USER_GROUP` (value: `"USER_GROUP"`)

* `ORGANIZATION` (value: `"ORGANIZATION"`)




