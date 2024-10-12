# TicketmasterPublishApi.Venue

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**accessibleSeatingDetails** | **{String: String}** | Venue accessible seating details - multi-lingual fields | [optional] 
**active** | **Boolean** | Indicate if the entity is active, inactive entity won&#39;t appear in Discovery API | [optional] [default to false]
**additionalInfos** | **{String: String}** | Additional informations of the entity - multi-lingual fields | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**boxOfficeInfo** | [**VenueBoxOfficeInfo**](VenueBoxOfficeInfo.md) |  | [optional] 
**city** | [**City**](City.md) |  | [optional] 
**country** | [**Country**](Country.md) |  | [optional] 
**currency** | **String** | Default currency of ticket prices for events in this venue | [optional] 
**descriptions** | **{String: String}** | Descriptions of the entity - multi-lingual fields | [optional] 
**discoverable** | **Boolean** | True if the entity is dicoverable in discovery API | [optional] [default to false]
**distance** | **Number** |  | [optional] 
**dma** | [**[Dma]**](Dma.md) | The list of associated DMAs (Designated Market Areas) of the venue | [optional] 
**generalInfo** | [**VenueGeneralInfo**](VenueGeneralInfo.md) |  | [optional] 
**images** | [**[Image]**](Image.md) | Images of the entity | [optional] 
**location** | [**Location**](Location.md) |  | [optional] 
**markets** | [**[Market]**](Market.md) | Markets of the venue | [optional] 
**names** | **{String: String}** | Names of the entity - multi-lingual fields | [optional] 
**parkingDetails** | **{String: String}** | Venue parking info - multi-lingual fields | [optional] 
**postalCode** | **String** | Postal code / zipcode of the venue | [optional] 
**references** | **{String: String}** | References of this entity in an other system. Reference is the exact same entity | [optional] 
**relationships** | **[Object]** | Relationships on the entity, like if the entity is a duplicate of another one | [optional] 
**social** | [**Social**](Social.md) |  | [optional] 
**source** | [**Source**](Source.md) |  | [optional] 
**state** | [**State**](State.md) |  | [optional] 
**test** | **Boolean** | Indicate if this is a test entity, by default test entities won&#39;t appear in discovery API | [optional] [default to false]
**timezone** | **String** | Timezone of the venue | [optional] 
**type** | **String** | Type of the entity | 
**units** | **String** |  | [optional] 
**url** | **String** | URL of a web site detail page of the entity | [optional] 
**version** | **Number** | Version of the entity. Version is to avoid updated an entity with an older version | [optional] 



## Enum: TypeEnum


* `event` (value: `"event"`)

* `venue` (value: `"venue"`)

* `attraction` (value: `"attraction"`)




