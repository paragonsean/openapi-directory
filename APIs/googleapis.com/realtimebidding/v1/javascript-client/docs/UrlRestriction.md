# RealTimeBiddingApi.UrlRestriction

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**endDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**restrictionType** | **String** | The restriction type for the specified URL. | [optional] 
**startDate** | [**ModelDate**](ModelDate.md) |  | [optional] 
**url** | **String** | Required. The URL to use for applying the restriction on the user list. | [optional] 



## Enum: RestrictionTypeEnum


* `RESTRICTION_TYPE_UNSPECIFIED` (value: `"RESTRICTION_TYPE_UNSPECIFIED"`)

* `CONTAINS` (value: `"CONTAINS"`)

* `EQUALS` (value: `"EQUALS"`)

* `STARTS_WITH` (value: `"STARTS_WITH"`)

* `ENDS_WITH` (value: `"ENDS_WITH"`)

* `DOES_NOT_EQUAL` (value: `"DOES_NOT_EQUAL"`)

* `DOES_NOT_CONTAIN` (value: `"DOES_NOT_CONTAIN"`)

* `DOES_NOT_START_WITH` (value: `"DOES_NOT_START_WITH"`)

* `DOES_NOT_END_WITH` (value: `"DOES_NOT_END_WITH"`)




