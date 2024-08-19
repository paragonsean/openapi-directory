# MyBusinessAccountManagementApi.Account

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountName** | **String** | Required. The name of the account. For an account of type &#x60;PERSONAL&#x60;, this is the first and last name of the user account. | [optional] 
**accountNumber** | **String** | Output only. Account reference number if provisioned. | [optional] [readonly] 
**name** | **String** | Immutable. The resource name, in the format &#x60;accounts/{account_id}&#x60;. | [optional] 
**organizationInfo** | [**OrganizationInfo**](OrganizationInfo.md) |  | [optional] 
**permissionLevel** | **String** | Output only. Specifies the permission level the user has for this account. | [optional] [readonly] 
**primaryOwner** | **String** | Required. Input only. The resource name of the account which will be the primary owner of the account being created. It should be of the form &#x60;accounts/{account_id}&#x60;. | [optional] 
**role** | **String** | Output only. Specifies the AccountRole of this account. | [optional] [readonly] 
**type** | **String** | Required. Contains the type of account. Accounts of type PERSONAL and ORGANIZATION cannot be created using this API. | [optional] 
**verificationState** | **String** | Output only. If verified, future locations that are created are automatically connected to Google Maps, and have Google+ pages created, without requiring moderation. | [optional] [readonly] 
**vettedState** | **String** | Output only. Indicates whether the account is vetted by Google. A vetted account is able to verify locations via the VETTED_PARTNER method. | [optional] [readonly] 



## Enum: PermissionLevelEnum


* `PERMISSION_LEVEL_UNSPECIFIED` (value: `"PERMISSION_LEVEL_UNSPECIFIED"`)

* `OWNER_LEVEL` (value: `"OWNER_LEVEL"`)

* `MEMBER_LEVEL` (value: `"MEMBER_LEVEL"`)





## Enum: RoleEnum


* `ACCOUNT_ROLE_UNSPECIFIED` (value: `"ACCOUNT_ROLE_UNSPECIFIED"`)

* `PRIMARY_OWNER` (value: `"PRIMARY_OWNER"`)

* `OWNER` (value: `"OWNER"`)

* `MANAGER` (value: `"MANAGER"`)

* `SITE_MANAGER` (value: `"SITE_MANAGER"`)





## Enum: TypeEnum


* `ACCOUNT_TYPE_UNSPECIFIED` (value: `"ACCOUNT_TYPE_UNSPECIFIED"`)

* `PERSONAL` (value: `"PERSONAL"`)

* `LOCATION_GROUP` (value: `"LOCATION_GROUP"`)

* `USER_GROUP` (value: `"USER_GROUP"`)

* `ORGANIZATION` (value: `"ORGANIZATION"`)





## Enum: VerificationStateEnum


* `VERIFICATION_STATE_UNSPECIFIED` (value: `"VERIFICATION_STATE_UNSPECIFIED"`)

* `VERIFIED` (value: `"VERIFIED"`)

* `UNVERIFIED` (value: `"UNVERIFIED"`)

* `VERIFICATION_REQUESTED` (value: `"VERIFICATION_REQUESTED"`)





## Enum: VettedStateEnum


* `VETTED_STATE_UNSPECIFIED` (value: `"VETTED_STATE_UNSPECIFIED"`)

* `NOT_VETTED` (value: `"NOT_VETTED"`)

* `VETTED` (value: `"VETTED"`)

* `INVALID` (value: `"INVALID"`)




