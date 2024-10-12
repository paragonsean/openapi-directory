# SearchAds360ReportingApi.GoogleAdsSearchads360V0CommonTargetRestriction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**bidOnly** | **Boolean** | Indicates whether to restrict your ads to show only for the criteria you have selected for this targeting_dimension, or to target all values for this targeting_dimension and show ads based on your targeting in other TargetingDimensions. A value of &#x60;true&#x60; means that these criteria will only apply bid modifiers, and not affect targeting. A value of &#x60;false&#x60; means that these criteria will restrict targeting as well as applying bid modifiers. | [optional] 
**targetingDimension** | **String** | The targeting dimension that these settings apply to. | [optional] 



## Enum: TargetingDimensionEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `KEYWORD` (value: `"KEYWORD"`)

* `AUDIENCE` (value: `"AUDIENCE"`)

* `TOPIC` (value: `"TOPIC"`)

* `GENDER` (value: `"GENDER"`)

* `AGE_RANGE` (value: `"AGE_RANGE"`)

* `PLACEMENT` (value: `"PLACEMENT"`)

* `PARENTAL_STATUS` (value: `"PARENTAL_STATUS"`)

* `INCOME_RANGE` (value: `"INCOME_RANGE"`)




