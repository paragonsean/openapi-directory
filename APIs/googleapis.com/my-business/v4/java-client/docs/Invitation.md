

# Invitation

Output only. Represents a pending invitation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**name** | **String** | The resource name for the invitation. |  [optional] |
|**role** | [**RoleEnum**](#RoleEnum) | The invited role on the account. |  [optional] |
|**targetAccount** | [**Account**](Account.md) |  |  [optional] |
|**targetLocation** | [**TargetLocation**](TargetLocation.md) |  |  [optional] |



## Enum: RoleEnum

| Name | Value |
|---- | -----|
| ADMIN_ROLE_UNSPECIFIED | &quot;ADMIN_ROLE_UNSPECIFIED&quot; |
| OWNER | &quot;OWNER&quot; |
| CO_OWNER | &quot;CO_OWNER&quot; |
| MANAGER | &quot;MANAGER&quot; |
| COMMUNITY_MANAGER | &quot;COMMUNITY_MANAGER&quot; |



