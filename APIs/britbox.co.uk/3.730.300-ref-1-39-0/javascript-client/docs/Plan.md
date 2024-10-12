# RocketServices.Plan

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alias** | **String** | An alias for a plan. | 
**benefits** | **[String]** | The list of benefits to display for a plan. | 
**billingPeriodFrequency** | **Number** | Given the &#x60;billingPeriodType&#x60; this is how frequently it will run. e.g. every 2 weeks. | 
**billingPeriodType** | **String** | The type of billing period used. | 
**currency** | **String** | The currency a plan is offered in. | 
**customFields** | **{String: Object}** | A map of custom fields defined by a curator for a plan. | [optional] 
**hasTrialPeriod** | **Boolean** | True if a plan has a trial period, false if not. | 
**id** | **String** | The identifier of a plan. | 
**isActive** | **Boolean** | True if a plan is active, false if its retired. | 
**isFeatured** | **Boolean** | True if a plan should be highlighted as featured, false if not. | 
**isPrivate** | **Boolean** | True if a plan should not be presented in the primary plan options, false if not. | 
**price** | **Number** | The price of a plan. If a free plan then undefined. | [optional] 
**revenueType** | **String** | The revenue type a plan targets. | 
**subscriptionCode** | **String** | The subscription code a plan targets. | 
**tagline** | **String** | The short tagline for a plan. | 
**termsAndConditions** | **String** | The terms and conditions for a plan. | 
**title** | **String** | The title of a plan. | 
**trialPeriodDays** | **Number** | How many days a trial period runs for a plan. Only valid if &#x60;hasTrialPeriod&#x60; is true. | 
**type** | **String** | The type of plan. | 



## Enum: BillingPeriodTypeEnum


* `day` (value: `"day"`)

* `week` (value: `"week"`)

* `month` (value: `"month"`)

* `year` (value: `"year"`)

* `none` (value: `"none"`)





## Enum: RevenueTypeEnum


* `TVOD` (value: `"TVOD"`)

* `SVOD` (value: `"SVOD"`)





## Enum: TypeEnum


* `Free` (value: `"Free"`)

* `Subscription` (value: `"Subscription"`)




