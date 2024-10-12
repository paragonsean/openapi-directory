

# PropertyModel

Stores the 'Sales' type fields for property ownable as a stepping stone to a full on BO when we finally get the go ahead to write sales!!

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**area** | **String** | The area the property is located in. |  [optional] |
|**branch** | **String** | The branch the block, property or room is assigned to |  [optional] |
|**description** | **String** | The block, property or room description. |  [optional] |
|**etag** | **String** | A unique identifier defining the object and change revision. |  [optional] |
|**fullAddress** | **String** | The full address of a block, property or room, formatted with line breaks such that it may be used on a letter directly. |  [optional] |
|**globalReference** | **String** | The global reference to this block, property or room |  [optional] |
|**mainPhoto** | **String** | Gets the main photo, if there is one. |  [optional] |
|**managedByStaff** | **String** | The staff memeber that manages the block, property or room |  [optional] |
|**OID** | **String** | The unique Object ID (OID). |  [optional] |
|**propertySource** | **String** | The block, property or room source type |  [optional] |
|**propertyType** | [**PropertyTypeEnum**](#PropertyTypeEnum) | The block or property type. |  [optional] |
|**roomName** | **String** | The room name (if applicable). |  [optional] |
|**videoURL** | **String** | URL of the video linked to the property |  [optional] |



## Enum: PropertyTypeEnum

| Name | Value |
|---- | -----|
| HOUSE | &quot;House&quot; |
| FLAT_APARTMENT | &quot;FlatApartment&quot; |
| BUNGALOW | &quot;Bungalow&quot; |
| LAND | &quot;Land&quot; |
| HOUSE_FLAT_SHARE | &quot;HouseFlatShare&quot; |
| GARAGE_PARKING | &quot;GarageParking&quot; |
| COMMERCIAL_PROPERTY | &quot;CommercialProperty&quot; |
| BLOCK | &quot;Block&quot; |
| TERRACED_HOUSE | &quot;TerracedHouse&quot; |
| END_TERRACE_HOUSE | &quot;EndTerraceHouse&quot; |
| SEMI_DETACHED_HOUSE | &quot;SemiDetachedHouse&quot; |
| DETACHED_HOUSE | &quot;DetachedHouse&quot; |
| SEMI_DETACHED_BUNGALOW | &quot;SemiDetachedBungalow&quot; |
| TOWN_HOUSE | &quot;TownHouse&quot; |
| COTTAGE | &quot;Cottage&quot; |
| SERVICED_APARTMENT | &quot;ServicedApartment&quot; |
| STUDIO | &quot;Studio&quot; |
| APARTMENT | &quot;Apartment&quot; |
| BARN | &quot;Barn&quot; |
| FARM_HOUSE | &quot;FarmHouse&quot; |
| PENTHOUSE | &quot;Penthouse&quot; |
| BUILDING_PLOT | &quot;BuildingPlot&quot; |
| DETACHED_BUNGALOW | &quot;DetachedBungalow&quot; |
| LINK_DETACHED | &quot;LinkDetached&quot; |
| MID_TERRACED_BUNGALOW | &quot;MidTerracedBungalow&quot; |
| LAND_RESIDENTIAL | &quot;LandResidential&quot; |



