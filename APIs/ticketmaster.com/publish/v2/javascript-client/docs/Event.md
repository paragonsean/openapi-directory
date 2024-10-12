# TicketmasterPublishApi.Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active** | **Boolean** | Indicate if the entity is active, inactive entity won&#39;t appear in Discovery API | [optional] [default to false]
**additionalInfos** | **{String: String}** | Additional informations of the entity - multi-lingual fields | [optional] 
**attractions** | [**[Attraction]**](Attraction.md) | Ordered Attraction related to the event | [optional] 
**classifications** | [**[Classification]**](Classification.md) | Event&#39;s classifications | [optional] 
**dates** | [**EventDates**](EventDates.md) |  | [optional] 
**descriptions** | **{String: String}** | Descriptions of the entity - multi-lingual fields | [optional] 
**discoverable** | **Boolean** | True if the entity is dicoverable in discovery API | [optional] [default to false]
**distance** | **Number** |  | [optional] 
**images** | [**[Image]**](Image.md) | Images of the entity | [optional] 
**infos** | **{String: String}** | Any information related to the event - multi-lingual fields | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**names** | **{String: String}** | Names of the entity - multi-lingual fields | [optional] 
**place** | [**Place**](Place.md) |  | [optional] 
**pleaseNotes** | **{String: String}** | Any notes related to the event - multi-lingual fields | [optional] 
**priceRanges** | [**[PriceRange]**](PriceRange.md) | Price ranges of this event | [optional] 
**promoter** | [**Promoter**](Promoter.md) |  | [optional] 
**publicVisibility** | [**PublicVisibility**](PublicVisibility.md) |  | [optional] 
**references** | **{String: String}** | References of this entity in an other system. Reference is the exact same entity | [optional] 
**relationships** | **[Object]** | Relationships on the entity, like if the entity is a duplicate of another one | [optional] 
**sales** | [**EventSalesDates**](EventSalesDates.md) |  | [optional] 
**source** | [**Source**](Source.md) |  | [optional] 
**test** | **Boolean** | Indicate if this is a test entity, by default test entities won&#39;t appear in discovery API | [optional] [default to false]
**type** | **String** | Type of the entity | 
**units** | **String** |  | [optional] 
**url** | **String** | URL of a web site detail page of the entity | [optional] 
**venue** | [**Venue**](Venue.md) |  | [optional] 
**version** | **Number** | Version of the entity. Version is to avoid updated an entity with an older version | [optional] 



## Enum: TypeEnum


* `event` (value: `"event"`)

* `venue` (value: `"venue"`)

* `attraction` (value: `"attraction"`)




