

# PoiAssignedTargetingOptionDetails

Details for assigned POI targeting option. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_POI`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**displayName** | **String** | Output only. The display name of a POI, e.g. \&quot;Times Square\&quot;, \&quot;Space Needle\&quot;, followed by its full address if available. |  [optional] [readonly] |
|**latitude** | **Double** | Output only. Latitude of the POI rounding to 6th decimal place. |  [optional] [readonly] |
|**longitude** | **Double** | Output only. Longitude of the POI rounding to 6th decimal place. |  [optional] [readonly] |
|**proximityRadiusAmount** | **Double** | Required. The radius of the area around the POI that will be targeted. The units of the radius are specified by proximity_radius_unit. Must be 1 to 800 if unit is &#x60;DISTANCE_UNIT_KILOMETERS&#x60; and 1 to 500 if unit is &#x60;DISTANCE_UNIT_MILES&#x60;. |  [optional] |
|**proximityRadiusUnit** | [**ProximityRadiusUnitEnum**](#ProximityRadiusUnitEnum) | Required. The unit of distance by which the targeting radius is measured. |  [optional] |
|**targetingOptionId** | **String** | Required. The targeting_option_id of a TargetingOption of type &#x60;TARGETING_TYPE_POI&#x60;. Accepted POI targeting option IDs can be retrieved using &#x60;targetingTypes.targetingOptions.search&#x60;. If targeting a specific latitude/longitude coordinate removed from an address or POI name, you can generate the necessary targeting option ID by rounding the desired coordinate values to the 6th decimal place, removing the decimals, and concatenating the string values separated by a semicolon. For example, you can target the latitude/longitude pair of 40.7414691, -74.003387 using the targeting option ID \&quot;40741469;-74003387\&quot;. **Upon** **creation, this field value will be updated to append a semicolon and** **alphanumerical hash value if only latitude/longitude coordinates are** **provided.** |  [optional] |



## Enum: ProximityRadiusUnitEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;DISTANCE_UNIT_UNSPECIFIED&quot; |
| MILES | &quot;DISTANCE_UNIT_MILES&quot; |
| KILOMETERS | &quot;DISTANCE_UNIT_KILOMETERS&quot; |



