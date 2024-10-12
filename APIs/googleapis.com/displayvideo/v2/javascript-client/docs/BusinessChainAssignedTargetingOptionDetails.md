# DisplayVideo360Api.BusinessChainAssignedTargetingOptionDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**displayName** | **String** | Output only. The display name of a business chain, e.g. \&quot;KFC\&quot;, \&quot;Chase Bank\&quot;. | [optional] [readonly] 
**proximityRadiusAmount** | **Number** | Required. The radius of the area around the business chain that will be targeted. The units of the radius are specified by proximity_radius_unit. Must be 1 to 800 if unit is &#x60;DISTANCE_UNIT_KILOMETERS&#x60; and 1 to 500 if unit is &#x60;DISTANCE_UNIT_MILES&#x60;. The minimum increment for both cases is 0.1. Inputs will be rounded to the nearest acceptable value if it is too granular, e.g. 15.57 will become 15.6. | [optional] 
**proximityRadiusUnit** | **String** | Required. The unit of distance by which the targeting radius is measured. | [optional] 
**targetingOptionId** | **String** | Required. The targeting_option_id of a TargetingOption of type &#x60;TARGETING_TYPE_BUSINESS_CHAIN&#x60;. Accepted business chain targeting option IDs can be retrieved using SearchTargetingOptions. | [optional] 



## Enum: ProximityRadiusUnitEnum


* `UNSPECIFIED` (value: `"DISTANCE_UNIT_UNSPECIFIED"`)

* `MILES` (value: `"DISTANCE_UNIT_MILES"`)

* `KILOMETERS` (value: `"DISTANCE_UNIT_KILOMETERS"`)




