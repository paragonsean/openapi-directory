# LotaData.PlaceDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ambience** | [**[FeatureReference]**](FeatureReference.md) | expected mood and feel of the event | [optional] 
**category** | [**[FeatureReference]**](FeatureReference.md) | Associated PlaceCategory. May be multiple (Tier 1) | [optional] 
**contact** | [**ContactDetail**](ContactDetail.md) |  | [optional] 
**_function** | [**[FeatureReference]**](FeatureReference.md) | PlaceFunction. (Tier 2 taxonomy) | [optional] 
**openingHours** | [**[Timeframe]**](Timeframe.md) |  | [optional] 
**photo** | [**[ImageMeta]**](ImageMeta.md) |  | [optional] 
**id** | **String** |  | [optional] 
**type** | **String** | Type of place where Place is a physical address, LocalBusiness is any type of comercial property, AdministrativeArea is a political or colloquial area, and Virtual is out of this world | [optional] 
**address** | [**Address**](Address.md) |  | [optional] 
**geo** | [**GeoPt**](GeoPt.md) |  | [optional] 
**geometry** | **Object** | Shape defined per GeoJSON spec | [optional] 
**location** | [**VirtualLocation**](VirtualLocation.md) |  | [optional] 
**logo** | [**ImageMeta**](ImageMeta.md) |  | [optional] 
**name** | **String** |  | [optional] 
**tag** | [**[FeatureReference]**](FeatureReference.md) |  | [optional] 



## Enum: TypeEnum


* `Place` (value: `"Place"`)

* `LocalBusiness` (value: `"LocalBusiness"`)

* `AdministrativeArea` (value: `"AdministrativeArea"`)

* `TouristAttraction` (value: `"TouristAttraction"`)

* `Landform` (value: `"Landform"`)

* `LandmarksOrHistoricalBuildings` (value: `"LandmarksOrHistoricalBuildings"`)

* `Residence` (value: `"Residence"`)

* `Virtual` (value: `"Virtual"`)




