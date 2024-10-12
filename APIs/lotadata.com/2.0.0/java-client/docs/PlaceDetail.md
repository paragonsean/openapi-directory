

# PlaceDetail


## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ambience** | [**List&lt;FeatureReference&gt;**](FeatureReference.md) | expected mood and feel of the event |  [optional] |
|**category** | [**List&lt;FeatureReference&gt;**](FeatureReference.md) | Associated PlaceCategory. May be multiple (Tier 1) |  [optional] |
|**contact** | [**ContactDetail**](ContactDetail.md) |  |  [optional] |
|**function** | [**List&lt;FeatureReference&gt;**](FeatureReference.md) | PlaceFunction. (Tier 2 taxonomy) |  [optional] |
|**openingHours** | [**List&lt;Timeframe&gt;**](Timeframe.md) |  |  [optional] |
|**photo** | [**List&lt;ImageMeta&gt;**](ImageMeta.md) |  |  [optional] |
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



