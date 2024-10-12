

# Event

Event

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**active** | **Boolean** | Indicate if the entity is active, inactive entity won&#39;t appear in Discovery API |  [optional] |
|**additionalInfos** | **Map&lt;String, String&gt;** | Additional informations of the entity - multi-lingual fields |  [optional] |
|**attractions** | [**List&lt;Attraction&gt;**](Attraction.md) | Ordered Attraction related to the event |  [optional] |
|**classifications** | [**List&lt;Classification&gt;**](Classification.md) | Event&#39;s classifications |  [optional] |
|**dates** | [**EventDates**](EventDates.md) |  |  [optional] |
|**descriptions** | **Map&lt;String, String&gt;** | Descriptions of the entity - multi-lingual fields |  [optional] |
|**discoverable** | **Boolean** | True if the entity is dicoverable in discovery API |  [optional] |
|**distance** | **Double** |  |  [optional] |
|**images** | [**Set&lt;Image&gt;**](Image.md) | Images of the entity |  [optional] |
|**infos** | **Map&lt;String, String&gt;** | Any information related to the event - multi-lingual fields |  [optional] |
|**location** | [**Location**](Location.md) |  |  [optional] |
|**names** | **Map&lt;String, String&gt;** | Names of the entity - multi-lingual fields |  [optional] |
|**place** | [**Place**](Place.md) |  |  [optional] |
|**pleaseNotes** | **Map&lt;String, String&gt;** | Any notes related to the event - multi-lingual fields |  [optional] |
|**priceRanges** | [**Set&lt;PriceRange&gt;**](PriceRange.md) | Price ranges of this event |  [optional] |
|**promoter** | [**Promoter**](Promoter.md) |  |  [optional] |
|**publicVisibility** | [**PublicVisibility**](PublicVisibility.md) |  |  [optional] |
|**references** | **Map&lt;String, String&gt;** | References of this entity in an other system. Reference is the exact same entity |  [optional] |
|**relationships** | **List&lt;Object&gt;** | Relationships on the entity, like if the entity is a duplicate of another one |  [optional] |
|**sales** | [**EventSalesDates**](EventSalesDates.md) |  |  [optional] |
|**source** | [**Source**](Source.md) |  |  [optional] |
|**test** | **Boolean** | Indicate if this is a test entity, by default test entities won&#39;t appear in discovery API |  [optional] |
|**type** | [**TypeEnum**](#TypeEnum) | Type of the entity |  |
|**units** | **String** |  |  [optional] |
|**url** | **String** | URL of a web site detail page of the entity |  [optional] |
|**venue** | [**Venue**](Venue.md) |  |  [optional] |
|**version** | **Long** | Version of the entity. Version is to avoid updated an entity with an older version |  [optional] |



## Enum: TypeEnum

| Name | Value |
|---- | -----|
| EVENT | &quot;event&quot; |
| VENUE | &quot;venue&quot; |
| ATTRACTION | &quot;attraction&quot; |



