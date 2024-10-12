

# ProximityLocationListAssignedTargetingOptionDetails

Targeting details for proximity location list. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_PROXIMITY_LOCATION_LIST`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**proximityLocationListId** | **String** | Required. ID of the proximity location list. Should refer to the location_list_id field of a LocationList resource whose type is &#x60;TARGETING_LOCATION_TYPE_PROXIMITY&#x60;. |  [optional] |
|**proximityRadius** | **Double** | Required. Radius expressed in the distance units set in proximity_radius_unit. This represents the size of the area around a chosen location that will be targeted. Radius should be between 1 and 500 miles or 800 kilometers. |  [optional] |
|**proximityRadiusUnit** | [**ProximityRadiusUnitEnum**](#ProximityRadiusUnitEnum) | Required. Radius distance units. |  [optional] |



## Enum: ProximityRadiusUnitEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PROXIMITY_RADIUS_UNIT_UNSPECIFIED&quot; |
| MILES | &quot;PROXIMITY_RADIUS_UNIT_MILES&quot; |
| KILOMETERS | &quot;PROXIMITY_RADIUS_UNIT_KILOMETERS&quot; |



