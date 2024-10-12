

# Variable

Represents a Google Tag Manager Variable.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | GTM Account ID. |  [optional] |
|**containerId** | **String** | GTM Container ID. |  [optional] |
|**disablingTriggerId** | **List&lt;String&gt;** | For mobile containers only: A list of trigger IDs for disabling conditional variables; the variable is enabled if one of the enabling trigger is true while all the disabling trigger are false. Treated as an unordered set. @mutable tagmanager.accounts.containers.workspaces.variables.create @mutable tagmanager.accounts.containers.workspaces.variables.update |  [optional] |
|**enablingTriggerId** | **List&lt;String&gt;** | For mobile containers only: A list of trigger IDs for enabling conditional variables; the variable is enabled if one of the enabling triggers is true while all the disabling triggers are false. Treated as an unordered set. @mutable tagmanager.accounts.containers.workspaces.variables.create @mutable tagmanager.accounts.containers.workspaces.variables.update |  [optional] |
|**fingerprint** | **String** | The fingerprint of the GTM Variable as computed at storage time. This value is recomputed whenever the variable is modified. |  [optional] |
|**formatValue** | [**VariableFormatValue**](VariableFormatValue.md) |  |  [optional] |
|**name** | **String** | Variable display name. @mutable tagmanager.accounts.containers.workspaces.variables.create @mutable tagmanager.accounts.containers.workspaces.variables.update |  [optional] |
|**notes** | **String** | User notes on how to apply this variable in the container. @mutable tagmanager.accounts.containers.workspaces.variables.create @mutable tagmanager.accounts.containers.workspaces.variables.update |  [optional] |
|**parameter** | [**List&lt;Parameter&gt;**](Parameter.md) | The variable&#39;s parameters. @mutable tagmanager.accounts.containers.workspaces.variables.create @mutable tagmanager.accounts.containers.workspaces.variables.update |  [optional] |
|**parentFolderId** | **String** | Parent folder id. |  [optional] |
|**path** | **String** | GTM Variable&#39;s API relative path. |  [optional] |
|**scheduleEndMs** | **String** | The end timestamp in milliseconds to schedule a variable. @mutable tagmanager.accounts.containers.workspaces.variables.create @mutable tagmanager.accounts.containers.workspaces.variables.update |  [optional] |
|**scheduleStartMs** | **String** | The start timestamp in milliseconds to schedule a variable. @mutable tagmanager.accounts.containers.workspaces.variables.create @mutable tagmanager.accounts.containers.workspaces.variables.update |  [optional] |
|**tagManagerUrl** | **String** | Auto generated link to the tag manager UI |  [optional] |
|**type** | **String** | GTM Variable Type. @mutable tagmanager.accounts.containers.workspaces.variables.create @mutable tagmanager.accounts.containers.workspaces.variables.update |  [optional] |
|**variableId** | **String** | The Variable ID uniquely identifies the GTM Variable. |  [optional] |
|**workspaceId** | **String** | GTM Workspace ID. |  [optional] |



