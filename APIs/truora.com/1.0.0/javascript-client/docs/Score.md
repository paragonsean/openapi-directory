# ChecksApi.Score

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**byId** | [**ScoreDetail**](ScoreDetail.md) |  | 
**byName** | [**ScoreDetail**](ScoreDetail.md) |  | 
**dataSet** | **String** | Dataset summed up to create the score | 
**result** | **String** | Overall result of the data collected. If at least one collected data status is found, the result will be found, otherwise, it will be the most frecuent status | [optional] 
**score** | **Number** | Dataset score. Number between 0 and 1 where 1 is the best score. | 
**severity** | **String** | Risk asociated with each category for the search according to the information found. None is returned when the person, vehicle or company is in the clear. Unknown is returned when the score is none due to a problem with one of the searches | 



## Enum: DataSetEnum


* `affiliations_and_insurances` (value: `"affiliations_and_insurances"`)

* `alert_in_media` (value: `"alert_in_media"`)

* `behavior` (value: `"behavior"`)

* `business_background` (value: `"business_background"`)

* `criminal_record` (value: `"criminal_record"`)

* `driving_licenses` (value: `"driving_licenses"`)

* `international_background` (value: `"international_background"`)

* `legal_background` (value: `"legal_background"`)

* `personal_identity` (value: `"personal_identity"`)

* `professional_background` (value: `"professional_background"`)

* `traffic_fines` (value: `"traffic_fines"`)

* `vehicle_information` (value: `"vehicle_information"`)

* `vehicle_permits` (value: `"vehicle_permits"`)

* `taxes_and_finances` (value: `"taxes_and_finances"`)





## Enum: ResultEnum


* `pending` (value: `"pending"`)

* `found` (value: `"found"`)

* `not_found` (value: `"not_found"`)

* `error` (value: `"error"`)

* `delayed` (value: `"delayed"`)

* `ignored` (value: `"ignored"`)





## Enum: SeverityEnum


* `unknown` (value: `"unknown"`)

* `none` (value: `"none"`)

* `very_low` (value: `"very_low"`)

* `low` (value: `"low"`)

* `medium` (value: `"medium"`)

* `high` (value: `"high"`)

* `very_high` (value: `"very_high"`)




