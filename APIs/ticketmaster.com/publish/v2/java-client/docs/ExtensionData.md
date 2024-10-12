

# ExtensionData

This class defines an extenstion data on the Publish API

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**data** | **Object** | The actual information to add to the entity |  |
|**relatedEntityId** | **String** | Id of the entity to add this extionsion to. If the relatedEntityId is Null, a relatedEntitySource MUST be provided |  [optional] |
|**relatedEntitySource** | [**Source**](Source.md) |  |  [optional] |
|**relatedEntityType** | [**RelatedEntityTypeEnum**](#RelatedEntityTypeEnum) | The type of the entity to add this extensions to |  |
|**source** | **String** | Source of the extension, where it came from |  |
|**type** | **String** | The type of the extension. This represent the data sent |  |
|**versionNumber** | **Long** | Version of the extensions. Version is to prevent to override an extension with an older one |  [optional] |



## Enum: RelatedEntityTypeEnum

| Name | Value |
|---- | -----|
| EVENT | &quot;event&quot; |
| VENUE | &quot;venue&quot; |
| ATTRACTION | &quot;attraction&quot; |



