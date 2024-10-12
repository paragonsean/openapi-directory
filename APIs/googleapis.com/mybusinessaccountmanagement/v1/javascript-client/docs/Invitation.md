# MyBusinessAccountManagementApi.Invitation

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **String** | Required. The resource name for the invitation. &#x60;accounts/{account_id}/invitations/{invitation_id}&#x60;. | [optional] 
**role** | **String** | Output only. The invited role on the account. | [optional] [readonly] 
**targetAccount** | [**Account**](Account.md) |  | [optional] 
**targetLocation** | [**TargetLocation**](TargetLocation.md) |  | [optional] 
**targetType** | **String** | Output only. Specifies which target types should appear in the response. | [optional] [readonly] 



## Enum: RoleEnum


* `ADMIN_ROLE_UNSPECIFIED` (value: `"ADMIN_ROLE_UNSPECIFIED"`)

* `PRIMARY_OWNER` (value: `"PRIMARY_OWNER"`)

* `OWNER` (value: `"OWNER"`)

* `MANAGER` (value: `"MANAGER"`)

* `SITE_MANAGER` (value: `"SITE_MANAGER"`)





## Enum: TargetTypeEnum


* `TARGET_TYPE_UNSPECIFIED` (value: `"TARGET_TYPE_UNSPECIFIED"`)

* `ACCOUNTS_ONLY` (value: `"ACCOUNTS_ONLY"`)

* `LOCATIONS_ONLY` (value: `"LOCATIONS_ONLY"`)




