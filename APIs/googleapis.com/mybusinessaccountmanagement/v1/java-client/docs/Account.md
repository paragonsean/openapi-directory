

# Account

An account is a container for your location. If you are the only user who manages locations for your business, you can use your personal Google Account. To share management of locations with multiple users, [create a business account] (https://support.google.com/business/answer/6085339?ref_topic=6085325).

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountName** | **String** | Required. The name of the account. For an account of type &#x60;PERSONAL&#x60;, this is the first and last name of the user account. |  [optional] |
|**accountNumber** | **String** | Output only. Account reference number if provisioned. |  [optional] [readonly] |
|**name** | **String** | Immutable. The resource name, in the format &#x60;accounts/{account_id}&#x60;. |  [optional] |
|**organizationInfo** | [**OrganizationInfo**](OrganizationInfo.md) |  |  [optional] |
|**permissionLevel** | [**PermissionLevelEnum**](#PermissionLevelEnum) | Output only. Specifies the permission level the user has for this account. |  [optional] [readonly] |
|**primaryOwner** | **String** | Required. Input only. The resource name of the account which will be the primary owner of the account being created. It should be of the form &#x60;accounts/{account_id}&#x60;. |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) | Output only. Specifies the AccountRole of this account. |  [optional] [readonly] |
|**type** | [**TypeEnum**](#TypeEnum) | Required. Contains the type of account. Accounts of type PERSONAL and ORGANIZATION cannot be created using this API. |  [optional] |
|**verificationState** | [**VerificationStateEnum**](#VerificationStateEnum) | Output only. If verified, future locations that are created are automatically connected to Google Maps, and have Google+ pages created, without requiring moderation. |  [optional] [readonly] |
|**vettedState** | [**VettedStateEnum**](#VettedStateEnum) | Output only. Indicates whether the account is vetted by Google. A vetted account is able to verify locations via the VETTED_PARTNER method. |  [optional] [readonly] |



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
| PRIMARY_OWNER | &quot;PRIMARY_OWNER&quot; |
| OWNER | &quot;OWNER&quot; |
| MANAGER | &quot;MANAGER&quot; |
| SITE_MANAGER | &quot;SITE_MANAGER&quot; |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| ACCOUNT_TYPE_UNSPECIFIED | &quot;ACCOUNT_TYPE_UNSPECIFIED&quot; |
| PERSONAL | &quot;PERSONAL&quot; |
| LOCATION_GROUP | &quot;LOCATION_GROUP&quot; |
| USER_GROUP | &quot;USER_GROUP&quot; |
| ORGANIZATION | &quot;ORGANIZATION&quot; |



## Enum: VerificationStateEnum

| Name | Value |
|---- | -----|
| VERIFICATION_STATE_UNSPECIFIED | &quot;VERIFICATION_STATE_UNSPECIFIED&quot; |
| VERIFIED | &quot;VERIFIED&quot; |
| UNVERIFIED | &quot;UNVERIFIED&quot; |
| VERIFICATION_REQUESTED | &quot;VERIFICATION_REQUESTED&quot; |



## Enum: VettedStateEnum

| Name | Value |
|---- | -----|
| VETTED_STATE_UNSPECIFIED | &quot;VETTED_STATE_UNSPECIFIED&quot; |
| NOT_VETTED | &quot;NOT_VETTED&quot; |
| VETTED | &quot;VETTED&quot; |
| INVALID | &quot;INVALID&quot; |



