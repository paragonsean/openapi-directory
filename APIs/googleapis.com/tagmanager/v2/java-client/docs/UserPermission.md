

# UserPermission

Represents a user's permissions to an account and its container.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountAccess** | [**AccountAccess**](AccountAccess.md) |  |  [optional] |
|**accountId** | **String** | The Account ID uniquely identifies the GTM Account. |  [optional] |
|**containerAccess** | [**List&lt;ContainerAccess&gt;**](ContainerAccess.md) | GTM Container access permissions. @mutable tagmanager.accounts.permissions.create @mutable tagmanager.accounts.permissions.update |  [optional] |
|**emailAddress** | **String** | User&#39;s email address. @mutable tagmanager.accounts.permissions.create |  [optional] |
|**path** | **String** | GTM UserPermission&#39;s API relative path. |  [optional] |



