

# GalleryItemProperties

Properties of a gallery item.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**additionalProperties** | **Map&lt;String, String&gt;** | List of additional properties provided for the item. |  [optional] [readonly] |
|**artifacts** | [**List&lt;Artifact&gt;**](Artifact.md) | List of artifacts for the gallery item. |  [optional] [readonly] |
|**categoryIds** | **List&lt;String&gt;** | List of category IDs the gallery item belongs to. |  [optional] [readonly] |
|**changedTime** | **OffsetDateTime** | Last update time of gallery item. |  [optional] |
|**createdTime** | **OffsetDateTime** | The date and time that the gallery item was created. |  [optional] |
|**definitionTemplates** | [**DefinitionTemplates**](DefinitionTemplates.md) |  |  [optional] |
|**description** | **String** | The description of the gallery item. |  [optional] |
|**filters** | [**List&lt;Filter&gt;**](Filter.md) | List of filters for the gallery item. |  [optional] [readonly] |
|**iconFileUris** | [**GalleryItemPropertiesIconFileUris**](GalleryItemPropertiesIconFileUris.md) |  |  [optional] |
|**identity** | **String** | Identity of the gallery item. |  [optional] |
|**images** | [**List&lt;ImageGroup&gt;**](ImageGroup.md) | List of images. |  [optional] [readonly] |
|**itemDisplayName** | **String** | Displayed name in the portal. |  [optional] |
|**itemName** | **String** | The display name for the gallery item, for the locale of the request. |  [optional] |
|**itemType** | [**ItemTypeEnum**](#ItemTypeEnum) | Describes the type of the gallery item, either GalleryItem or ItemGroup. |  [optional] |
|**links** | [**List&lt;LinkProperties&gt;**](LinkProperties.md) | Links provided for the item. |  [optional] [readonly] |
|**longSummary** | **String** | Long summary of the gallery item. |  [optional] |
|**marketingMaterial** | [**MarketingMaterial**](MarketingMaterial.md) |  |  [optional] |
|**metadata** | [**OpenProperty**](OpenProperty.md) |  |  [optional] |
|**products** | [**List&lt;Product&gt;**](Product.md) | List of products. |  [optional] [readonly] |
|**properties** | **Map&lt;String, String&gt;** | List of properties provided for the gallery item. |  [optional] [readonly] |
|**publisher** | **String** | The publisher of the gallery item. |  [optional] |
|**publisherDisplayName** | **String** | Display name of the publisher. |  [optional] |
|**resourceGroupName** | **String** | Resource group name the gallery item belongs too. |  [optional] |
|**screenshotUris** | **List&lt;String&gt;** | List of screenshot image URIs provided for the item. |  [optional] [readonly] |
|**summary** | **String** | Short summary of the gallery item. |  [optional] |
|**uiDefinitionUri** | **String** | The URL of the view definition object that defines the UI information that is used when an instance of the gallery item resource definition is created. |  [optional] |
|**version** | **String** | The version identifier of the gallery item, in Major.Minor.Build format. |  [optional] |



## Enum: ItemTypeEnum

| Name | Value |
|---- | -----|
| GALLERY_ITEM | &quot;GalleryItem&quot; |
| ITEM_GROUP | &quot;ItemGroup&quot; |



