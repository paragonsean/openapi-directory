

# GoogleAdsSearchads360V0CommonTargetRestriction

The list of per-targeting-dimension targeting settings.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**bidOnly** | **Boolean** | Indicates whether to restrict your ads to show only for the criteria you have selected for this targeting_dimension, or to target all values for this targeting_dimension and show ads based on your targeting in other TargetingDimensions. A value of &#x60;true&#x60; means that these criteria will only apply bid modifiers, and not affect targeting. A value of &#x60;false&#x60; means that these criteria will restrict targeting as well as applying bid modifiers. |  [optional] |
|**targetingDimension** | [**TargetingDimensionEnum**](#TargetingDimensionEnum) | The targeting dimension that these settings apply to. |  [optional] |



## Enum: TargetingDimensionEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| KEYWORD | &quot;KEYWORD&quot; |
| AUDIENCE | &quot;AUDIENCE&quot; |
| TOPIC | &quot;TOPIC&quot; |
| GENDER | &quot;GENDER&quot; |
| AGE_RANGE | &quot;AGE_RANGE&quot; |
| PLACEMENT | &quot;PLACEMENT&quot; |
| PARENTAL_STATUS | &quot;PARENTAL_STATUS&quot; |
| INCOME_RANGE | &quot;INCOME_RANGE&quot; |



