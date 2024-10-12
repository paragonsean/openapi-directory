# DisplayVideo360Api.ProximityLocationListAssignedTargetingOptionDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**proximityLocationListId** | **String** | Required. ID of the proximity location list. Should refer to the location_list_id field of a LocationList resource whose type is &#x60;TARGETING_LOCATION_TYPE_PROXIMITY&#x60;. | [optional] 
**proximityRadiusRange** | **String** | Required. Radius range for proximity location list. This represents the size of the area around a chosen location that will be targeted. &#x60;All&#x60; proximity location targeting under a single resource must have the same radius range value. Set this value to match any existing targeting. If updated, this field will change the radius range for all proximity targeting under the resource. | [optional] 



## Enum: ProximityRadiusRangeEnum


* `UNSPECIFIED` (value: `"PROXIMITY_RADIUS_RANGE_UNSPECIFIED"`)

* `SMALL` (value: `"PROXIMITY_RADIUS_RANGE_SMALL"`)

* `MEDIUM` (value: `"PROXIMITY_RADIUS_RANGE_MEDIUM"`)

* `LARGE` (value: `"PROXIMITY_RADIUS_RANGE_LARGE"`)




