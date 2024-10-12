

# ContainerVersion

Represents a Google Tag Manager Container Version.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | GTM Account ID. |  [optional] |
|**container** | [**Container**](Container.md) |  |  [optional] |
|**containerId** | **String** | GTM Container ID. |  [optional] |
|**containerVersionId** | **String** | The Container Version ID uniquely identifies the GTM Container Version. |  [optional] |
|**deleted** | **Boolean** | A value of true indicates this container version has been deleted. |  [optional] |
|**fingerprint** | **String** | The fingerprint of the GTM Container Version as computed at storage time. This value is recomputed whenever the container version is modified. |  [optional] |
|**folder** | [**List&lt;Folder&gt;**](Folder.md) | The folders in the container that this version was taken from. |  [optional] |
|**macro** | [**List&lt;Macro&gt;**](Macro.md) | The macros in the container that this version was taken from. |  [optional] |
|**name** | **String** | Container version display name. @mutable tagmanager.accounts.containers.versions.update |  [optional] |
|**notes** | **String** | User notes on how to apply this container version in the container. @mutable tagmanager.accounts.containers.versions.update |  [optional] |
|**rule** | [**List&lt;Rule&gt;**](Rule.md) | The rules in the container that this version was taken from. |  [optional] |
|**tag** | [**List&lt;Tag&gt;**](Tag.md) | The tags in the container that this version was taken from. |  [optional] |
|**trigger** | [**List&lt;Trigger&gt;**](Trigger.md) | The triggers in the container that this version was taken from. |  [optional] |
|**variable** | [**List&lt;Variable&gt;**](Variable.md) | The variables in the container that this version was taken from. |  [optional] |



