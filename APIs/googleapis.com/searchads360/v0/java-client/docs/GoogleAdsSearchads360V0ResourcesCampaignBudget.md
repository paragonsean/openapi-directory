

# GoogleAdsSearchads360V0ResourcesCampaignBudget

A campaign budget.

## Properties

| Name | Type | Description | Notes |
|------------ | ------------- | ------------- | -------------|
|**amountMicros** | **String** | The amount of the budget, in the local currency for the account. Amount is specified in micros, where one million is equivalent to one currency unit. Monthly spend is capped at 30.4 times this amount. |  [optional] |
|**deliveryMethod** | [**DeliveryMethodEnum**](#DeliveryMethodEnum) | The delivery method that determines the rate at which the campaign budget is spent. Defaults to STANDARD if unspecified in a create operation. |  [optional] |
|**period** | [**PeriodEnum**](#PeriodEnum) | Immutable. Period over which to spend the budget. Defaults to DAILY if not specified. |  [optional] |
|**resourceName** | **String** | Immutable. The resource name of the campaign budget. Campaign budget resource names have the form: &#x60;customers/{customer_id}/campaignBudgets/{campaign_budget_id}&#x60; |  [optional] |



## Enum: DeliveryMethodEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| STANDARD | &quot;STANDARD&quot; |
| ACCELERATED | &quot;ACCELERATED&quot; |



## Enum: PeriodEnum

| Name | Value |
|---- | -----|
| UNSPECIFIED | &quot;UNSPECIFIED&quot; |
| UNKNOWN | &quot;UNKNOWN&quot; |
| DAILY | &quot;DAILY&quot; |
| FIXED_DAILY | &quot;FIXED_DAILY&quot; |
| CUSTOM_PERIOD | &quot;CUSTOM_PERIOD&quot; |



