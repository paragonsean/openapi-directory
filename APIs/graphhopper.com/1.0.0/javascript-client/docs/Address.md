# GraphHopperDirectionsApi.Address

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**curbside** | **String** | Optional parameter. Specifies on which side a point should be relative to the driver when she leaves/arrives at a start/target/via point. Only supported for motor vehicles and OpenStreetMap. | [optional] [default to &#39;any&#39;]
**lat** | **Number** | Latitude of location. | 
**locationId** | **String** | Specifies the id of the location. | 
**lon** | **Number** | Longitude of location. | 
**name** | **String** | Name of location. | [optional] 
**streetHint** | **String** | Optional parameter. Specifies a hint for each address to better snap the coordinates (lon,lat) to road network. E.g. if there is an address or house with two or more neighboring streets you can control for which street the closest location is looked up. | [optional] 



## Enum: CurbsideEnum


* `right` (value: `"right"`)

* `left` (value: `"left"`)

* `any` (value: `"any"`)




