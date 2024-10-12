# PocketSmith.Event

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The amount of the event. | [optional] 
**amountInBaseCurrency** | **Number** | The amount of the event in the user&#39;s base currency. | [optional] 
**category** | [**Category**](Category.md) |  | [optional] 
**colour** | **String** | The CSS hex-style colour of the event. | [optional] 
**currencyCode** | **String** | The currency code of the event. | [optional] 
**date** | **String** | The date of the event. | [optional] 
**id** | **String** | The unique identifier of the event. | [optional] 
**infiniteSeries** | **Boolean** | Whether the event repeats and does not have an end date. | [optional] 
**note** | **String** | The note of the event. | [optional] 
**repeatInterval** | **Number** | The repeat interval of how often the event takes place. | [optional] 
**repeatType** | **String** | The repeat type of the event. | [optional] 
**scenario** | [**Scenario**](Scenario.md) |  | [optional] 
**seriesId** | **Number** | The unique identifier of the series that the event belongs to. | [optional] 
**seriesStartId** | **String** | The unique identifier of the series followed by the series&#39;s start date. | [optional] 



## Enum: RepeatTypeEnum


* `once` (value: `"once"`)

* `daily` (value: `"daily"`)

* `weekly` (value: `"weekly"`)

* `fortnightly` (value: `"fortnightly"`)

* `monthly` (value: `"monthly"`)

* `yearly` (value: `"yearly"`)

* `each weekday` (value: `"each weekday"`)




