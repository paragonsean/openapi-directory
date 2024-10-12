

# Client


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | GTM Account ID. |  [optional] |
|**clientId** | **String** | The Client ID uniquely identifies the GTM client. |  [optional] |
|**containerId** | **String** | GTM Container ID. |  [optional] |
|**fingerprint** | **String** | The fingerprint of the GTM Client as computed at storage time. This value is recomputed whenever the client is modified. |  [optional] |
|**name** | **String** | Client display name. @mutable tagmanager.accounts.containers.workspaces.clients.create @mutable tagmanager.accounts.containers.workspaces.clients.update |  [optional] |
|**notes** | **String** | User notes on how to apply this tag in the container. @mutable tagmanager.accounts.containers.workspaces.tags.create @mutable tagmanager.accounts.containers.workspaces.tags.update |  [optional] |
|**parameter** | [**List&lt;Parameter&gt;**](Parameter.md) | The client&#39;s parameters. @mutable tagmanager.accounts.containers.workspaces.clients.create @mutable tagmanager.accounts.containers.workspaces.clients.update |  [optional] |
|**parentFolderId** | **String** | Parent folder id. |  [optional] |
|**path** | **String** | GTM client&#39;s API relative path. |  [optional] |
|**priority** | **Integer** | Priority determines relative firing order. @mutable tagmanager.accounts.containers.workspaces.clients.create @mutable tagmanager.accounts.containers.workspaces.clients.update |  [optional] |
|**tagManagerUrl** | **String** | Auto generated link to the tag manager UI |  [optional] |
|**type** | **String** | Client type. @mutable tagmanager.accounts.containers.workspaces.clients.create @mutable tagmanager.accounts.containers.workspaces.clients.update |  [optional] |
|**workspaceId** | **String** | GTM Workspace ID. |  [optional] |



