# BatchService.NodeAgentSku

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **String** | The node agent SKU id. | [optional] 
**osType** | **String** | The type of operating system compatible with the node agent SKU. | [optional] 
**verifiedImageReferences** | [**[ImageReference]**](ImageReference.md) | The list of images verified to be compatible with this node agent SKU. This collection is not exhaustive (the node agent may be compatible with other images). | [optional] 



## Enum: OsTypeEnum


* `linux` (value: `"linux"`)

* `windows` (value: `"windows"`)

* `unmapped` (value: `"unmapped"`)




