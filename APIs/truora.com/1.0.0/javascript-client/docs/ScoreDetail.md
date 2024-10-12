# ChecksApi.ScoreDetail

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**result** | **String** | Overall result of the data collected. If at least one collected data status is found, the result will be found, otherwise, it will be the most frecuent status | 
**score** | **Number** | Dataset score. Number between 0 and 1 where 1 is the best score. | 
**severity** | **String** | Risk asociated with each category for the search according to the information found. None is returned when the person, vehicle or company is in the clear. Unknown is returned when the score is none | 



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




