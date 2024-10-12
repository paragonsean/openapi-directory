

# ProximityLocationListAssignedTargetingOptionDetails

Targeting details for proximity location list. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_PROXIMITY_LOCATION_LIST`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**proximityLocationListId** | **String** | Required. ID of the proximity location list. Should refer to the location_list_id field of a LocationList resource whose type is &#x60;TARGETING_LOCATION_TYPE_PROXIMITY&#x60;. |  [optional] |
|**proximityRadiusRange** | [**ProximityRadiusRangeEnum**](#ProximityRadiusRangeEnum) | Required. Radius range for proximity location list. This represents the size of the area around a chosen location that will be targeted. &#x60;All&#x60; proximity location targeting under a single resource must have the same radius range value. Set this value to match any existing targeting. If updated, this field will change the radius range for all proximity targeting under the resource. |  [optional] |



## Enum: ProximityRadiusRangeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;PROXIMITY_RADIUS_RANGE_UNSPECIFIED&quot; |
| SMALL | &quot;PROXIMITY_RADIUS_RANGE_SMALL&quot; |
| MEDIUM | &quot;PROXIMITY_RADIUS_RANGE_MEDIUM&quot; |
| LARGE | &quot;PROXIMITY_RADIUS_RANGE_LARGE&quot; |



