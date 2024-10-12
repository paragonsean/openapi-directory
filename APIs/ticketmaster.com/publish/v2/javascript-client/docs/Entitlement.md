# TicketmasterPublishApi.Entitlement

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | **Object** | The actual entitlements information to add to the entity | 
**relatedEntityId** | **String** | Id of the entity to add this extionsion to. If the relatedEntityId is Null, a relatedEntitySource MUST be provided | [optional] 
**relatedEntitySource** | [**Source**](Source.md) |  | [optional] 
**relatedEntityType** | **String** | The type of the entity to add this entitlement to | 
**source** | **String** | Source of the extension, where it came from | 
**versionNumber** | **Number** | Version of the entitlements. Version is to prevent to override an entitlements with an older one | [optional] 



## Enum: RelatedEntityTypeEnum


* `event` (value: `"event"`)

* `venue` (value: `"venue"`)

* `attraction` (value: `"attraction"`)





## Enum: SourceEnum


* `ticketmaster` (value: `"ticketmaster"`)




