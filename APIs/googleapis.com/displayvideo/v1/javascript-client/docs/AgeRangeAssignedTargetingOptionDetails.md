# DisplayVideo360Api.AgeRangeAssignedTargetingOptionDetails

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ageRange** | **String** | Required. The age range of an audience. We only support targeting a continuous age range of an audience. Thus, the age range represented in this field can be 1) targeted solely, or, 2) part of a larger continuous age range. The reach of a continuous age range targeting can be expanded by also targeting an audience of an unknown age. | [optional] 
**targetingOptionId** | **String** | Required. The targeting_option_id of a TargetingOption of type &#x60;TARGETING_TYPE_AGE_RANGE&#x60;. | [optional] 



## Enum: AgeRangeEnum


* `UNSPECIFIED` (value: `"AGE_RANGE_UNSPECIFIED"`)

* `18_24` (value: `"AGE_RANGE_18_24"`)

* `25_34` (value: `"AGE_RANGE_25_34"`)

* `35_44` (value: `"AGE_RANGE_35_44"`)

* `45_54` (value: `"AGE_RANGE_45_54"`)

* `55_64` (value: `"AGE_RANGE_55_64"`)

* `65_PLUS` (value: `"AGE_RANGE_65_PLUS"`)

* `UNKNOWN` (value: `"AGE_RANGE_UNKNOWN"`)




