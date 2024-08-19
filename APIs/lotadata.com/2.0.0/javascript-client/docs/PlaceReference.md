# LotaData.PlaceReference

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
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




