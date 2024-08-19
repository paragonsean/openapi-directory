# RocketServices.EePlanListItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The price of a plan. If a free plan then undefined. | [optional] 
**ctaText** | **String** | The textual description. | 
**currency** | **String** | The currency a plan is offered in. | 
**description** | **String** | The textual description. | 
**headerText** | **String** | The textual description. | 
**heroText** | **String** | The textual description. | 
**id** | **String** | The identifier of a plan. | 
**interval** | **String** | The type of billing period used. | [optional] 
**intervalCount** | **Number** | Given the &#x60;interval&#x60; this is how frequently it will run. e.g. every 2 weeks. | [optional] 
**longText** | **String** | The textual description. | 
**nickname** | **String** | The title of a plan. | 
**product** | **String** | The product of a plan. | 
**trialPeriodDays** | **Number** | How many days a trial period runs for a plan. Only valid if &#x60;hasTrialPeriod&#x60; is true. | 



## Enum: IntervalEnum


* `day` (value: `"day"`)

* `week` (value: `"week"`)

* `month` (value: `"month"`)

* `year` (value: `"year"`)

* `none` (value: `"none"`)




