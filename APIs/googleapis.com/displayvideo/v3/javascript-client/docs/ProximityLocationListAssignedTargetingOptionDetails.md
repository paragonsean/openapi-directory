# DisplayVideo360Api.ProximityLocationListAssignedTargetingOptionDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proximityLocationListId** | **String** | Required. ID of the proximity location list. Should refer to the location_list_id field of a LocationList resource whose type is &#x60;TARGETING_LOCATION_TYPE_PROXIMITY&#x60;. | [optional] 
**proximityRadius** | **Number** | Required. Radius expressed in the distance units set in proximity_radius_unit. This represents the size of the area around a chosen location that will be targeted. Radius should be between 1 and 500 miles or 800 kilometers. | [optional] 
**proximityRadiusUnit** | **String** | Required. Radius distance units. | [optional] 



## Enum: ProximityRadiusUnitEnum


* `UNSPECIFIED` (value: `"PROXIMITY_RADIUS_UNIT_UNSPECIFIED"`)

* `MILES` (value: `"PROXIMITY_RADIUS_UNIT_MILES"`)

* `KILOMETERS` (value: `"PROXIMITY_RADIUS_UNIT_KILOMETERS"`)




