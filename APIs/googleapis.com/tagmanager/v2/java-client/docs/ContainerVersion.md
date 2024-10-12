

# ContainerVersion

Represents a Google Tag Manager Container Version.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**accountId** | **String** | GTM Account ID. |  [optional] |
|**builtInVariable** | [**List&lt;BuiltInVariable&gt;**](BuiltInVariable.md) | The built-in variables in the container that this version was taken from. |  [optional] |
|**client** | [**List&lt;Client&gt;**](Client.md) | The clients in the container that this version was taken from. |  [optional] |
|**container** | [**Container**](Container.md) |  |  [optional] |
|**containerId** | **String** | GTM Container ID. |  [optional] |
|**containerVersionId** | **String** | The Container Version ID uniquely identifies the GTM Container Version. |  [optional] |
|**customTemplate** | [**List&lt;CustomTemplate&gt;**](CustomTemplate.md) | The custom templates in the container that this version was taken from. |  [optional] |
|**deleted** | **Boolean** | A value of true indicates this container version has been deleted. |  [optional] |
|**description** | **String** | Container version description. @mutable tagmanager.accounts.containers.versions.update |  [optional] |
|**fingerprint** | **String** | The fingerprint of the GTM Container Version as computed at storage time. This value is recomputed whenever the container version is modified. |  [optional] |
|**folder** | [**List&lt;Folder&gt;**](Folder.md) | The folders in the container that this version was taken from. |  [optional] |
|**gtagConfig** | [**List&lt;GtagConfig&gt;**](GtagConfig.md) | The Google tag configs in the container that this version was taken from. |  [optional] |
|**name** | **String** | Container version display name. @mutable tagmanager.accounts.containers.versions.update |  [optional] |
|**path** | **String** | GTM Container Version&#39;s API relative path. |  [optional] |
|**tag** | [**List&lt;Tag&gt;**](Tag.md) | The tags in the container that this version was taken from. |  [optional] |
|**tagManagerUrl** | **String** | Auto generated link to the tag manager UI |  [optional] |
|**transformation** | [**List&lt;Transformation&gt;**](Transformation.md) | The transformations in the container that this version was taken from. |  [optional] |
|**trigger** | [**List&lt;Trigger&gt;**](Trigger.md) | The triggers in the container that this version was taken from. |  [optional] |
|**variable** | [**List&lt;Variable&gt;**](Variable.md) | The variables in the container that this version was taken from. |  [optional] |
|**zone** | [**List&lt;Zone&gt;**](Zone.md) | The zones in the container that this version was taken from. |  [optional] |



