# SearchAds360ReportingApi.GoogleAdsSearchads360V0ResourcesCampaignBudget

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**amountMicros** | **String** | The amount of the budget, in the local currency for the account. Amount is specified in micros, where one million is equivalent to one currency unit. Monthly spend is capped at 30.4 times this amount. | [optional] 
**deliveryMethod** | **String** | The delivery method that determines the rate at which the campaign budget is spent. Defaults to STANDARD if unspecified in a create operation. | [optional] 
**period** | **String** | Immutable. Period over which to spend the budget. Defaults to DAILY if not specified. | [optional] 
**resourceName** | **String** | Immutable. The resource name of the campaign budget. Campaign budget resource names have the form: &#x60;customers/{customer_id}/campaignBudgets/{campaign_budget_id}&#x60; | [optional] 



## Enum: DeliveryMethodEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `STANDARD` (value: `"STANDARD"`)

* `ACCELERATED` (value: `"ACCELERATED"`)





## Enum: PeriodEnum


* `UNSPECIFIED` (value: `"UNSPECIFIED"`)

* `UNKNOWN` (value: `"UNKNOWN"`)

* `DAILY` (value: `"DAILY"`)

* `FIXED_DAILY` (value: `"FIXED_DAILY"`)

* `CUSTOM_PERIOD` (value: `"CUSTOM_PERIOD"`)




