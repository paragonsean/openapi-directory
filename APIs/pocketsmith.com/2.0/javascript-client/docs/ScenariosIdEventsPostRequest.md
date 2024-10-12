# PocketSmith.ScenariosIdEventsPostRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The amount of the event. A positive amount is a credit, and a negative amount is a debit. | 
**categoryId** | **Number** | The unique identifier of the category for the event. | 
**date** | **String** | The starting date of the event. | 
**note** | **String** | A note for the event. | [optional] 
**repeatInterval** | **Number** | The repeat interval of the event. | [optional] [default to 1]
**repeatType** | **String** | The repeat type of the event. | 



## Enum: RepeatTypeEnum


* `once` (value: `"once"`)

* `daily` (value: `"daily"`)

* `weekly` (value: `"weekly"`)

* `fortnightly` (value: `"fortnightly"`)

* `monthly` (value: `"monthly"`)

* `yearly` (value: `"yearly"`)

* `each weekday` (value: `"each weekday"`)




