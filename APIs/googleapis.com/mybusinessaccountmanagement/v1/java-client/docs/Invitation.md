

# Invitation

Represents a pending invitation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | Required. The resource name for the invitation. &#x60;accounts/{account_id}/invitations/{invitation_id}&#x60;. |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) | Output only. The invited role on the account. |  [optional] [readonly] |
|**targetAccount** | [**Account**](Account.md) |  |  [optional] |
|**targetLocation** | [**TargetLocation**](TargetLocation.md) |  |  [optional] |
|**targetType** | [**TargetTypeEnum**](#TargetTypeEnum) | Output only. Specifies which target types should appear in the response. |  [optional] [readonly] |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| ADMIN_ROLE_UNSPECIFIED | &quot;ADMIN_ROLE_UNSPECIFIED&quot; |
| PRIMARY_OWNER | &quot;PRIMARY_OWNER&quot; |
| OWNER | &quot;OWNER&quot; |
| MANAGER | &quot;MANAGER&quot; |
| SITE_MANAGER | &quot;SITE_MANAGER&quot; |



## Enum: TargetTypeEnum

| Name | Value |
|---- | -----|
| TARGET_TYPE_UNSPECIFIED | &quot;TARGET_TYPE_UNSPECIFIED&quot; |
| ACCOUNTS_ONLY | &quot;ACCOUNTS_ONLY&quot; |
| LOCATIONS_ONLY | &quot;LOCATIONS_ONLY&quot; |



