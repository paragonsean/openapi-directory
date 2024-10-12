

# AugmentationData

This class defines the Augmentation Data on the Publish API

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**changes** | [**List&lt;Change&gt;**](Change.md) | List of changes to apply to the related entity |  |
|**relatedEntityId** | **String** | Id of the entity to apply the augmentation data. |  |
|**relatedEntityType** | [**RelatedEntityTypeEnum**](#RelatedEntityTypeEnum) | The type of the entity to apply the augmentation data. |  |
|**score** | **Float** | The confidence (%) level of the accuracy of this augmention data. 100 is the better |  [optional] |
|**source** | **String** | The source where the augementation data came from |  |
|**versionNumber** | **Long** | Vesion of this augmentation data. This field is to avoid updating entity with old data.  |  |



## Enum: RelatedEntityTypeEnum

| Name | Value |
|---- | -----|
| EVENT | &quot;event&quot; |
| ATTRACTION | &quot;attraction&quot; |
| VENUE | &quot;venue&quot; |



