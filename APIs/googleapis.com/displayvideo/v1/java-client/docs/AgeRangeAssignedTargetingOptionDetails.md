

# AgeRangeAssignedTargetingOptionDetails

Represents a targetable age range. This will be populated in the details field of an AssignedTargetingOption when targeting_type is `TARGETING_TYPE_AGE_RANGE`.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**ageRange** | [**AgeRangeEnum**](#AgeRangeEnum) | Required. The age range of an audience. We only support targeting a continuous age range of an audience. Thus, the age range represented in this field can be 1) targeted solely, or, 2) part of a larger continuous age range. The reach of a continuous age range targeting can be expanded by also targeting an audience of an unknown age. |  [optional] |
|**targetingOptionId** | **String** | Required. The targeting_option_id of a TargetingOption of type &#x60;TARGETING_TYPE_AGE_RANGE&#x60;. |  [optional] |



## Enum: AgeRangeEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;AGE_RANGE_UNSPECIFIED&quot; |
| _18_24 | &quot;AGE_RANGE_18_24&quot; |
| _25_34 | &quot;AGE_RANGE_25_34&quot; |
| _35_44 | &quot;AGE_RANGE_35_44&quot; |
| _45_54 | &quot;AGE_RANGE_45_54&quot; |
| _55_64 | &quot;AGE_RANGE_55_64&quot; |
| _65_PLUS | &quot;AGE_RANGE_65_PLUS&quot; |
| UNKNOWN | &quot;AGE_RANGE_UNKNOWN&quot; |



