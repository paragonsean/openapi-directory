# PocketSmith.EventsIdPutRequest

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The amount of the event. A positive amount is a credit, and a negative amount is a debit. | [optional] 
**behaviour** | **String** | Whether the update applies only to this event, to all events within the series from this event or to all events within the series. | 
**note** | **String** | A note for the event. | [optional] 
**repeatInterval** | **Number** | The repeat interval of the event. | [optional] 
**repeatType** | **String** | The repeat type of the event. | [optional] 



## Enum: BehaviourEnum


* `one` (value: `"one"`)

* `forward` (value: `"forward"`)

* `all` (value: `"all"`)





## Enum: RepeatTypeEnum


* `once` (value: `"once"`)

* `daily` (value: `"daily"`)

* `weekly` (value: `"weekly"`)

* `fortnightly` (value: `"fortnightly"`)

* `monthly` (value: `"monthly"`)

* `yearly` (value: `"yearly"`)

* `each weekday` (value: `"each weekday"`)




