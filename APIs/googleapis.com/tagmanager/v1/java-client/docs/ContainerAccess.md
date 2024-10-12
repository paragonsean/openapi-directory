

# ContainerAccess

Defines the Google Tag Manager Container access permissions.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**containerId** | **String** | GTM Container ID. @mutable tagmanager.accounts.permissions.create @mutable tagmanager.accounts.permissions.update |  [optional] |
|**permission** | [**List&lt;PermissionEnum&gt;**](#List&lt;PermissionEnum&gt;) | List of Container permissions. Valid container permissions are: read, edit, delete, publish. @mutable tagmanager.accounts.permissions.create @mutable tagmanager.accounts.permissions.update |  [optional] |



## Enum: List&lt;PermissionEnum&gt;

| Name | Value |
|---- | -----|
| READ | &quot;read&quot; |
| EDIT | &quot;edit&quot; |
| PUBLISH | &quot;publish&quot; |
| DELETE | &quot;delete&quot; |
| MANAGE | &quot;manage&quot; |
| EDIT_WORKSPACE | &quot;editWorkspace&quot; |



