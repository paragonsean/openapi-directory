

# ContainerAccess

Defines the Google Tag Manager Container access permissions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerId** | **String** | GTM Container ID. @mutable tagmanager.accounts.permissions.create @mutable tagmanager.accounts.permissions.update |  [optional] |
|**permission** | [**PermissionEnum**](#PermissionEnum) | List of Container permissions. @mutable tagmanager.accounts.permissions.create @mutable tagmanager.accounts.permissions.update |  [optional] |



## Enum: PermissionEnum

| Name | Value |
|---- | -----|
| CONTAINER_PERMISSION_UNSPECIFIED | &quot;containerPermissionUnspecified&quot; |
| NO_ACCESS | &quot;noAccess&quot; |
| READ | &quot;read&quot; |
| EDIT | &quot;edit&quot; |
| APPROVE | &quot;approve&quot; |
| PUBLISH | &quot;publish&quot; |



