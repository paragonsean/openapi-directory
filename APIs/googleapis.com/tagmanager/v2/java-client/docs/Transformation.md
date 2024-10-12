

# Transformation

Represents a Google Tag Manager Transformation.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | GTM Account ID. |  [optional] |
|**containerId** | **String** | GTM Container ID. |  [optional] |
|**fingerprint** | **String** | The fingerprint of the GTM Transformation as computed at storage time. This value is recomputed whenever the transformation is modified. |  [optional] |
|**name** | **String** | Transformation display name. @mutable tagmanager.accounts.containers.workspaces.transformations.create @mutable tagmanager.accounts.containers.workspaces.transformations.update |  [optional] |
|**notes** | **String** | User notes on how to apply this transformation in the container. @mutable tagmanager.accounts.containers.workspaces.transformations.create @mutable tagmanager.accounts.containers.workspaces.transformations.update |  [optional] |
|**parameter** | [**List&lt;Parameter&gt;**](Parameter.md) | The transformation&#39;s parameters. @mutable tagmanager.accounts.containers.workspaces.transformations.create @mutable tagmanager.accounts.containers.workspaces.transformations.update |  [optional] |
|**parentFolderId** | **String** | Parent folder id. |  [optional] |
|**path** | **String** | GTM transformation&#39;s API relative path. |  [optional] |
|**tagManagerUrl** | **String** | Auto generated link to the tag manager UI |  [optional] |
|**transformationId** | **String** | The Transformation ID uniquely identifies the GTM transformation. |  [optional] |
|**type** | **String** | Transformation type. @mutable tagmanager.accounts.containers.workspaces.transformations.create @mutable tagmanager.accounts.containers.workspaces.transformations.update |  [optional] |
|**workspaceId** | **String** | GTM Workspace ID. |  [optional] |



