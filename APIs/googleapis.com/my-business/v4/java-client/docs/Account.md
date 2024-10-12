

# Account

An account is a container for your business's locations. If you are the only user who manages locations for your business, you can use your personal Google Account. To share management of locations with multiple users, [create a business account] (https://support.google.com/business/answer/6085339?ref_topic=6085325).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountName** | **String** | The name of the account. *Note:* For an account with AccountType &#x60;PERSONAL&#x60;, this is the first and last name of the user account. |  [optional] |
|**accountNumber** | **String** | Account reference number if provisioned. |  [optional] |
|**name** | **String** | The resource name, in the format &#x60;accounts/{account_id}&#x60;. |  [optional] |
|**organizationInfo** | [**OrganizationInfo**](OrganizationInfo.md) |  |  [optional] |
|**permissionLevel** | [**PermissionLevelEnum**](#PermissionLevelEnum) | Output only. Specifies the PermissionLevel the caller has for this account. |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) | Output only. Specifies the AccountRole the caller has for this account. |  [optional] |
|**state** | [**AccountState**](AccountState.md) |  |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Output only. Specifies the AccountType of this account. |  [optional] |



## Enum: PermissionLevelEnum

| Name | Value |
|---- | -----|
| PERMISSION_LEVEL_UNSPECIFIED | &quot;PERMISSION_LEVEL_UNSPECIFIED&quot; |
| OWNER_LEVEL | &quot;OWNER_LEVEL&quot; |
| MEMBER_LEVEL | &quot;MEMBER_LEVEL&quot; |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| ACCOUNT_ROLE_UNSPECIFIED | &quot;ACCOUNT_ROLE_UNSPECIFIED&quot; |
| OWNER | &quot;OWNER&quot; |
| CO_OWNER | &quot;CO_OWNER&quot; |
| MANAGER | &quot;MANAGER&quot; |
| COMMUNITY_MANAGER | &quot;COMMUNITY_MANAGER&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ACCOUNT_TYPE_UNSPECIFIED | &quot;ACCOUNT_TYPE_UNSPECIFIED&quot; |
| PERSONAL | &quot;PERSONAL&quot; |
| LOCATION_GROUP | &quot;LOCATION_GROUP&quot; |
| USER_GROUP | &quot;USER_GROUP&quot; |
| ORGANIZATION | &quot;ORGANIZATION&quot; |



