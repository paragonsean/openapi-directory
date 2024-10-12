

# AccountAccess

Defines the Google Tag Manager Account access permissions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**permission** | [**PermissionEnum**](#PermissionEnum) | Whether the user has no access, user access, or admin access to an account. @mutable tagmanager.accounts.permissions.create @mutable tagmanager.accounts.permissions.update |  [optional] |



## Enum: PermissionEnum

| Name | Value |
|---- | -----|
| ACCOUNT_PERMISSION_UNSPECIFIED | &quot;accountPermissionUnspecified&quot; |
| NO_ACCESS | &quot;noAccess&quot; |
| USER | &quot;user&quot; |
| ADMIN | &quot;admin&quot; |



