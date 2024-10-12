# RocketServices.ItvPlanListItem

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amount** | **Number** | The price of a plan. If a free plan then undefined. | 
**currency** | **String** | The currency a plan is offered in. | 
**description** | **String** | The textual description. | 
**id** | **String** | The identifier of a plan. | 
**interval** | **String** | The type of billing period used. | 
**intervalCount** | **Number** | Given the &#x60;interval&#x60; this is how frequently it will run. e.g. every 2 weeks. | 
**nickname** | **String** | The title of a plan. | 
**product** | **String** | The product description. | 
**savingLabel** | **String** | The saving label. | [optional] 
**switchingText** | **String** | The text to switch for. | [optional] 
**trialPeriodDays** | **Number** | How many days a trial period runs for a plan. Only valid if &#x60;hasTrialPeriod&#x60; is true. | [optional] 



## Enum: IntervalEnum


* `day` (value: `"day"`)

* `week` (value: `"week"`)

* `month` (value: `"month"`)

* `year` (value: `"year"`)

* `none` (value: `"none"`)




