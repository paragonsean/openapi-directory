

# PlaceReference

Unique Location

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**atId** | **String** |  |  [optional] |
|**atType** | [**AtTypeEnum**](#AtTypeEnum) | Type of place where Place is a physical address, LocalBusiness is any type of comercial property, AdministrativeArea is a political or colloquial area, and Virtual is out of this world |  [optional] |
|**address** | [**Address**](Address.md) |  |  [optional] |
|**geo** | [**GeoPt**](GeoPt.md) |  |  [optional] |
|**geometry** | **Object** | Shape defined per GeoJSON spec |  [optional] |
|**location** | [**VirtualLocation**](VirtualLocation.md) |  |  [optional] |
|**logo** | [**ImageMeta**](ImageMeta.md) |  |  [optional] |
|**name** | **String** |  |  [optional] |
|**tag** | [**List&lt;FeatureReference&gt;**](FeatureReference.md) |  |  [optional] |



## Enum: AtTypeEnum

| Name | Value |
|---- | -----|
| PLACE | &quot;Place&quot; |
| LOCAL_BUSINESS | &quot;LocalBusiness&quot; |
| ADMINISTRATIVE_AREA | &quot;AdministrativeArea&quot; |
| TOURIST_ATTRACTION | &quot;TouristAttraction&quot; |
| LANDFORM | &quot;Landform&quot; |
| LANDMARKS_OR_HISTORICAL_BUILDINGS | &quot;LandmarksOrHistoricalBuildings&quot; |
| RESIDENCE | &quot;Residence&quot; |
| VIRTUAL | &quot;Virtual&quot; |



