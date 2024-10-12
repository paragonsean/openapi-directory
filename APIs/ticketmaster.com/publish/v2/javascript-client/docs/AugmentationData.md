# TicketmasterPublishApi.AugmentationData

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**changes** | [**[Change]**](Change.md) | List of changes to apply to the related entity | 
**relatedEntityId** | **String** | Id of the entity to apply the augmentation data. | 
**relatedEntityType** | **String** | The type of the entity to apply the augmentation data. | 
**score** | **Number** | The confidence (%) level of the accuracy of this augmention data. 100 is the better | [optional] 
**source** | **String** | The source where the augementation data came from | 
**versionNumber** | **Number** | Vesion of this augmentation data. This field is to avoid updating entity with old data.  | 



## Enum: RelatedEntityTypeEnum


* `event` (value: `"event"`)

* `attraction` (value: `"attraction"`)

* `venue` (value: `"venue"`)




