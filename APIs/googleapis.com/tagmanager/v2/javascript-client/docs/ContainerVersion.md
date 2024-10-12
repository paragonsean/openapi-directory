# TagManagerApi.ContainerVersion

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accountId** | **String** | GTM Account ID. | [optional] 
**builtInVariable** | [**[BuiltInVariable]**](BuiltInVariable.md) | The built-in variables in the container that this version was taken from. | [optional] 
**client** | [**[Client]**](Client.md) | The clients in the container that this version was taken from. | [optional] 
**container** | [**Container**](Container.md) |  | [optional] 
**containerId** | **String** | GTM Container ID. | [optional] 
**containerVersionId** | **String** | The Container Version ID uniquely identifies the GTM Container Version. | [optional] 
**customTemplate** | [**[CustomTemplate]**](CustomTemplate.md) | The custom templates in the container that this version was taken from. | [optional] 
**deleted** | **Boolean** | A value of true indicates this container version has been deleted. | [optional] 
**description** | **String** | Container version description. @mutable tagmanager.accounts.containers.versions.update | [optional] 
**fingerprint** | **String** | The fingerprint of the GTM Container Version as computed at storage time. This value is recomputed whenever the container version is modified. | [optional] 
**folder** | [**[Folder]**](Folder.md) | The folders in the container that this version was taken from. | [optional] 
**gtagConfig** | [**[GtagConfig]**](GtagConfig.md) | The Google tag configs in the container that this version was taken from. | [optional] 
**name** | **String** | Container version display name. @mutable tagmanager.accounts.containers.versions.update | [optional] 
**path** | **String** | GTM Container Version&#39;s API relative path. | [optional] 
**tag** | [**[Tag]**](Tag.md) | The tags in the container that this version was taken from. | [optional] 
**tagManagerUrl** | **String** | Auto generated link to the tag manager UI | [optional] 
**transformation** | [**[Transformation]**](Transformation.md) | The transformations in the container that this version was taken from. | [optional] 
**trigger** | [**[Trigger]**](Trigger.md) | The triggers in the container that this version was taken from. | [optional] 
**variable** | [**[Variable]**](Variable.md) | The variables in the container that this version was taken from. | [optional] 
**zone** | [**[Zone]**](Zone.md) | The zones in the container that this version was taken from. | [optional] 


